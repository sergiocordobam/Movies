from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    return render(request, 'home.html', {'name':'Sergio Córdoba'})

def about(request):
    return render(request, 'about.html')