from django.contrib import admin

from .models import Covid_Observations, CovidData

class CaseAdmin(admin.ModelAdmin):
    list_display = ("sno", "observationdate", "state", 'country', "last_updated", "confirmed", "deaths", "recovered")
    search_fields = ("sno",)

class CovidDataAdmin(admin.ModelAdmin):
    list_display = ("name", "filedata")
    search_fields = ("name",)

admin.site.register(Covid_Observations, CaseAdmin)
admin.site.register(CovidData, CovidDataAdmin)