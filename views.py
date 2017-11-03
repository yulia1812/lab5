from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

def function_view(request):
    return HttpResponse('pesponse from function view')

class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')

class ExampleView(View):
    def get(self, request):
        return render(request, 'example.html', {'list':['1', '2', '3', 4, 5]})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)


class ZadanieView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'zadanie1.html', data)

class Zadanie1View(View):
    def get(self, request, id1):
        data = {
            'order': {
                'id': id1
            }
        }
        return render(request, 'el_zadanie.html', data)