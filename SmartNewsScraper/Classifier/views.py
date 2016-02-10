from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request,'home.html',{})

def viewArticles(request):
	# articles=Article.objects.filter(relevant = True)
	# for article in articles:
	# 	article.summary = article.summary[:150]+"..."
	# print articles
	# response={}
	# response['articles']=articles
	# response['dtime']=datetime.datetime.now()
	
	return render(request,'showcase.html',{})