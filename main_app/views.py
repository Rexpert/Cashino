from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


accts = [{
    'type': 'Wallet',
    'details': [{
        'id': 1,
        'name': 'TNG',
        'date': '23 Jun 2020',
        'bal': '32.58',
    }, {
        'id': 2,
        'name': 'Cash',
        'date': '24 Jun 2020',
        'bal': '4.20',
    }, {
        'id': 3,
        'name': 'Some Wallet',
        'date': '24 Jun 2020',
        'bal': '228.88',
    }]
}, {
    'type': 'Moneybox',
    'details': [{
        'id': 4,
        'name': 'Milo Tin',
        'date': '22 Jun 2020',
        'bal': '30.50',
    }]
}, {
    'type': 'Bank',
    'details': [{
        'id': 5,
        'name': 'Bank Islam',
        'date': '18 Jun 2020',
        'bal': '16.34',
    }, {
        'id': 6,
        'name': 'Bank Rakyat',
        'date': '18 Jun 2020',
        'bal': '220.59',
    }, {
        'id': 7,
        'name': 'Bank ZZZZZZZZZZ',
        'date': '18 Jun 2020',
        'bal': '888888.88',
    }, {
        'id': 8,
        'name': 'Bank WTF',
        'date': '18 Jun 2020',
        'bal': '23232.22',
    }]
}]

receives = [{
    'l1': 'Papa',
    'l2': ['Pocket Money', 'Angpao']
}, {
    'l1': 'Mami',
    'l2': ['Family Food', 'Housewares', 'Pocket Money']
}, {
    'l1': 'Hooi Koon',
    'l2': ['Pay Back', 'Family Food']
}]

pays = [{
    'l1': 'Food',
    'l2': ['Family Food', 'Breakfast', 'Treats', 'Snacks', 'Lunch', 'Dinner']
}, {
    'l1': 'Housewares',
    'l2': ['Light Bulb', 'Kettle']
}, {
    'l1': 'Transport',
    'l2': ['TNG', 'Bus', 'Parking', 'Petrol']
}, {
    'l1': 'Fees',
    'l2': ['Bank Charge', 'Saman']
}]


def home(request):
    if request.method == 'POST':
        print('acct id: ', request.POST.get('id'))
        print('amount: ', float(request.POST.get('atm_new_bal')) -
              float(request.POST.get('bal')))
    context = {
        'accts': accts,
    }
    return render(request, 'main_app/home.html', context)


def transaction(request):
    context = {
        'accts': accts,
        'receives': receives,
        'pays': pays,
    }
    return render(request, 'main_app/transaction.html', context)
