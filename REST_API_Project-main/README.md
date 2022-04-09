# DjangoHotelMgmtSystem
--------------------------
Step-1: 
Clone the repository using $ git clone https://github.com/prabav639/DjangoHotelMgmtSystem.git 
and get into the repository using **cd DjangoHotelMgmtSystem**

Step-2:
Install the dependencies using pip install
Used conda environment to perform the task

Step-3:
Open the file using any IDE and change the database settings in testproject/settings.py file under DATABASES {}

Step-4:
Make the necessary migrations to add the tables into DB using the command;
$ python manage.py makemigrations -> Will create migrations file
$ pythonmanage.py migrate -> To complete the migration

Step-5:
Run the server using the command;

$ python manage.py runserver

Step-6:
It will start running in the address: https://127.0.0.1:8000

We can make the GET and POST requests using any application like POSTMAN etc;
