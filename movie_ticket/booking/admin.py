from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Screening)
admin.site.register(Booking)

