from django.db import models

class User(models.Model):
    loanoriginalamount = models.IntegerField(blank = False)
    statedmonthlyincome = models.IntegerField(blank = False)
    term = models.IntegerField(blank = False)
    employmentstatus = models.IntegerField(blank=False, null=False)
    monthlyloanpayment = models.FloatField(null = True)
    debttoincomeratio = models.FloatField(null = True)
    isborrowerhomeowner = models.BooleanField(default=True, blank=False, null=False)
    socialmediaaccess = models.IntegerField(blank = False)
    friends = models.IntegerField(blank = False)
    postbyuser = models.IntegerField(blank = False)

