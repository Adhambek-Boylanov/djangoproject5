from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContractForm, DriverForm, UserForm,CarForm
def index(request):
    cars = Car.objects.all()
    users = User.objects.all()
    contracts = Contract.objects.all()
    drivers = Driver.objects.all()
    context = {
        'cars':cars,
        'users':users,
        'drivers':drivers,
        'contracts':contracts
    }
    return render(request,'index.html',context=context)
def create_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.price = contract.calculate_price()
            contract.save()
            return redirect('dashboard')
    else:
        form = ContractForm()
    return render(request, 'create_contract.html', {'form': form})

# Shartnoma tafsilotlari
def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contract_detail.html', {'contract': contract})

# Haydovchilar ro‘yxati
def drivers_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers_list.html', {'drivers': drivers})

# Yangi haydovchi qo‘shish
def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DriverForm()
    return render(request, 'add_driver.html', {'form': form})

# Foydalanuvchilar ro‘yxati
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

# Yangi foydalanuvchi qo‘shish
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def contracts_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts_list.html', {'contracts': contracts})

def update_drivers(request,pk):
    drivers = get_object_or_404(Driver,id=pk)
    if request.method == "POST":
        form = DriverForm(request.POST,instance=drivers)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DriverForm(instance=drivers)
    return render(request,'update_drivers.html',{'form':form,'drivers':drivers})
