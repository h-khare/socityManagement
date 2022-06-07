from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login as l
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log
from urllib3 import HTTPResponse
from societyAdmin.forms import AdminLogin, Carpenters, Electricians, Painters, Plumbers, Roofers
from societyAdmin.models import Carpenter, Electrician, Painter, Plumber, Ruffer
from user.models import User
from django.contrib.auth.models import User as kl
# Create your views here.
def adminLogin(request):
        error=False
        logout_details=False
        if request.method=="POST":
            fm=AdminLogin(request.POST)
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            print(password)
            user=authenticate(username=username,password=password)
            if user is not None:
                l(request,user)
                logout_details=True
                return HttpResponseRedirect("/profile/")
            error=True
        else:
            fm=AdminLogin()
        return render(request,'adminLogin.html',{'fm':fm,'errors':error,'logout_details':logout_details})

def AdminProfile(request):
    if request.user.is_authenticated:
            c = Carpenter.objects.filter().count()
            p=Painter.objects.filter().count()
            e=Electrician.objects.filter().count()
            pl=Plumber.objects.filter().count()
            r=Ruffer.objects.filter().count()
            k=p+pl+e+c+r
            us=User.objects.filter().count()
            # user=kl.objects.
            print(c,p)
            return render(request,"AdminProfile.html",{"c":c,"p":p,"e":e,"pl":pl,"r":r,"k":k,"us":us,"userss":request.user})
    else:
        return HttpResponseRedirect('/login/')
def AdminLogout(request):
    log(request)
    return HttpResponseRedirect("/login/")

def carpenter(request):
    if request.user.is_authenticated:
        try:
            if request.method=="POST":
                fm=Carpenters(request.POST)
                name = request.POST['name']
                email = request.POST['email']
                mobile = request.POST['mobile']
                address=request.POST['address']
                price = request.POST['price']
                usr=Carpenter(carname=name,caremail=email,carmobile=mobile,caraddress=address,carprice=price,carstatus=False,carbook=False)
                usr.save()
                return HttpResponseRedirect('/profile/')
            else:
                fm=Carpenters()
        except:
            return render(request,'carpenter.html',{"fm":fm,'register':True})
        return render(request,'carpenter.html',{"fm":fm})
    else:
        return HttpResponseRedirect('/login/')
def painter(request):
    if request.user.is_authenticated:
            try:
                if request.method=="POST":
                    fm=Painters(request.POST)
                    name = request.POST['name']
                    email = request.POST['email']
                    mobile = request.POST['mobile']
                    address=request.POST['address']
                    price = request.POST['price']
                    usr=Painter(painame=name,paiemail=email,paimobile=mobile,paiaddress=address,paiprice=price,paistatus=False,paibook=False)
                    usr.save()
                    return HttpResponseRedirect('/profile/')
                else:
                    fm=Painters()
            except:
                return render(request,'painting.html',{"fm":fm,'register':True})
            return render(request,'painting.html',{"fm":fm})
    else:
        return HttpResponseRedirect('/login/')
def roofer(request):
    if request.user.is_authenticated:
            try:
                if request.method=="POST":
                    fm=Roofers(request.POST)
                    name = request.POST['name']
                    email = request.POST['email']
                    mobile = request.POST['mobile']
                    address=request.POST['address']
                    price = request.POST['price']
                    usr=Ruffer(rufname=name,rufemail=email,rufmobile=mobile,rufaddress=address,rufprice=price,rufstatus=False,rufbook=False)
                    usr.save()
                    return HttpResponseRedirect('/profile/')
                else:
                    fm=Roofers()
            except:
                return render(request,'roofer.html',{"fm":fm,'register':True})
            return render(request,'roofer.html',{"fm":fm})
    else:
        return HttpResponseRedirect('/login/')

def plumber(request):
    if request.user.is_authenticated:
            try:
                if request.method=="POST":
                    fm=Plumbers(request.POST)
                    name = request.POST['name']
                    email = request.POST['email']
                    mobile = request.POST['mobile']
                    address=request.POST['address']
                    price = request.POST['price']
                    usr=Plumber(plname=name,plnemail=email,plnmobile=mobile,plnaddress=address,plnprice=price,plnstatus=False,plnbook=False)
                    usr.save()
                    return HttpResponseRedirect('/profile/')
                else:
                    fm=Plumbers()
            except:
                return render(request,'plumber.html',{"fm":fm,'register':True})
            return render(request,'plumber.html',{"fm":fm})
    else:
        return HttpResponseRedirect('/login/')

def electrician(request):
    if request.user.is_authenticated:
            try:
                if request.method=="POST":
                    fm=Electricians(request.POST)
                    name = request.POST['name']
                    email = request.POST['email']
                    mobile = request.POST['mobile']
                    address=request.POST['address']
                    price = request.POST['price']
                    usr=Electrician(elename=name,eleemail=email,elemobile=mobile,eleaddress=address,eleprice=price,elestatus=False,elebook=False)
                    usr.save()
                    return HttpResponseRedirect('/profile/')
                else:
                    fm=Electricians()
            except:
                return render(request,'electrician.html',{"fm":fm,'register':True})
            return render(request,'electrician.html',{"fm":fm})
    else:
        return HttpResponseRedirect('/login/')

def report(request):
    if request.user.is_authenticated:
        carpenter=Carpenter.objects.all()
        roofer=Ruffer.objects.all()
        painter=Painter.objects.all()
        electrician=Electrician.objects.all()
        plumber=Plumber.objects.all()
        return render(request,'Report.html',{"carpenter":carpenter,"painter":painter,"roofer":roofer,"electrician":electrician,"plumber":plumber})
    else:
        return HttpResponseRedirect('/login/')
def deleteData(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Plumber.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/report/')
    else:
            return HttpResponseRedirect('/login/')
def deleteRoofers(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Ruffer.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/report/')
    else:
            return HttpResponseRedirect('/login/')
def deleteDataElectrician(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Electrician.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/report/')
    else:
        return HttpResponseRedirect('/login/')
def deletePainter(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Painter.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/report/')
    else:
      return HttpResponseRedirect('/login/')
  
def deleteCarpenter(request,id):
    if request.user.is_authenticated():
        if request.method=="POST":
            pi=Carpenter.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/report/')
    else:
            return HttpResponseRedirect('/login/')
def updatePlumber(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Plumber.objects.get(pk=id)
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address=request.POST['address']
            price = request.POST['price'] 
            pi.plname=name
            pi.plnemail=email
            pi.plnmobile=mobile
            pi.plnaddress=address
            pi.plnprice=price       
            pi.save()
            return HttpResponseRedirect('/report/')
        else:    
            pi=Plumber.objects.get(pk=id)
        return render(request,'updatePlumber.html',{"fm":pi})
    else:
        return HttpResponseRedirect('/login/')
def updatePainter(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
                pi=Painter.objects.get(pk=id)
                name = request.POST['name']
                email = request.POST['email']
                mobile = request.POST['mobile']
                address=request.POST['address']
                price = request.POST['price'] 
                pi.painame=name
                pi.paiemail=email
                pi.paimobile=mobile
                pi.paiaddress=address
                pi.paiprice=price       
                pi.save()
                return HttpResponseRedirect('/report/')
        else:    
            pi=Painter.objects.get(pk=id)
        return render(request,'updatePainter.html',{"fm":pi})
    else:
        return HttpResponseRedirect('/login/')
def updateElectrician(request,id):
    if request.user.is_authenticated:
            if request.method=="POST":
                pi=Electrician.objects.get(pk=id)
                name = request.POST['name']
                email = request.POST['email']
                mobile = request.POST['mobile']
                address=request.POST['address']
                price = request.POST['price'] 
                pi.elename=name
                pi.eleemail=email
                pi.elemobile=mobile
                pi.eleaddress=address
                pi.eleprice=price       
                pi.save()
                return HttpResponseRedirect('/report/')
            else:    
                pi=Electrician.objects.get(pk=id)
            return render(request,'updateElectrician.html',{"fm":pi})
    else:
        return HttpResponseRedirect('/login/')

def updateCarpenter(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Carpenter.objects.get(pk=id)
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address=request.POST['address']
            price = request.POST['price'] 
            pi.carname=name
            pi.caremail=email
            pi.carmobile=mobile
            pi.caraddress=address
            pi.carprice=price       
            pi.save()
            return HttpResponseRedirect('/report/')
        else:    
            pi=Carpenter.objects.get(pk=id)
        return render(request,'updateCarpenter.html',{"fm":pi})
    else:
        return HttpResponseRedirect('/login/')

def updateRoofer(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Ruffer.objects.get(pk=id)
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address=request.POST['address']
            price = request.POST['price'] 
            pi.rufname=name
            pi.rufemail=email
            pi.rufmobile=mobile
            pi.rufaddress=address
            pi.rufprice=price       
            pi.save()
            return HttpResponseRedirect('/report/')
        else:    
            pi=Ruffer.objects.get(pk=id)
        return render(request,'updateRoofer.html',{"fm":pi})
    else:
        return HttpResponseRedirect('/login/')
    
def userInfo(request):
    if request.user.is_authenticated:
        users=User.objects.all()
        return render(request,'userinfo.html',{"users":users})
    else:
        return HttpResponseRedirect('/login/')