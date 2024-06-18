from django.shortcuts import render
# from .forms import RestaurantForm
from .models import *
from django.db.models import Sum
from django.db.models import Prefetch
from django.utils import timezone
# Create your views here.
def index(request):
    #prefetch_related  here restaurant can have many ratings so here we use prefetch_related

    # restaurants=Restaurant.objects.prefetch_related('ratings','sales')
    # restaurants=Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings','sales')
    # context = {'restaurants':restaurants}

    #select_related here rating is associated with one restaurant

    # ratings= Rating.objects.all()
    # ratings= Rating.objects.select_related('restaurant')# along with each rating we want to fetch associated restaurants
    # ratings= Rating.objects.only('rating','restaurant__name').select_related('restaurant')
    # context = {'ratings':ratings}

    # Get all 5 star ratings, and fetch all the sales for restaurants with 5 star ratings.

    # restaurants=Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5)

    # restaurants=Restaurant.objects.prefetch_related('ratings', 'sales') \
    #         .filter(ratings__rating=5) \
    #         .annotate(total=Sum('sales__income'))

    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # monthly_sales = Prefetch(
    #     'sales',
    #     queryset= Sale.objects.filter(datetime__gte = month_ago),
    # )
    # restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5) 
    # restaurants= restaurants.annotate(total=Sum('sales__income'))
    # print([r.total for r in restaurants])


    
    # context = {'ratings':ratings}
    # return render(request, 'index.html', context)
    return render(request, 'index.html')