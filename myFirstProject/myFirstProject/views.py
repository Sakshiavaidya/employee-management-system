from django.http import HttpResponse
from django.shortcuts import render,redirect
from loginmodel.models import LoginModel
from employemodel.models import Employee

def aboutUs(request):

    return HttpResponse("Hey this is about us page")

def home(request):
    data={
        "title":"My home page",
        "name":"Hey this is Sakshi"
    }
    
    return render(request,"index.html",data)

def sum(request):
    result=0
    try:
        
        num1=int(request.GET['num1'])
        num2=int(request.GET['num2'])
        result=num1+num2
    except Exception as e:
        print(e)
        
    return render (request,"sum.html", {"sum":result})  

def cal(request):
    result=0
    try:
        
        #num1=int(request.GET['num1'])
        #num2=int(request.GET['num2'])
        #opr=request.GET['opr']
        
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        opr=request.POST['opr']
        
        if opr=="+":
            result=num1+num2
        elif opr=="-":
            result=num1-num2
        elif opr=="*":
            result=num1*num2 
        elif opr=="/":
            result=num1/num2
        elif opr=="%":
            result=num1%num2        
    except Exception as e:
        print(e)   
        
    return render (request,"cal.html", {"cal":result})    



def personal_info(request):
     
    return render(request, "personal_info.html")

def login(request):
        
    try:
            
        username=request.POST['username']
        password=request.POST['password']
        lg=LoginModel(username=username,password=password)
        lg.save()
    except:
        pass
        
        
    return render(request,'login.html')   


def emp(request):
      emp=Employee.objects.all()
      
      data={
          'emp':emp
      }
    
      return render(request,'employe.html',data)   

def addEmp(request):
    
    if request.method=='POST':
        
        try:
            
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            emp=Employee(name=name,email=email,address=address,phone=phone)
            emp.save()
        
            return redirect('/emp/')
        
        except Exception as e:
            print(e)
            
    return redirect('/emp/')

def edit(request):
    
    emp=Employee.objects
    
    data={
        'emp':emp
    }
        
    return render(request, 'employe.html',data)   

def update(request,id):
    
    if request.method=='POST':
        
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            emp=Employee(id=id,name=name,email=email,address=address,phone=phone)
            emp.save()
            return redirect('/emp/')
    
    
    return render(request, 'employe.html')   

def delete(request,id):
    
    emp=Employee.objects.filter(id=id).delete()
    
    return redirect('/emp/')