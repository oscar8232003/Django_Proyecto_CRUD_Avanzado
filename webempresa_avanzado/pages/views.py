from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page, Ofertas
from .forms import PageForm


class StaffRequiredMixin(object):
    """este mixin reqeurira que el usuario sea miembro del staff"""

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #if not request.user.is_staff:   #el @method hace el trabajo de este if
            #return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    """
      def dispatch(self, request, *args, **kwargs):
        #if not request.user.is_staff:   #el @method hace el trabajo de este if
            #return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    """


class PageListView(ListView):#Sirve para llamar una lista, para usarlo es objects o page(nombre del modelo), el template tiene que cambiarse igual para que lo reconosca
    model = Page
    template_name_suffix = '_listar'

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['Ofertas'] = Ofertas.objects.all()
        #context['Paginas'] = Ofertas.objects.all()
        return context


class pageDetailView(DetailView):#Sirve para llamar 1 objeto para usarlo es objects o page(nombre del modelo)
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order'] #Ya se encuentra en el form
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'#Nombre del template

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'


class PageDelete(StaffRequiredMixin, DeleteView): #Otra forma de llamar al dispatch con su clase
    model = Page
    success_url = reverse_lazy('pages:pages')