from django.shortcuts import render
from listings.models import Listing 
from django.utils import timezone
from listings.choices import category_choices,district_choices, price_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    top_rated = Listing.objects.order_by("-rating").filter(is_published=True)[:3]
    current_time = timezone.localtime().time()
    context = {"listings" : listings, "current_time" : current_time, "top_rated": top_rated, 
    "category_choices" :category_choices , "district_choices" :district_choices, "price_choices" : price_choices }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')

