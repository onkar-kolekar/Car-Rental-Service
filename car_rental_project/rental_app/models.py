from django.db import models

# Create your models here.
class registration(models.Model):
    car_type=(
        ('Compact','Compact'),
        ('Premium','Premium'),
        ('Minivan','Minivan'),
    )
    Booking_number=models.IntegerField(primary_key=True,auto_created=True)
    customer_name=models.CharField(max_length=50)
    Car_category=models.Choices(car_type)
    Time_date_for_the_rental=models.DateTimeField()
    Carmileage_in_kilometres=models.IntegerField()

class price(models.Model):
    baseDayRental=models.IntegerField()
    no_of_days=models.IntegerField()
    kilometerPrice=models.IntegerField()
    numberOfKilometers=models.IntegerField
    def get_computed(self):
        if registration.Car_category=='Compact':
            result = self.baseDayRental * self.numberOfDays
        elif registration.Car_category=='Premium':
            result = self.baseDayRental * self.numberOfDays * 1.2 + self.kilometerPrice * self.numberOfKilometers
        elif registration.Car_category=='Minivan':
            result = self.baseDayRental * self.numberOfDays * 1.7 + (self.kilometerPrice * self.numberOfKilometers * 1.5 )
        return result

class car_return(models.Model):
    register = models.ForeignKey(registration, on_delete=models.CASCADE)
    bk_no=registration.Booking_number
    time_date=registration.Time_date_for_the_rental
    mileage=registration.Carmileage_in_kilometres