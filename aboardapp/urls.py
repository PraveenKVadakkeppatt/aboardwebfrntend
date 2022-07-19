from . import views
from django.urls import path,include

urlpatterns = [
        path('', views.home, name='home'),
        path('base', views.base, name='base'),
        path('it_head', views.it_head, name='it_head'),
        path('profile', views.profile, name='profile'),
        path('leads_option', views.leads_option, name='leads_option'),
        path('add_leads', views.add_leads, name='add_leads'),


        

]