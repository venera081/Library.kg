from django.shortcuts import render
from . import models


def search_view(request):
    query = request.GET.get('s', '')
    clothes_lst = models.Clothe.objects.filter(name_clothe__icontains=query) if query else models.Clothe.none
    context = {
        'clothes': clothes_lst,
        's': query
    }
    return render(request, template_name='clothes/all_clothes.html', context=context)


def all_clothes(request):
    if request.method == "GET":
        clothes = models.Clothe.objects.all().order_by('-id')
        return render(request, 'clothes/all_clothes.html', 
                      {'clothes': clothes})
    

def women_clothes(request):
    if request.method == "GET":
        clothes = models.Clothe.objects.filter(tags__name='#Одежда женская').order_by('-id')
        return render(request, 'clothes/women_clothes.html', 
                      {'clothes': clothes})
    

def men_clothes(request):
    if request.method == "GET":
        clothes = models.Clothe.objects.filter(tags__name='#Одежда мужская').order_by('-id')
        return render(request, 'clothes/men_clothes.html', 
                      {'clothes': clothes})
    
def kids_clothes(request):
    if request.method == "GET":
        clothes = models.Clothe.objects.filter(tags__name='#Одежда детская').order_by('-id')
        return render(request, 'clothes/kids_clothes.html', 
                      {'clothes': clothes})
    

    

    


    
    

    
