from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Auto

# --- LISTAR AUTOS (con login requerido) ---
class AutoListView(LoginRequiredMixin, ListView):
    model = Auto
    template_name = 'cars/auto_list.html'
    context_object_name = 'autos'
    login_url = 'accounts:login'  # si no está logueado, redirige al login


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

