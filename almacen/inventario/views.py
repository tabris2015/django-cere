from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Item, Categoria, Encargado
from .forms import ItemForm, CategoriaForm


class EncargadosListView(ListView):
    model = Encargado
    context_object_name = 'encargados'


class CrearYListarView(View):
    name = 'objects'
    template = 'default'
    form = None
    model = None

    def get(self, request):
        return render(
            request,
            self.template,
            {
                self.name: self.model.objects.all(),
                'form': self.form()
            }
        )

    def post(self, request):
        form = self.form(request.POST)
        form.save()
        return HttpResponseRedirect(reverse(f'inventario:{self.name}'))


class ItemView(CrearYListarView):
    name = 'items'
    template = 'inventario/items.html'
    form = ItemForm
    model = Item


class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventario/detalle_item.html'
    slug_field = 'id'


class EncargadoDetailView(DetailView):
    model = Encargado
    template_name = 'inventario/detalle_encargado.html'
    slug_field = 'id'


class CategoriaView(CrearYListarView):
    name = 'categorias'
    template = 'inventario/categorias.html'
    form = CategoriaForm
    model = Categoria



@login_required
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
