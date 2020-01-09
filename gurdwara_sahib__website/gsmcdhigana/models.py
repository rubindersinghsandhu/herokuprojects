from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    TYPE_CHOICES=(
        ('Spent','Spent'),
        ('Deposited','Deposited'),
    )
    heading=models.CharField(max_length=100)
    content=models.TextField()
    billimage=models.ImageField(upload_to='bill/',blank=True,default='bill/no.png')
    amount=models.IntegerField()
    type=models.CharField(max_length=10,choices=TYPE_CHOICES)
    creater=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

class expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    spent=models.DecimalField(max_digits=8,decimal_places=0,default=0)
    deposited=models.DecimalField(max_digits=8,decimal_places=0,default=0)
    def __str__(self):
        return self.user.username
    def add_expense(self,type,amount):
            if type=='Spent':
                self.spent+=amount
            else:
                self.deposited+=amount
