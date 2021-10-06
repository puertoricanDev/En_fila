from django.shortcuts import render

# Create your views here.
def managementIndex(request):
    return render(request, "management/index.html")