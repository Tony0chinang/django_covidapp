# django_covidapp

- This is an example of COVID Cases Web App implemented using python/Django.
- This project holds a csv file which will be extracted when the web app starts.
- This project will extract a csv file which contains covid cases data and displays thru and endpoint.


## Installation (Windows)

###### Technology Requirements:
- **Python 3** – To install python 3, follow the instructions found here at the Python Software Foundations downloads page. The current Python version is v3.6.0.
- **Pip** - Included with Python 3 is the pip tool. To check, enter this command from Command prompt: 
		
       pip --version
       
- **VirtualEnv** – VirtualEnv create virtual space/environment which isolate you project from overriding any files or libraries belong to another project. To install, enter this command from Command prompt.
		
      pip install vitualenv
      
- **Django** – This is applications framework used to create the web app, it will be installed later.

###### Instructions:
1.	Make sure to install the technology requirements first.
2.	Extract the downloaded zip project to your specific folder.
3.	Go to project folder [‘django_covidapp-main’] thru the command prompt.
4.	From the command prompt, create a virtual environment (‘env’ folder) for this project by running this from the command prompt.
      
            Vitualenv env

      You now have 2 folders inside ‘django_covidapp-main’ folder. ‘env’ folder and ‘covidapp’ folder.

5.	Activate your virtual environment for this project by running this from the command prompt.

            Env\scripts\activate
            
      You should see an '(env)' from the start of command prompt.
      
6.	Change folder to ‘covidapp’. Once you’re inside the ‘covidapp’ folder, you should see ‘requirements.txt’ file.
7.	Install Django and all the necessary libraries by running this from the command prompt.

            pip install -r requirements.txt
            
       This project is now ready to run locally.
      
      This project is now ready to run locally.
        
###### Run Project Locally:

8.	To run the project local server, enter this command from Command prompt:

            manage.py runserver
            
9.	Once the development server started at ‘http://127.0.0.1:8000/’, open this url to your website to test the web app/website.

      **Note:** In case port 8000 is not available to your machine, you can change it (say, port 9000) by running this from the command prompt.
	
                manage.py runserver 9000
            
      Once the development server started at ‘http://127.0.0.1:9000/’, open this url to your website to test the web app/website.

10.	To stop the development server press ‘Ctrl +End’ keys.

###### Admin Section of the site:

Django has a build-in administration dashboard which displays all tables and apps used by the project.
Use this url to access the administration dashboard.

             http://127.0.0.1:8000/admin/
          
              Username: admin
              Password: admin

**Tables:**
1.	Covid datas: holds the csv file that will be extracted by the web app.
2.	Covid_observationss: holds all covid cases record extracted from the csv file,

    **Note:** The table label was pluralized by django by default which is why there is a double s from the label, the database table is named ‘Covid_observations’..

