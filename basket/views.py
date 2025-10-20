from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


class CreateBasketView(generic.CreateView):
    model = models.Basket
    form_class = forms.BasketForm
    template_name = 'basket/create_basket.html'
    success_url = '/basket_list/'


# def createBasket(request):
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = forms.BasketForm()
#     return render(request, template_name='basket/create_basket.html',
#                   context={'form': form})


class ReadStudentView(generic.ListView):
    model = models.Basket
    template_name = 'basket/basket_list.html'
    context_object_name = 'bask'

# def readBasket(request):
#     if request.method == 'GET':
#         basket = models.Basket.objects.all().order_by('-id')
#     return render(request, template_name='basket/basket_list.html', 
#                   context={'bask': basket})

class UpdateBasketView(generic.UpdateView):
    model = models.Basket
    form_class = forms.BasketForm
    template_name = 'basket/update_basket.html' 
    success_url = '/student_list/'    

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

# def updateBasket(request, id):
#     basket_id = get_object_or_404(models.Basket, id=id)
#     if request.method == 'POST':
#          form = forms.BasketForm(request.POST, instance=basket_id)
#          if form.is_valid():
#              form.save()
#              return redirect('basket_list')
#     else:
#         form = forms.BasketForm(instance=basket_id)
    
#     return render(request, template_name='basket/update_basket.html',
#                   context={
                    #   'form': form,
                    #   "basket_id": basket_id,
                    #   })



class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)
# def deleteBasket(request, id):
#     basket_id = get_object_or_404(models.Basket, id=id)
#     basket_id.delete()
#     return redirect('basket_list')
