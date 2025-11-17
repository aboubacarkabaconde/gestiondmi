from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employe
from .forms import EmployeForm


@login_required
def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, "sites/employes/liste.html", {"employes": employes})


@login_required
def ajouter_employe(request):
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employé ajouté avec succès !")
            return redirect("sites:liste_employes")
    else:
        form = EmployeForm()

    return render(request, "sites/employes/form.html", {"form": form})


@login_required
def modifier_employe(request, id):
    employe = get_object_or_404(Employe, pk=id)
    if request.method == "POST":
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            messages.success(request, "Employé modifié avec succès !")
            return redirect("sites:liste_employes")
    else:
        form = EmployeForm(instance=employe)

    return render(request, "sites/employes/form.html", {"form": form})


@login_required
def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, pk=id)
    if request.method == "POST":
        employe.delete()
        messages.success(request, "Employé supprimé avec succès !")
        return redirect("sites:liste_employes")

    return render(request, "sites/employes/supprimer.html", {"employe": employe})
