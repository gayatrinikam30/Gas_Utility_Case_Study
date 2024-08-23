CASE STUDY-

A gas utility company is experiencing a high volume of customer service requests. The 
company's current system is not able to handle the volume of requests, and customers are 
experiencing long wait times and poor service.

Develop a Django application to provide consumer services for gas utilities. The application 
would allow customers to submit service requests online, track the status of their requests, 
and view their account information.

The application would also provide customer support representatives with a tool to manage 
requests and provide support to customers.

Here are some specific features that the Django application should include:
Service requests: The application would allow customers to submit service requests online. 
This would include the ability to select the type of service request, provide details about the 
request, and attach files.

Request tracking: The application would allow customers to track the status of their service 
requests. This would include the ability to see the status of the request, the date and time 
the request was submitted, and the date and time the request was resolved.

Bonus Points for structure of the django application codebase

TO RUN THE PROJECT-

1. Install Python:
Make sure you have Python installed on your system. Django typically works with Python 3.x.

You can check your Python version with:
python --version

2. Create a Virtual Environment:
It's a good practice to use a virtual environment for your Django project to manage dependencies.

python -m venv myenv

Activate the virtual environment:

On Windows:
myenv\Scripts\activate
On macOS/Linux:
source myenv/bin/activate

3. Install Django and Other Dependencies:

Navigate to your project directory and install Django along with Django REST Framework:
pip install django djangorestframework

Make Migrations:

4. Create migrations for your models:

python manage.py makemigrations

Apply Migrations:

Apply the migrations to create the database schema:

python manage.py migrate

5.Create a Superuser
To access the Django admin interface, create a superuser:

python manage.py createsuperuser

Follow the prompts to set up a username, email, and password.

6.Run the Development Server
Start the Django development server:

python manage.py runserver

7. Access the Application
Visit the Admin Interface:
Open your web browser and go to:

http://127.0.0.1:8000/admin/
Log in with the superuser credentials you created.

There you can add you service request using 
+Add 
and this request will saved with the date and time 
You can check your request over there later also change them and delete them .
