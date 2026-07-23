from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q
from.choices import category_choices,district_choices,price_choices

# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    current_time = timezone.localtime().time()
    context = {"listings":paged_listings, "current_time":current_time}
    return render(request,"listings/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    current_time = timezone.localtime().time()
    context = {"listing":listing, "current_time":current_time}
    return render(request,"listings/listing.html", context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    current_time = timezone.localtime().time()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords))
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(cuisine_choices__iexact=category)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            if price =='Budget': 
                queryset_list = queryset_list.filter(price__lte=200)
            if price =='Average': 
                queryset_list = queryset_list.filter(price__gt=200).filter(price__lte=400)
            if price =='Puremium': 
                queryset_list = queryset_list.filter(price__gt=400)
    if 'open' in request.GET:
            open = request.GET['open']
            if open == 'yes':
                queryset_list = queryset_list.filter(opening_hours__gte=current_time)

    paginator = Paginator(queryset_list, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    context = {"listings":paged_listings, 
               "current_time":current_time, 
               "category_choices":category_choices, 
               "district_choices":district_choices, 
               "price_choices":price_choices, 
               "values" : request.GET}
    return render(request,"listings/search.html", context)


