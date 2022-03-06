from django.db import models
from datetime import datetime


# Create your models here.
class TrustWallet(models.Model):
    link = models.CharField(max_length=200)
    date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.link

class MetaMask(models.Model):
    link = models.CharField(max_length=200)
    date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.link

class WalletConnect(models.Model):
    link = models.CharField(max_length=200)
    date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.link
