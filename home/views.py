from django.shortcuts import render, HttpResponse
from django.db import connection
from home.models import Customer
from home.models import Bank_statement
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from home.models import Transfer_money

import datetime
# Create your views here.


def CustomerData(request):
    customer = Customer.objects.all()
    return render(request, 'data.html', {'customers': customer})


def index(request):
    return render(request, 'index.html')


def bank(request):
    return render(request,'bank.html')


def bank_statement_details(request):
    if(request.method == "POST"):
        Name = request.POST.get('Name')
        AccountNo = request.POST.get('AccountNo')
        bank_statement_details = Bank_statement(Name=Name, AccountNo=AccountNo)
        bank_statement_details.save()
        bank = Customer.objects.filter(Name=Name, AccountNo=AccountNo)
    for b in bank:
        print(b)
    return render(request, 'bank_statement_details.html', {'bank': bank})


# Transfer the money

def transfer(request):
    if request.method == "POST":
        SenderName = request.POST.get('sendername')
        SenderAccountNo = request.POST.get('text1')
        ReceiverAccountNo = request.POST.get('text2')
        ReceiverName = request.POST.get('text5')
        Amount = int(request.POST.get('text3'))
       # Date=datetime.date.now()

        transfer = Transfer_money(SenderName=SenderName, SenderAccountNo=SenderAccountNo,
                                  ReceiverAccountNo=ReceiverAccountNo, ReceiverName=ReceiverName, Amount=Amount)
        transfer.save()
        send = Customer.objects.filter(
            Name=SenderName, AccountNo=SenderAccountNo)

        reciever = Customer.objects.filter(
            Name=ReceiverName, AccountNo=ReceiverAccountNo)
        for i in send:
            sbal = i.CurrentBalance
           
            semail = i.Email
         
            stype = i.AccountType
            
        for j in reciever: 
           rbalance=j.CurrentBalance
           remail=j.Email
           raccounttype=j.AccountType
        t=transfer.Amount
        if t>0 and t<sbal:
            sbal=sbal-t
            rbalance=rbalance+t
            send=Customer.objects.get(AccountNo=SenderAccountNo)
            send.CurrentBalance=sbal
            send.Email=semail
            send.AccountType=stype
            send.save()
            receiver=Customer.objects.get(AccountNo=ReceiverAccountNo)
            receiver.CurrentBalance=rbalance
            receiver.Email=remail
            receiver.AccountType=raccounttype
            receiver.save()
            messages.success(request,'Transaction is successful')

        else:
            messages.error(request,'Transaction fail')

    return render(request, 'Transfer.html')



def transfer_money(request):
    transfer = Transfer_money.objects.all().order_by('id').reverse()
    return render(request, 'transfer_hist.html', {'transfer': transfer})
