from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            "brand",
            "model",
            "year",
            "color",
            "availability",
            "price_per_day",
            "location",
            "image_url",
            "power",
            "system",
            "accompanists",
        ]
        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            "availability": "Disponible",
            "price_per_day": "Precio por día",
            "location": "Ubicación",
            "image_url": "Imagen (URL)",
            "power": "Potencia (HP)",
            "system": "Sistema",
            "accompanists": "Acompañantes",
        }
        widgets = {
            "year": forms.NumberInput(attrs={"min": 1886, "max": 2025}),
            "price_per_day": forms.NumberInput(attrs={"step": "0.01"}),
            "color": forms.TextInput(attrs={"placeholder": "Ej: Rojo"}),
            "location": forms.TextInput(attrs={"placeholder": "Ej: Bogotá"}),
            "image_url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "availability": forms.CheckboxInput(),
            "system": forms.Select(),
            "accompanists": forms.Select(),
        }
