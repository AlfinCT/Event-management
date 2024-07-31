from django.contrib import admin

from event.models import Work, Team, Client,BookEvent,Rate

# Register your models here.
admin.site.register(Work)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(BookEvent)
admin.site.register(Rate)