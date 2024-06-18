from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    staff, created = Staff.objects.get_or_create(name='John Wick')
    print(staff)
    # print(type(staff.restaurants))
    print(staff.restaurants.all())
    staff.restaurants.add(Restaurant.objects.first())
    print(staff.restaurants.all())




    # pprint(connection.queries)
