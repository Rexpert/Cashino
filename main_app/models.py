from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Acct_type(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15)


class Acct(models.Model):
    acct_type = models.ForeignKey("Acct_type", on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)


class Receive(models.Model):
    history = models.ForeignKey("History", on_delete=models.CASCADE)
    l2_suggestion = models.ForeignKey(
        "L2_suggestion", on_delete=models.DO_NOTHING)


class Transfer(models.Model):
    history = models.ForeignKey("History", on_delete=models.CASCADE)
    acct = models.ForeignKey("Acct", on_delete=models.CASCADE)


class Pay(models.Model):
    history = models.ForeignKey("History", on_delete=models.DO_NOTHING)
    l2_suggestion = models.ForeignKey(
        "L2_suggestion", on_delete=models.DO_NOTHING)


class History(models.Model):

    class Action(models.IntegerChoices):
        OPEN = 1
        RECEIVE = 2
        TRANSFER = 3
        PAY = 4
        CALIBRATE = 5
        CLOSE = 6

    acct = models.ForeignKey("Acct", on_delete=models.CASCADE)
    action = models.IntegerField(choices=Action.choices)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    last_modify = models.DateTimeField(default=timezone.now)


class L2_suggestion(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    l1_suggestion = models.ForeignKey(
        "L1_suggestion", on_delete=models.CASCADE)


class L1_suggestion(models.Model):
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)
