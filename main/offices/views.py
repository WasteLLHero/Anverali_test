from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Order, User
from .forms import MyCustomUserForm
from django.contrib.auth import login, authenticate
class MainView(View):
    def get(self, request):
        response_dict = 'Привет'
        return render(request, "base.html", {'response': response_dict})


def registration(request):
    if request.method == 'POST':
        form = MyCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/main')
    else:
        form = MyCustomUserForm()
    return render(request, 'register.html', {'form': form})

class CreateOrderView(View):
    def get(self, request):
        pass
    

class OrderListView(View):
    def get(self, request):
        order_list = Order.objects.all()
        all_users = User.objects.all()
        print(f'Это список заказов -> {order_list}')
        print(f'Все пользователи -> {all_users[0].password}')
        return render(request, "orders_list.html", {'response': order_list})