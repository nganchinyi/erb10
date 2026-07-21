from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from django.utils import timezone

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
    return render(request,"listings/listing.html")

def search(request):
    return render(request,"listings/search.html")
