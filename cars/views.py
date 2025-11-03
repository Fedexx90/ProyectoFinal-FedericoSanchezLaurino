from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Auto
from .forms import AutoForm

# Mostrar lista de autos con filtros
def auto_list(request):
    query = request.GET.get('q')  # búsqueda por texto
    anio = request.GET.get('anio')  # filtro por año
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    autos = Auto.objects.all()

    # Filtro de búsqueda (marca o modelo)
    if query:
        autos = autos.filter(
            Q(marca__icontains=query) | Q(modelo__icontains=query)
        )

    anio_min = request.GET.get('anio_min')
    anio_max = request.GET.get('anio_max')

    # Filtro por rango de años
    if anio_min:
        autos = autos.filter(anio__gte=int(anio_min))
    if anio_max:
        autos = autos.filter(anio__lte=int(anio_max))

    # Filtro por rango de precios
    if precio_min:
        autos = autos.filter(precio__gte=precio_min)
    if precio_max:
        autos = autos.filter(precio__lte=precio_max)

    # Crear lista de años predefinida (1910 a 2025)
    anios_disponibles = list(range(2025, 1909, -1))

    context = {
        'autos': autos,
        'query': query,
        'anio': anio,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'anios_disponibles': anios_disponibles,
    }
    return render(request, 'cars/auto_list.html', context)

# Detalle de un auto
def auto_detail(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'cars/auto_detail.html', {'auto': auto})

# Crear un auto nuevo
@login_required
def auto_create(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            auto = form.save(commit=False)
            auto.creador = request.user  # 👈 asigna el usuario actual
            auto.save()
            return redirect('cars:auto_list')
    else:
        form = AutoForm()
    return render(request, 'cars/auto_form.html', {'form': form})

# Editar un auto
@login_required
def auto_update(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('auto_list')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'cars/auto_form.html', {'form': form})

# Eliminar un auto
@login_required
def auto_delete(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        auto.delete()
        return redirect('auto_list')
    return render(request, 'cars/auto_confirm_delete.html', {'auto': auto})

