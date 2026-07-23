from django.db import models
from chefs.models import Chef
from .choices import category_choices, district_choices

class Listing(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50, choices=district_choices.items(),default='')
    cuisine_choices=models.CharField(max_length=50,choices=category_choices.items(),default='') # cuisine_choices
    description=models.TextField(blank=True)
    specialty=models.IntegerField() # specialty
    room_type=models.CharField(max_length=50)
    has_wifi=models.BooleanField(default=True) # has_wifi
    has_delivery=models.BooleanField(default=True) # has_delivery
    rating=models.FloatField(default = 0.0) # add default value
    opening_hours=models.TimeField()  #opening_hours
    price=models.IntegerField()
    promo_badge_text = models.CharField(max_length=100, blank=True, null=True)
    accepts_reservations = models.BooleanField(default=False)
    ambiance_note = models.CharField(max_length=100, blank=True)
    contant_number = models.CharField(max_length=20, blank=True)

    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering= ['-list_date']
        indexes = [models.Index(fields=['list_date'])]

    def __str__(self):
       return self.title