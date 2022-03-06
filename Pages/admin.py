from django.contrib import admin
from .models import TrustWallet
from .models import MetaMask, WalletConnect
# Register your models here.
admin.site.register(TrustWallet)
admin.site.register(MetaMask)
admin.site.register(WalletConnect)
