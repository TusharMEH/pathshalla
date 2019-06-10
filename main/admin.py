from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
	

	fieldsets = [("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
				 
				 ("content",{"fields":["tutorial_content"]}),
				 ("URL",{"fields":["tutorial_slug"]}),
				 ("Series",{"fields":["tutorial_series"]}),
			]

	formfield_overrides={models.TextField:{'widget':TinyMCE()}}



admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial,TutorialAdmin)