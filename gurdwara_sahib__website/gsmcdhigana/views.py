from django.shortcuts import render , redirect
from .forms import postForm,userloginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .models import post,expense

# Create your views here.

def userlogin(request):
    form = userloginform(request.POST or None)
    if form.is_valid():
        data=request.POST.dict()
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    context = {
        'form': form,
    }
    return render(request, "html/login.html", context)

def homepage(request):
    if post.objects.exists():
        posts=post.objects.order_by('-date_posted')
        tamount,tspent,tdeposit=0,0,0
        for apost in posts:
            expenseobj=expense.objects.filter(user=apost.creater).first()
            tspent=tspent+expenseobj.spent
            tdeposit=tdeposit+expenseobj.deposited
        tamount=tdeposit-tspent
        useractive=request.user.is_authenticated
        print(useractive)
        data={
            'posts':posts,
            'ustatus':useractive,
            'amount':tamount,
            'spent':tspent,
            'deposit':tdeposit,
        }
        return render(request,'html/homepage.html',data)
    else:
        return redirect('postdata')

def postdata(request):
    if request.user.is_authenticated:
        form=postForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.creater=request.user
            instance.save()
            dummy=expense.objects.filter(user=instance.creater)
            if dummy:
                dummy=dummy.first()
                dummy.add_expense(instance.type,instance.amount)
                dummy.save()
            else:
                dummy=expense(user=instance.creater,spent=0,deposited=0)
                dummy.add_expense( instance.type, instance.amount)
                dummy.save()
        else:
            print("form not valid")
        data = {
            'form': form,
            'request':request,
        }
        return render(request,'html/postform.html',data)
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('home')

def imageview(request,id):
    img=post.objects.filter(id=id).first()
    data={
        'post':img,
        'id':id,
    }
    return render(request,'html/bill.html',data)



