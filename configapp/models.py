from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.model} - {self.number_plate}"


class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)  # Har bir haydovchida bitta mashina

    def __str__(self):
        return f"{self.name} ({self.car})"


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    distance_km = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def calculate_price(self):
        return round(self.distance_km * 5000, 2)  # 1 km = 5000 so‘m

    def __str__(self):
        return f"{self.user.name} → {self.to_address}"
