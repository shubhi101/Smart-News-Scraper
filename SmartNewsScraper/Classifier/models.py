from __future__ import unicode_literals

from django.db import models

###To be added : Keywords List, Organisations List


# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=180)
	link=models.CharField(max_length=360)
	content=models.TextField
	pubdate=models.DateTimeField(auto_now=False)
	added_on=models.DateTimeField(auto_now=True)
	author=models.CharField(max_length=60)
	tags=models.CharField(max_length=180,blank=True) #for now, just deserialize the array and store
	sentiment=models.BooleanField #true=positive false=negative


#Other keywords that indicate any relevance.
class Keyword(models.Model):
	keyword=models.CharField(max_length=300)
	def __unicode__(self):
		return self.keyword

class RelatedKeywords(models.Model):
	article=models.OneToOneField(Article)
	keywords=models.ManyToManyField(Keyword,blank=True)
	def __unicode__(self):
		return self.article.title


#store all articles and keywords related to this person.
class Person(models.Model):
	name=models.CharField(max_length=60)
	keywords=models.ManyToManyField(Keyword,blank=True)
	def __unicode__(self):
		return self.name

#List of persons to whom the article is relevant.
class RelatedPersons(models.Model):
	article=models.OneToOneField(Article)
	person=models.ManyToManyField(Person,blank=True)
	def __unicode__(self):
		return self.person.name

#store all articles and keywords related to this organization.
class Organization(models.Model):
	name=models.CharField(max_length=60)
	keywords=models.ManyToManyField(Keyword,blank=True)
	def __unicode__(self):
		return self.name

#List of organizations to whom the article is relevant.
class RelatedOrganizations(models.Model):
	article=models.OneToOneField(Article)
	organization=models.ManyToManyField(Organization,blank=True)
	def __unicode__(self):
		return self.organization.name

#Synonyms used for the name of the college.
class Synonyms(models.Model):
	synonym=models.CharField(max_length=300)
	def __unicode__(self):
		return self.synonym




	