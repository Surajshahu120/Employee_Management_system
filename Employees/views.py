from django.shortcuts import render,HttpResponse
from .models import Employees_table
from datetime import datetime


def employee(request):
    return render(request, 'Employees/details.html')


def add_employee(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        dept= int(request.POST["dept"])
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        role = int(request.POST["role"])
        Phone = int(request.POST["Phone"])
        add = Employees_table(
            first_name=first_name, last_name=last_name, dept_id=dept, salary=salary,bonus=bonus, role_id=role, Phone=Phone ,hire_date=datetime.now())
        add.save()
        return HttpResponse("Data is added")
    elif request.method=='GET':
        return render(request, 'Employees/add.html')
    else: 
        return HttpResponse("Error value occured")


def view_employee(request):
    emp = Employees_table.objects.all()
    # context={
    #     "emps":emp
    # }
    # print(context)
    return render(request, 'Employees/view.html', {"emps": emp})


def remove_employee(request,remove_id=0):
    if remove_id:
        try:
            emp_to_be_removed=Employees_table.objects.get(id=remove_id)
            emp_to_be_removed.delete()
            return("Data is removed Successfuly ")
        except:
            return HttpResponse("invalid data")
    remove=Employees_table.objects.all()
    return render(request, 'Employees/remove.html',{'remove':remove})


def filter_employee(request):
    return render(request, 'Employees/filter.html')
