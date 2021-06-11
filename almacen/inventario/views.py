from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Item
from .forms import ItemForm


def items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('inventario:items'))
    else:
        items_list = Item.objects.all()
        form = ItemForm()
        context = {
            'items': items_list,
            'form': form
        }
        return render(request, 'inventario/items.html', context)
