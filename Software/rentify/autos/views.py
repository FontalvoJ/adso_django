from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from .forms import AutoForm

# 🔹 Listar autos
def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/lista_autos.html", {"autos": autos})

# 🔹 Crear un auto
def crear_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_autos")  
    else:
        form = AutoForm()  

    return render(request, "autos/crear_auto.html", {"form": form})

# 🔹 Detalle de un auto
def detalle_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, "autos/detalle_auto.html", {"auto": auto})

# 🔹 Editar un auto
def editar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == "POST":
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect("lista_autos")
    else:
        form = AutoForm(instance=auto)
    return render(request, "autos/editar_auto.html", {"form": form, "auto": auto})

# 🔹 Eliminar un auto
def eliminar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == "POST":
        auto.delete()
        return redirect("lista_autos")
    return render(request, "autos/eliminar_auto.html", {"auto": auto})


def inicio(request):
   return render(request, "autos/inicio.html")