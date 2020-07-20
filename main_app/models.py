from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Acct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    bal = models.DecimalField(max_digits=8, decimal_places=2)
    acct_type = models.CharField(max_length=15)
    acct_name = models.CharField(max_length=15)


class Receive(models.Model):
    history = models.ForeignKey("History", on_delete=models.DO_NOTHING)
    from_who = models.CharField(max_length=15)
    for_what = models.CharField(max_length=15)


class Transfer(models.Model):
    history_to = models.ForeignKey(
        "History", on_delete=models.DO_NOTHING, related_name="transfer_to")
    history_from = models.ForeignKey(
        "History", on_delete=models.DO_NOTHING, related_name="transfer_from")


class Pay(models.Model):
    history = models.ForeignKey("History", on_delete=models.DO_NOTHING)
    primary = models.CharField(max_length=15)
    secondary = models.CharField(max_length=15)


class Calibrate(models.Model):
    history = models.ForeignKey("History", on_delete=models.DO_NOTHING)


class History(models.Model):

    class Action(models.IntegerChoices):
        OPEN = 1
        RECEIVE = 2
        TRANSFER = 3
        PAY = 4
        CALIBRATE = 5
        CLOSE = 6

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acct = models.ForeignKey(
        "Acct", on_delete=models.CASCADE)
    action = models.IntegerField(choices=Action.choices)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bal = models.DecimalField(max_digits=8, decimal_places=2)
    last_modify = models.DateTimeField(default=timezone.now)
