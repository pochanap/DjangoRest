from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def employeeView(request):
    emp = {
        'id': 226,
        'name': 'Hrithi',
        'sal': 2302000
    }
    return JsonResponse(emp)
