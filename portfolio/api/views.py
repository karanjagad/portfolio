from django.shortcuts import render

def ContactView(request):
    return render(request, 'api/home.html')  # Make sure this path is correct
