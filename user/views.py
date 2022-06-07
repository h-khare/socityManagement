from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from societyAdmin.models import Carpenter, Electrician, Painter, Plumber, Ruffer
from user.forms import UserLogin, UserRegistration
from django.contrib.auth import login as l
from user.models import User

# Create your views here.
def userLogin(request):
    try:
        error=False
        if request.method=="POST":
            fm=UserLogin(request.POST)
            username = request.POST['email']
            print(username)
            password = request.POST['password']
            print(password)
            error=True
            print(error)
            user=User.objects.filter(email=username,password=password)
            print(user)
            k=user[0]
            request.session['user1']=k.email
            if k is not None:
                return HttpResponseRedirect('/user_profile/')
            
          
        else:
            fm=UserLogin()
        return render(request,'userLogin.html',{"fm":fm,"errors":error})
    except:
        pass
    return render(request,'userLogin.html',{"fm":fm,"errors":error})
def registration(request):
    try:
        error=False
        if request.method=="POST":
            fm=UserRegistration(request.POST)
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address=request.POST['address']
            password = request.POST['password']
            usr=User(name=name,email=email,mobile=mobile,address=address,password=password)
            usr.save()
            return HttpResponseRedirect('/user_login/')
        else:
            fm=UserRegistration()
    except:
        error=True
        return render(request,'registration.html',{"fm":fm,'register':True,"errors":error})
    return render(request,'registration.html',{"fm":fm,"errors":error  })

def userProfile(request):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        c = Carpenter.objects.filter().count()
        p=Painter.objects.filter().count()
        e=Electrician.objects.filter().count()
        pl=Plumber.objects.filter().count()
        r=Ruffer.objects.filter().count()
        l=p+pl+e+c+r
        return render(request,'UserProfile.html',{"usercontent":k,"c":c,"p":p,"e":e,"pl":pl,"r":r,"l":l})
    except:
        pass
    return HttpResponseRedirect('/user_login/')
    
def PlumberDetails(request):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        
        plumber=Plumber.objects.all()
        a=True
        if k.plumberDetails !="":
          a=False  
        return render(request,'PlumberDetail.html',{"usercontent":k,"plumber":plumber,"a":a})
    except:
        pass
    return HttpResponseRedirect('/user_login/')
    
def ElectricianDetails(request):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        electrician=Electrician.objects.all()
        a=True
        if k.electricianDetails !="":
          a=False  
        return render(request,'ElectricianDetail.html',{"usercontent":k,"electrician":electrician,"a":a})
    except:
        pass
    return HttpResponseRedirect('/user_login/')
def CarpenterDetails(request):
    try:
        email=request.session['user1']
        print(email,"Harsh")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        carpenter=Carpenter.objects.all()
        a=True
        if k.carpentersDetails !="":
          a=False  
        return render(request,'CarpenterDetail.html',{"usercontent":k,"carpenter":carpenter,"a":a})
    except:
        pass
    return HttpResponseRedirect('/user_login/')
def PainterDetails(request):

        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        painter=Painter.objects.all()
        a=True
        if k.painterDetails !="":
          a=False  
        return render(request,'PainterDetail.html',{"usercontent":k,"painter":painter,"a":a})

def RooferDetails(request):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        print(email)
        user=User.objects.filter(email=email)
        k=user[0]
        roofer=Ruffer.objects.all()
        a=True
        if k.rooferDetails !="":
          a=False  
        return render(request,'RooferDetail.html',{"usercontent":k,"roofer":roofer,"a":a})
    except:
        pass
    return HttpResponseRedirect('/user_login/')

def userLogout(request):
    try:
        del request.session['user1']
    except KeyError:
        pass
    return HttpResponseRedirect('/user_login/')

def bookPlumber(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Plumber.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.plnusers=email
        plu.plnbook=True
        user.serviceDetails=plu.plntype
        user.plumberDetails=plu.id
        user.save()
        plu.save()
        print(plu.plnstatus)
        return HttpResponseRedirect('/plumber_details/')
    except:
        pass
    return HttpResponseRedirect('/user_login/')

def bookCarpenter(request,id):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Carpenter.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.carusers=email
        plu.carbook=True
        user.serviceDetails=plu.cartype
        user.carpentersDetails=plu.id
        user.save()
        plu.save()
        return HttpResponseRedirect('/carpenter_details/')
    except:
        pass
    return HttpResponseRedirect('/user_login/')

def bookPainter(request,id):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Painter.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.paiusers=email
        plu.paibook=True
        user.serviceDetails=plu.paitype
        user.painterDetails=plu.id
        user.save()
        plu.save()
        return HttpResponseRedirect('/painter_details/')
    except:
        pass
    return HttpResponseRedirect('/user_login/')
def bookRoffer(request,id):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Ruffer.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.rufusers=email
        plu.rufbook=True
        user.serviceDetails=plu.ruftype
        user.rooferDetails=plu.id
        user.save()
        plu.save()
        return HttpResponseRedirect('/roofer_details/')
    except:
        pass
    return HttpResponseRedirect('/user_login/')

def bookElectrician(request,id):
    try:
        email=request.session['user1']
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Electrician.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.eleusers=email
        plu.elebook=True
        user.serviceDetails=plu.eletype
        user.electricianDetails=plu.id
        user.save()
        plu.save()
        return HttpResponseRedirect('/electrician_details/')
    except:
        pass
    return HttpResponseRedirect('/user_login/')

def delPlBooking(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Plumber.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.plnusers=""
        plu.plnbook=False
        user.serviceDetails=""
        user.plumberDetails=""
        user.save()
        plu.save()
        print(plu.plnstatus)
        return HttpResponseRedirect('/plumber_details/')
    except:
        pass
    return HttpResponseRedirect("/user_login/")

def delPiBooking(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Painter.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.paiusers=""
        plu.paibook=False
        user.serviceDetails=""
        user.painterDetails=""
        user.save()
        plu.save()
        return HttpResponseRedirect('/painter_details/')
    except:
        pass
    return HttpResponseRedirect("/user_login/")

def delElBooking(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Electrician.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.eleusers=""
        plu.elebook=False
        user.serviceDetails=""
        user.electricianDetails=""
        user.save()
        plu.save()
        return HttpResponseRedirect('/electrician_details/')
    except:
        pass
    return HttpResponseRedirect("/user_login/")

def delCaBooking(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Carpenter.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.carusers=""
        plu.carbook=False
        user.serviceDetails=""
        user.carpentersDetails=""
        user.save()
        plu.save()
        return HttpResponseRedirect('/carpenter_details/')
    except:
        pass
    return HttpResponseRedirect("/user_login/")
def delRuBooking(request,id):
    try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        plu=Ruffer.objects.get(pk=id)
        user=User.objects.get(email=email)
        plu.rufusers=""
        plu.rufbook=False
        user.serviceDetails=""
        user.rooferDetails=""
        user.save()
        plu.save()
        return HttpResponseRedirect('/roofer_details/')
    except:
        pass
    return HttpResponseRedirect("/user_login/")

def service(request):
    # try:
        email=request.session['user1']
        print(email,"book")
        user=User.objects.filter(email=email)
        k=user[0]
        if email==None:
            return HttpResponseRedirect('/user_login/')
        paint=""
        roofer=""
        carpr=""
        elect=""
        count=0
        plumbs=""
        if k.electricianDetails!="":
            count=count+1
            elect=Electrician.objects.get(pk=k.electricianDetails)
        if k.rooferDetails!="":
            count=count+1
            roofer=Ruffer.objects.get(pk=k.rooferDetails)
        if k.carpentersDetails!="":
            count=count+1
            carpr=Carpenter.objects.get(pk=k.carpentersDetails)
        if k.painterDetails!="":
            count=count+1
            paint=Painter.objects.get(pk=k.painterDetails)
        if k.plumberDetails!="":
            count=count+1
            plumbs=Plumber.objects.get(pk=k.plumberDetails)


        return render(request,'services.html',{'count':count,"usercontent":k,'painter_details':paint,'plumber_detail':plumbs,'electirican_detail':elect,'roffer_detail':roofer,'carpenter_details':carpr})
    # except:
    #     pass
    # return HttpResponseRedirect('/user_login/')
    
    
def myUser(request):
    # try:
        email=request.session['user1']
        print(email,"book")
        if email==None:
            return HttpResponseRedirect('/user_login/')
        # plu=Ruffer.objects.get(pk=id)
        user=User.objects.get(email=email)
        return render(request,'MyUser.html',{"user":user})
    # except:
    #     pass
    # return HttpResponseRedirect("/user_login/")

