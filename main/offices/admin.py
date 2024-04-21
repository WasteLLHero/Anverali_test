from django.contrib import admin
from .models import  Order, User, OrderToAuthor, OrderToEcutor

admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderToAuthor)
admin.site.register(OrderToEcutor)

