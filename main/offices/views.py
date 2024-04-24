from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Order, OrderToAuthor, OrderToEcutor, User
from .forms import MyCustomUserForm
from django.contrib.auth import login, authenticate

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

class OrderListView(View):
    def get(self, request):
        order_list = Order.objects.filter(executor_id=None)
        if (not request.user.is_anonymous):
            if (request.user.role):
                return render(request, "orders_list.html", {'response': order_list})
            elif(not request.user.role):
                return render(request, "orders_list.html", {'response': order_list})
        else: 
            return render(request, "orders_list.html", {'response': order_list})
        
    def post(self, request):
        order_list = Order.objects.filter(executor_id=None)
        choice_order_to_complete = request.POST.get('chosen_order')
        choisen_order = Order.objects.filter(id=choice_order_to_complete)
        choisen_order.update(executor_id = OrderToEcutor.objects.create(executor_id = request.user))
        return render(request, "orders_list.html", {'response': order_list})
    
class CreateOrderView(View):
    def get(self, request):
        return render(request, "create_order.html", {'response': 1})
    def post(self, request):
        new_text_from_form = request.POST.get('order_name', None)
        if(new_text_from_form != None):
            new_order_keys = OrderToAuthor.objects.create(user_id = request.user )
            new_order = Order.objects.create(text = new_text_from_form, author_id = new_order_keys)
            new_order_keys.save()
            new_order.save()
        return render(request, "create_order.html", {'response': new_text_from_form})
        
class OrderPersonalListView(View):
    def get(self, request):
        order_list = Order.objects.filter(author_id__user_id = request.user.id)
        return render(request, "personalOrders.html", {'response': order_list})
    
class ExecutorOrderListView(View):
    def get (self, request):
        order_list = Order.objects.filter(executor_id__executor_id = request.user.id)
        return render(request, "personalOrders.html", {'response': order_list})