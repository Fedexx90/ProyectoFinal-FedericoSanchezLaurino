from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Auto


# --- LISTAR AUTOS (con login y filtros independientes) ---
class AutoListView(LoginRequiredMixin, ListView):
    model = Auto
    template_name = 'cars/auto_list.html'
    context_object_name = 'autos'
    login_url = 'accounts:login'

    def get_queryset(self):
        qs = super().get_queryset()

        # Campos del formulario GET
        q = (self.request.GET.get('q') or '').strip()
        anio_min = (self.request.GET.get('anio_min') or '').strip()
        anio_max = (self.request.GET.get('anio_max') or '').strip()
        precio_min = (self.request.GET.get('precio_min') or '').strip()
        precio_max = (self.request.GET.get('precio_max') or '').strip()

        # --- FILTROS COMBINABLES ---
        if q:
            qs = qs.filter(Q(marca__icontains=q) | Q(modelo__icontains=q))
        if anio_min:
            qs = qs.filter(anio__gte=anio_min)
        if anio_max:
            qs = qs.filter(anio__lte=anio_max)
        if precio_min:
            qs = qs.filter(precio__gte=precio_min)
        if precio_max:
            qs = qs.filter(precio__lte=precio_max)

        return qs


# --- DETALLE DE AUTO ---
class AutoDetailView(DetailView):
    model = Auto
    template_name = 'cars/auto_detail.html'
    context_object_name = 'auto'


# --- CREAR AUTO ---
class AutoCreateView(LoginRequiredMixin, CreateView):
    model = Auto
    template_name = 'cars/auto_form.html'
    fields = ['marca', 'modelo', 'anio', 'precio', 'descripcion', 'imagen']
    success_url = reverse_lazy('cars:auto_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# --- EDITAR AUTO ---
class AutoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Auto
    template_name = 'cars/auto_form.html'
    fields = ['marca', 'modelo', 'anio', 'precio', 'descripcion', 'imagen']
    success_url = reverse_lazy('cars:auto_list')

    def test_func(self):
        auto = self.get_object()
        return self.request.user == auto.user


# --- ELIMINAR AUTO ---
class AutoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Auto
    template_name = 'cars/auto_confirm_delete.html'
    success_url = reverse_lazy('cars:auto_list')

    def test_func(self):
        auto = self.get_object()
        return self.request.user == auto.user

# --- Agregar los valores al contexto ---
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['anio_min'] = self.request.GET.get('anio_min', '')
        context['anio_max'] = self.request.GET.get('anio_max', '')
        context['precio_min'] = self.request.GET.get('precio_min', '')
        context['precio_max'] = self.request.GET.get('precio_max', '')
        return context