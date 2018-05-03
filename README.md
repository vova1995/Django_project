use virtualenv
command: virtualenv venv
than activate virtualenv
command source venv/bin/activate
install django 1.9.7
command: pip install Django==1.9.7
create django project
command django-admin startproject mysite
create first app
command: python ./manage.py startapp catalog
create second one
command: python ./manage.py startapp my_app
install django rest framework
commands:
pip install djangorestframework
additional packages
pip install markdown  
pip install pyyaml    
pip install django-filter  
can be download from github:
git clone git@github.com:tomchristie/django-rest-framework.git
cd django-rest-framework
pip install -r requirements.txt
pip install -r optionals.txt

than create superuser
python3 manage.py createsuper 
login: admin
password: admin12345

used importin to db from csv files
file import.python3