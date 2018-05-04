Ubuntu
use virtualenv
command: virtualenv venv
than activate virtualenv
command: source venv/bin/activate
install django 1.9.7
command: pip install Django==1.9.7
create django project
command django-admin startproject mysite
create first app
command: python ./manage.py startapp catalog
create second one
command: python ./manage.py startapp my_app

than create superuser
python3 manage.py createsuper 
login: admin
password: admin12345

we need to create templates in such way my_rep/templates/my_rep and i this case django is able to see html files and we should update setting.py

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



used importin to db from csv files
file import.python3

if u forget admin password i recommend u a great topic : https://www.laurivan.com/change-a-django-password-manually/