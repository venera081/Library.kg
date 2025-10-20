from django.shortcuts import render
from . import models
from django.views import generic


class SearchView(generic.ListView):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            clothes_lst = models.Clothe.objects.filter(name_clothe__icontains=query) 
        else:
            clothes_lst = models.objects.none
        context = {
            'clothes': clothes_lst,
            's': query
        }
        return render(request, template_name='clothes/all_clothes.html', context=context)


# def search_view(request):
#     query = request.GET.get('s', '')
#     clothes_lst = models.Clothe.objects.filter(name_clothe__icontains=query) if query else models.Clothe.none
#     context = {
#         'clothes': clothes_lst,
#         's': query
#     }
#     return render(request, template_name='clothes/all_clothes.html', context=context)


class AllClothesView(generic.ListView):
    model = models.Clothe
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'clothes'

# def all_clothes(request):
#     if request.method == "GET":
#         clothes = models.Clothe.objects.all().order_by('-id')
#         return render(request, 'clothes/all_clothes.html', 
#                       {'clothes': clothes})
    

class WomenClothesView(generic.ListView):
    model = models.Clothe
    template_name = 'clothes/women_clothes.html'
    context_object_name = 'clothes'
    ordering = '-id'

    def get_queryset(self):
        women_clothes = self.model.objects.filter(tags__name='#Одежда женская')
        return women_clothes

# def women_clothes(request):
#     if request.method == "GET":
#         clothes = models.Clothe.objects.filter(tags__name='#Одежда женская').order_by('-id')
#         return render(request, 'clothes/women_clothes.html', 
#                       {'clothes': clothes})
    

class MenClothesView(generic.ListView):
    model = models.Clothe
    template_name = 'clothes/men_clothes.html'
    context_object_name = 'clothes'
    ordering = '-id'

    def get_queryset(self):
        men_clothes = self.model.objects.filter(tags__name='#Одежда мужская')
        return men_clothes

# def men_clothes(request):
#     if request.method == "GET":
#         clothes = models.Clothe.objects.filter(tags__name='#Одежда мужская').order_by('-id')
#         return render(request, 'clothes/men_clothes.html', 
#                       {'clothes': clothes})


class KidsClothesView(generic.ListView):
    model = models.Clothe
    template_name = 'clothes/kids_clothes.html' 
    context_object_name = 'clothes' 
    ordering = '-id'

    def get_queryset(self):
        kids_clothes = self.model.objects.filter(tags__name='#Одежда детская')
        return kids_clothes

# def kids_clothes(request):
#     if request.method == "GET":
#         clothes = models.Clothe.objects.filter(tags__name='#Одежда детская').order_by('-id')
#         return render(request, 'clothes/kids_clothes.html', 
#                       {'clothes': clothes})
    

    

    


    
    

    
