from django.db import models
from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers.UserManager import UsersManager as UserManager
from django.contrib.auth.models import AbstractUser
answers = [
        (True, 'Да'),
        (False, 'Нет')
    ]

    
role_list = (
    (True, 'Клиент'),
    (False, 'Исполнитель')
)
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30,null=True, blank=True)
    
    first_name = models.CharField( max_length=30,null=True, blank=True)
    sur_name = models.CharField( max_length=30,null=True, blank=True)
    last_name = models.CharField( max_length=30,null=True, blank=True)
    
    phone_number = RegexValidator(regex=r'^\+?7?\d{9,15}$', 
                                  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    email = models.EmailField(unique=True)
    
    date_joined = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField( default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    role = models.BooleanField(choices=role_list, default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']
    
class OrderToAuthor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user_id}'
    
class OrderToEcutor(models.Model):
    executor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.executor_id}'
       
class Order(models.Model):
    text = models.TextField()
    is_active = models.BooleanField(choices=answers, default=True)
    author_id = models.ForeignKey(OrderToAuthor, on_delete=models.CASCADE)
    executor_id = models.ForeignKey(OrderToEcutor, blank=True, null=True,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.text}'