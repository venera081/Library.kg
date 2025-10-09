from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def createBasket(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/create_basket.html',
                  context={'form': form})


def readBasket(request):
    if request.method == 'GET':
        basket = models.Basket.objects.all().order_by('-id')
    return render(request, template_name='basket/basket_list.html', 
                  context={'bask': basket})

        

def updateBasket(request, id):
    basket_id = get_object_or_404(models.Basket, id=id)
    if request.method == 'POST':
         form = forms.BasketForm(request.POST, instance=basket_id)
         if form.is_valid():
             form.save()
             return redirect('basket_list')
    else:
        form = forms.BasketForm(instance=basket_id)
    
    return render(request, template_name='basket/update_basket.html',
                  context={
                      'form': form,
                      "basket_id": basket_id,
                      })



def deleteBasket(request, id):
    basket_id = get_object_or_404(models.Basket, id=id)
    basket_id.delete()
    return redirect('basket_list')
