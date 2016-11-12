# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .forms import TypeForm
from .models import BillType, Bill
# Create your views here.


def index(request):
    bills = Bill.objects.all()
    return render(request, 'list.html',{'bills':bills})


def form(request,bill_id):
    content = {}
    bill_types = BillType.objects.all()
    content['bill_types'] = bill_types
    if bill_id != '' and int(bill_id) > 0:
        bill = Bill.objects.get(pk=bill_id)
        content['bill'] = bill

    return render(request, 'form.html', content)


def add(request):
    bill_id = request.POST['id'].strip()
    type_id = request.POST['type_id'].strip()
    name = request.POST['name'].strip()
    price = request.POST['price'].strip()
    bill_date = request.POST['date'].strip()
    description = request.POST['description'].strip()
    if bill_id != '' and int(bill_id) > 0 and type_id != '' and int(type_id) > 0:  # edit
        bill = Bill.objects.get(pk=int(bill_id))
        bill.name = name
        bill.price = float(price)
        bill.bill_date = bill_date
        bill.description = description
        bill.bill_type = BillType.objects.get(pk=int(type_id))
        bill.save()
        return HttpResponse("{'status':1}")

    elif type_id != '' and name != '' and price != '' and int(type_id) > 0 and float(price) > 0:
        bill = Bill()
        bill.name = name
        bill.price = float(price)
        bill.bill_date = bill_date
        bill.description = description
        bill.bill_type = BillType.objects.get(pk=int(type_id))
        bill.save()
        return HttpResponse("{'status':1}")
    else:
        return HttpResponse("{'status':0}")

def list_type(request):
    types = BillType.objects.all()
    return render(request, 'list_type.html',{'types':types})

def form_type(request, type_id):
    content = {}
    if type_id != '' and int(type_id) > 0:
        bill_type = BillType.objects.get(pk=type_id)
        content['bill_type'] = bill_type
    return render(request, 'form_type.html', content)


def add_type(request):
    type_id = request.POST['id'].strip()
    name = request.POST['name'].strip()
    status = request.POST['status'].strip()

    if type_id != '' and int(type_id) > 0:  # edit
        bill_type = BillType.objects.get(pk=int(type_id))
        bill_type.name = name
        bill_type.status = status
        bill_type.save()
        return HttpResponse("{'status':1}")

    elif name != '' and status != '':  # add
        bill_type = BillType()
        bill_type.name = name
        bill_type.status = status
        bill_type.save()
        return HttpResponse("{'status':1}")
    else:
        return HttpResponse("{'status':0}")
