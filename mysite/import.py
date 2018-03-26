#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv,sys,os

project_dir = '/home/vova/MyProject_Django/Django_project/mysite/mysite'

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from catalog.models import Catalog

data = csv.reader(open('/home/vova/MyProject_Django/Django_project/mysite/data.csv'), delimiter=",")

for row in data:
	if row[0] != 'Наименование':
		print(row[0])
		post = Catalog()
		post.name = row[0]
		post.place = row[1]
		post.price = row[2]
		post.save()