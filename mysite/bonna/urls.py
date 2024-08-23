from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_district', add_district, name='add_district'),
    path('add_union_ward', add_union_ward, name='add_union_ward'),
    path('get_upozillas/<int:district_id>/', get_upozillas, name='get_upozillas'),
]