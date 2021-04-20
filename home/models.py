from django.db import models
from django.db import connection

# Create your models here.

class Customer(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    AccountNo = models.CharField(max_length=7,null=True,blank=True)
    Email = models.CharField(max_length=122,null=True,blank=True)
    AccountType = models.CharField(max_length=122,null=True,blank=True)
    CurrentBalance = models.IntegerField(null=True,blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.AccountNo
        
class Bank_statement(models.Model):
    Name=models.CharField(max_length=1222,null=True,blank=True)
    AccountNo=models.CharField(max_length=122,null=True,blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.Name



class Transfer_money(models.Model):
    
    SenderName = models.CharField(max_length=122,null=True,blank=True)
    SenderAccountNo = models.CharField(max_length=7,null=True,blank=True)
    ReceiverName = models.CharField(max_length=122,null=True,blank=True)
    ReceiverAccountNo = models.CharField(max_length=7,null=True,blank=True)
    Amount = models.IntegerField(null=True,blank=True)
    Date = models.DateTimeField(null=True,blank=True)
   
    objects = models.Manager()

    def __str__(self):
        return self.SenderName
