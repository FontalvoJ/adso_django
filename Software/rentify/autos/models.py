
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
import datetime

class Auto(models.Model):
    brand = models.CharField(max_length=100)  # Marca
    model = models.CharField(max_length=100)  # Modelo
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1886),
            MaxValueValidator(datetime.date.today().year)
        ]
    )
    color = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    price_per_day = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    location = models.CharField(max_length=100)
    image_url = models.URLField(validators=[URLValidator()])
    power = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    
    SYSTEM_CHOICES = [
        ("Gasolina", "Gasolina"),
        ("Diesel", "Diesel"),
        ("Electrónico", "Electrónico"),
        ("Híbrido", "Híbrido"),
    ]
    system = models.CharField(max_length=20, choices=SYSTEM_CHOICES)
    
    ACCOMPANISTS_CHOICES = [
        (2, "2"),
        (4, "4"),
        (5, "5"),
        (7, "7"),
    ]
    accompanists = models.IntegerField(choices=ACCOMPANISTS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "autos"  
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
