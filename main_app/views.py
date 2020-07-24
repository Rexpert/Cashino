from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


accts = [{
    'type': 'Wallet',
    'details': [{
        'name': 'TNG',
        'date': '23 Jun 2020',
        'bal': '32.58',
    }, {
        'name': 'Cash',
        'date': '24 Jun 2020',
        'bal': '4.20',
    }, {
        'name': 'Some Wallet',
        'date': '24 Jun 2020',
        'bal': '228.88',
    }]
}, {
    'type': 'Moneybox',
    'details': [{
        'name': 'Milo Tin',
        'date': '22 Jun 2020',
        'bal': '30.50',
    }]
}, {
    'type': 'Bank',
    'details': [{
        'name': 'Bank Islam',
        'date': '18 Jun 2020',
        'bal': '16.34',
    }, {
        'name': 'Bank Rakyat',
        'date': '18 Jun 2020',
        'bal': '220.59',
    }, {
        'name': 'Bank ZZZZZZZZZZ',
        'date': '18 Jun 2020',
        'bal': '888888.88',
    }, {
        'name': 'Bank WTF',
        'date': '18 Jun 2020',
        'bal': '23232.22',
    }]
}]


def home(request):
    context = {
        'accts': accts
    }
    return render(request, 'main_app/home.html', context)


def transaction(request):
    return HttpResponse('Transaction')
