from django.contrib import admin
from storage.models import SourceFeed, News

admin.site.register(SourceFeed)
admin.site.register(News)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('published_datetime',)