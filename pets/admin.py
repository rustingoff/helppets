from django.contrib import admin

# Register your models here.
from .models import MainSlider, About, RoadMap, Service, DonationCase, News, Subscribe

admin.site.register(MainSlider)
admin.site.register(About)
admin.site.register(RoadMap)
admin.site.register(Service)
admin.site.register(DonationCase)
admin.site.register(News)
admin.site.register(Subscribe)
# Compare this snippet from pets/views.py:
