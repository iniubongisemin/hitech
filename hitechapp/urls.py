from django.urls import path
from .views import home_page_view, about_page_view, portfolio_page_view, contact_page_view, wedo_page_view


urlpatterns = [
    path('', home_page_view, name = 'home'),
    path('about/', about_page_view, name = 'about'),
    path('portfolio/', portfolio_page_view, name = 'portfolio'),
    path('contact/', contact_page_view, name = 'contact'),
    path('we_do/', wedo_page_view, name = 'wedo') 
] 