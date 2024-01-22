from django.shortcuts import render

# Create your views here.

# home page
def home_page_view(request):

    return render(request, 'main/index.html')

# about page
def about_page_view(request):

    return render(request, 'main/about.html')

# portfolio page
def portfolio_page_view(request):

    return render(request, 'main/portfolio.html')
  
# contact page
def contact_page_view(request):

    return render(request, 'main/contact.html')

# wedo page
def wedo_page_view(request):

    return render(request, 'main/we_do.html')