from django.urls import path,include
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',views.home),
    path('about/',cache_page(20)(views.about)),
    path('menu/',views.menu,name='menu'),
    path('delete/',views.delete,name='delete')
]