<h3>Django Tutorial</h3>
<p>This is a django application developed from the official documentation's tutorial. This will explain you the flow of django framework.</p>
<p>To start with we have to create a virtual environment for django and access it.<br>
  <pre><code>python3 -m venv django-env
source django-env/bin/activate
</code></pre></p>
<p>After creating the virtual environment you need to install django</p>
<code>pip install django</code>
<p>Now you need to bootstrap a django project using the following command</p>
<code>django-admin startproject mysite django_tutorial</code>
<p>Now your directory looks something like this: <pre><code>django_tutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py</code></pre></p>
<p>In this the manage.py file is used to run the django application(s). The mysite directory is the project. Using this project directory you an create multiple applications.<li>To start with the first file is __ini__.py which indicates that the directory containing this file should be treated as the python project.</li><li>settings.py file is responsible for defining the configurations for our applications. Key components of settings.py</li><ul><code>DEBUG=True</code> We can turn on or off the debug mode using this. DEBUG should be set to false when application is in production</ul><ul><code>ALLOWED_HOSTS['*']</code> Using this we can specify what are the host/domain names your application could serve. This prevents HTTPS host head attacks</ul><ul><pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',  # Your app
]</code></pre>INSTALLED_APPS contains django's built in apps and custom apps you have created.</ul>
<ul><code>DATABASES</code> contains configurations for connecting to your database.</ul>
<li>urls.py contains path to all your applications in the django project</li>
<li>asgi.py is an entry-point for ASGI-compatible web servers to serve your project</li>
<li>wsgi.py is an entry-point for WSGI-compatible web servers to serve your project</li></p>
After successfully creating the project you need to make applications. For creating the applications you need to create an app in the same directory.<br><code>python manage.py startapp poll</code>
<p>This will create a app directory poll which is laid out something like this.<pre><code>polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    views.py</code></pre></p>
    <p><li>Just like the project directory the __init__.py file here too indicates that this file should be treated as a python package which allows you to import modules from this directory.</li>  </p>
    <li>admin.py file is used for configuring the django admin interface.</li>
    <li>apps.py file contains the configurations of the application. It defines the app's name and configurations.</li>
    <li>the migrations directory contains the information about the files migrations which are used to manage changes to your database schema.</li>
    <li>models.py file is where you define the database models. Each model corresponds to a database table and defines the structure of the data.</li>
<li>
  In views.py file you define the views for your application. Views handle the logic behind what data is displayed and how it is presented to the user.
</li>
<p>To run your application run the command <code>python manage.py runserver</code>. If you have any changes in your database run the commands <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre></p>
  
  

