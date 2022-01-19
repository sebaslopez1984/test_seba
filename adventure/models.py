from django.db import models
import re
import math
# Create your models here.


class VehicleType(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    passengers = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    number_plate = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

    def can_start(self) -> bool:
        return self.vehicle_type.max_capacity >= self.passengers
    
    def validate_number_plate(self, patente):
        patronPatente = re.compile("[a-z]{3}-[\d]{3}-[\d]{3}")

        if patronPatente.search(patente):
            
            return True
        else:
            return False
    
    def get_distribution(self,cantidad):
        print(f"Si la cantidad de pasajeros son {cantidad}")
        if cantidad == 0:
            return []
    
        div= []
        filas = cantidad if cantidad == 2 else math.ceil(cantidad / 2)
        #print(f"filas => {filas}")
        esPar = True if cantidad % 2 == 0 else False

        count = filas - 1
        for f in range(0,filas):
            if count > 0:
                div.append([True,True])
        else:
            if esPar:
                if cantidad > 2:
                    div.append([True,True])
                div.append([False,False])
            else:
                div.append([True,False])
        count -= 1
    
        return div
    
class Journey(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.vehicle.name} ({self.start} - {self.end})"

    def is_finished(self, end):
        if end != 0:
            return True
        else:
            return False