'''
=============================================================================
Update word_features and/or synonyms.txt files and run this script to save
them to database.
=============================================================================

'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartNewsScraper.settings')
import django
django.setup()
from Classifier.models import *
from django.core.exceptions import MultipleObjectsReturned

with open("word_features.txt") as f:
	words = f.read().split('\n')
for w in words:
	try:
		Keyword.objects.get_or_create(keyword=w)
	except:
		pass

	
with open("synonyms.txt") as f:
	words = f.read().split('\n')
for w in words:
	try:
		Synonym.objects.get_or_create(synonym=w)
	except:
		pass

