from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Pages/index.html')
def wallets(request):
    return render(request,'Pages/wallet.html')