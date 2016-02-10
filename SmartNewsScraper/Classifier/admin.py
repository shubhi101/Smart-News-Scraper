from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Keyword)
admin.site.register(RelatedKeywords)
admin.site.register(Person)
admin.site.register(RelatedPersons)
admin.site.register(Organization)
admin.site.register(RelatedOrganizations)
admin.site.register(Synonyms)