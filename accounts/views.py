from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm, CustomUserCreationForm

# -----------------------------
# LOGIN
# -----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect("cars:auto_list")  # redirige a la lista de autos
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")


# -----------------------------
# LOGOUT
# -----------------------------
def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("accounts:login")


# -----------------------------
# REGISTRO DE USUARIO
# -----------------------------
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            messages.success(request, f"¡Cuenta creada con éxito, {user.username}!")
            return redirect("home")  # redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# -----------------------------
# PERFIL DE USUARIO
# -----------------------------
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


# -----------------------------
# EDITAR PERFIL
# -----------------------------
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("accounts:profile")
        else:
            messages.error(request, "Por favor revisá los datos ingresados.")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

