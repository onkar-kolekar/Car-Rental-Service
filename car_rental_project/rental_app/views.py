from django.shortcuts import render,HttpResponseRedirect
from .models import registration,price
from .forms import reg_class,priceform,car_return_form
# Create your views here.

def reg_view(r):
    form=reg_class()
    if r.method=='POST':
        form=reg_class(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/show_price_details')
    return render(r,'rental_app/car_registration_form.html',{'form':form})

def car_return(r):
    form=priceform()
    if r.method=='POST':
        form=reg_class(r.POST)
        if form.is_valid():
            form.save()
    return render(r,'rental_app/car_return.html',{'form':form})

def showpricedata(r,booking_no):
    form=car_return_form.objects.get(booking_no=booking_no)
    return render(r,'rental_app/price.html',{'form':form})
