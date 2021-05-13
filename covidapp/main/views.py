from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.staticfiles.storage import staticfiles_storage
from datetime import date, time, datetime
from django.utils.dateparse import parse_date
from dateutil.parser import *

import csv
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from covidapp.settings import MEDIA_ROOT

from .models import Covid_Observations as Case
from .models import CovidData

def extract_file(url):  
    print(url)
    count = 1
    
    with open(url, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            #if count < 51:
            print(line)
            if line[0] != 'SNo':
                observation = line[1]                                     
                lastupdate = line[4]
                confirmed = line[5]            
                confirm = confirmed.split(".",1)[0]
                deaths = line[6]            
                death = deaths.split(".",1)[0]
                recovered = line[7]            
                recover = recovered.split(".",1)[0]
                
                #create record
                case = Case()
                case.sno =  line[0]
                case.observationdate =  parse(observation)
                case.state =  line[2]
                case.country =  line[3]
                case.last_updated =  parse(lastupdate)
                case.confirmed =  (confirm)
                case.deaths =  (death)
                case.recovered =  (recover)
                case.save()
                print('new record saved...')
                
                #count = count+1

def home(request):    
    firstopen = request.session.get('newopen')
    
    cases = Case.objects.all().order_by('sno')
    coviddata = get_object_or_404(CovidData, name='covid')
        
    if firstopen is None:
        print("creating session...")
        request.session['newopen'] = '1'
            
        return render(request,'home0.html', {})
        
    elif firstopen == '1':
        print(firstopen)
        print("session exist...")
        print(coviddata.name)
        print(coviddata.filedata.url)
        url = f"{MEDIA_ROOT}/{coviddata.filedata}"    
        
        if cases.count():
            print('has data...' + str(cases.count()))
            #Case.objects.all().delete()
            ccount = cases.count()
        else:
            extract_file(url)
            cases = Case.objects.all().order_by('sno')
            ccount = cases.count()
        
        return render(request,'home1.html', { 'ccount':ccount })
                   
def search(request):
    print(request.GET)
    print(request.GET.get('observation_date'))
    print(request.GET.get('max_results'))
       
    print('searching...')
    return render(request,
                  'search.html',
                  {})

class TopConfirmedCases(APIView):
    def get(self, request):
        print(request.GET)
        print(request.GET.get('observation_date'))
        print(request.GET.get('max_results'))
        
        searddate = request.GET.get('observation_date')
        max_results = request.GET.get('max_results')
        
        querydate = parse(searddate)        
        queryset = Case.objects.filter(observationdate=querydate)
        
        countries = []
        for country in queryset:
            countries.append(country.country)           
        
        ucountries = set(countries)
        data = []
        for u in ucountries:
            bycountryqueryset = Case.objects.filter(observationdate=querydate).filter(country=u)
            print(str(bycountryqueryset.count()))
            xcountry = u
            xconfirmed = 0
            xdeaths = 0
            xrecovered = 0
            for bycountry in bycountryqueryset:
                xconfirmed = xconfirmed + bycountry.confirmed
                xdeaths = xdeaths + bycountry.deaths
                xrecovered = xrecovered + bycountry.recovered
                
            xdata=({
                'country': xcountry,
                'confirmed': xconfirmed,
                'deaths': xdeaths,
                'recovered': xrecovered,
            })
            if isinstance(data, list):
                print("data is exist...")
                data.append(xdata)
            else:
                print("creating data list...")
                data = (xdata)
            
        data.sort(key=lambda item: item.get("confirmed"),reverse=True)
       
        print('searching...')
        return Response({"observation_date":searddate,"countries": data[:int(max_results)]})

def clearData(request): 
    cases = Case.objects.all().order_by('sno')
    coviddata = get_object_or_404(CovidData, name='covid')
    
    if cases.count():
        print('has data...' + str(cases.count()))
        Case.objects.all().delete()
        del request.session['newopen']

               
    return redirect('home')
