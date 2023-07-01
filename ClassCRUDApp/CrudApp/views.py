from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


def goHome(request):
    Employees = EmployeeModel.objects.all()
    # search
    if request.method=='GET':
        search_name = request.GET.get('searchname')
        if search_name!=None:
            Employees = EmployeeModel.objects.filter(name__contains = search_name)

    # pagination
    paginator = Paginator(Employees, 5)
    page = request.GET.get('page')
    FinalEmployees = paginator.get_page(page)

    data = {
        'title': 'Home Page',
        'employees': FinalEmployees,
    }
    return render(request, 'index.html', data)


def goAdd(request):
    try:
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            form = EmployeeModel( 
                name = name,
                email = email,
                address = address,
                phone = phone
            )
            form.save()

            return redirect('/')

    except Exception as e:
        print(e)
    
    return redirect('/')


def goUpdate(request, id):
    try:
        if request.method=='POST':
            name = request.POST.get('updatename')
            email = request.POST.get('updateemail')
            address = request.POST.get('updateaddress')
            phone = request.POST.get('updatephone')

            form = EmployeeModel(
                id = id, 
                name = name,
                email = email,
                address = address,
                phone = phone
            )
            form.save()

            return redirect('/')

    except Exception as e:
        print(e)

    
    return redirect('/')

def goDelete(request, id):
    try:
        EmployeeModel.objects.get(id = id).delete()

    except Exception as e:
        print(e)

    return redirect('/')