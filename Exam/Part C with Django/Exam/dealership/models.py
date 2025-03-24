from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    Address = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    stateprovince = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    colour = models.DecimalField(max_digits=10, decimal_places=2)
    car_for_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class salesinvoice(models.Model):
    invoive_number = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Salesperson(models.Model):
    Lastname = models.models.CharField(max_length=100)
    FirstName = models.models.CharField(max_length=100)

    def __str__(self):
        return f"{self.car} at {self.dealer}"

class Service_Ticket(models.Model):
    Service_ticket = models.CharField(max_length=100)
    car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Datareceived = models.DateField()
    comments = models.TextField(max_length=200)
    date_retunrted = models.DateField()

    def __str__(self):
        return f"Sale of {self.car} to {self.customer} on {self.sale_date}"
