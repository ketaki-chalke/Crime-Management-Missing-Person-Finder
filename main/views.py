from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from main.models import MissingCase
from .models import CrimeReport
from .models import ContactSubmission
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
  return render(request,"main/home.html")

#def adminSignup(request):
 # return render(request,"main/signupA.html")
def my(request):
  return render(request,"main/my.html")

def uPd(request):
   return render(request,"main/updatess.html")



def faq(request):
  return render(request,"main/faq.html")
def faq2(request):
  return render(request,"main/faq2.html")

def cr2(request):
  return render(request,"main/cr2.html")
def cr1(request):
  return render(request,"main/cr2.html")

def contact(request):
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        p=ContactSubmission(full_name=full_name, email=email,message=message)
        p.save()
        return HttpResponse("Data saved")
    else:
       return render(request,"main/contact.html")

def publicsignup(request):
  if request.method=='POST':
    pname=request.POST.get('adminName')
    email=request.POST.get('email')
    pass1=request.POST.get('password')
    pass2=request.POST.get('cpassword')

    if pass1!=pass2:
      return HttpResponse("Your password and Confirm password are not same!!!")
    else:
     my_user=User.objects.create_user(pname,email,pass1)
     my_user.save()
     return redirect('signinG')
  return render(request,"main/signupG.html")


def signinG(request):
  if request.method=='POST':
    username=request.POST.get('username')
    pass1=request.POST.get('password')
    user=authenticate(request,username=username,password=pass1)
    if user is not None:
      login(request,user)
      return redirect('case')
    else:
      return HttpResponse("Username or Password is Incorrect!!!")
  return render(request,"main/signinG.html")

def LogoutPage(request):
  logout(request)
  return redirect('signupG')
      

def case(request):
    if request.method=="POST":
       
       name = request.POST['name']
       age = request.POST['age']
       description = request.POST['description']
       identificationMark = request.POST['identificationMark']
       height = request.POST['height']
       weight = request.POST['weight']
       gender = request.POST['gender']
       number = request.POST['number']
       image = request.POST.get('image')
       if 'image' in request.FILES:
            image = request.FILES['image']
          
       

       #print(name,age,description,identificationMark,height,weight,gender,number,image)
       ins = MissingCase(name=name,age=age,description=description,identificationMark=identificationMark,height=height,weight=weight,gender=gender,number=number,image=image)
       ins.save()
       print("database created successfully")
    return render(request, "main/case.html")

def feat(request):
  return render(request,"main/features.html")


 

def missing(request):
  all_persons = MissingCase.objects.all
  return render(request,"main/missing.html",{'all':all_persons})


def report(request):
  if request.method=='POST':
     case_id = request.POST.get("case_id")
     crime_no = request.POST.get("crime_no")
     crime_type = request.POST.get("crime_type")
     crime_name = request.POST.get("crime_name")
     age = request.POST.get("age")
     nickname = request.POST.get("nickname")
     adate = request.POST.get("adate")
     dateoc = request.POST.get("dateoc")
     gender = request.POST.get("gender")
     address = request.POST.get("address")
     birthmark = request.POST.get("birthmark")
     wanted = request.POST.get("wanted") 
     pending = request.POST.get("pending")

     criminal_info = CrimeReport(
            case_id=case_id,
            crime_no=crime_no,
            crime_type=crime_type,
            crime_name=crime_name,
            age=age,
            nickname=nickname,
            adate=adate,
            dateoc=dateoc,
            gender=gender,
            address=address,
            birthmark=birthmark,
            wanted=wanted,
            pending=pending
        )
     criminal_info.save()

    
  return render(request,"main/report.html")
  
  


def edit(request):
  std=CrimeReport.objects.all()
  return render(request,"main/edit.html",{"std":std})

def delete_std(request, case_id):
    if request.method == 'POST':
        try:
            print(case_id)
            pi = CrimeReport.objects.get(pk=case_id)
            print(pi)
            pi.delete()
            return HttpResponseRedirect(reverse('edit', args=[case_id]))  # Redirect to the edit page after deletion
        except ObjectDoesNotExist:
            # Handle the case where the User object does not exist
            pass
        return HttpResponseRedirect(reverse('edit'))  

def update_crime_report(request, case_id):
    crime_report = get_object_or_404(CrimeReport, pk=case_id)
    if request.method == 'POST':
        # Handle form submission and update crime report
        # Assuming you have a CrimeReportForm defined
        form = CrimeReport(request.POST, instance=crime_report)
        if form.is_valid():
            form.save()
            return redirect('edit.html')  # Redirect to the crime report list page
    else:
        form = CrimeReport(instance=crime_report)
    return render(request, 'updatess.html', {'form': form})

def recog(request):
  return render(request,"main/face-recog.html") 



def adminLogin(request):
  if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('features')  # Redirect to dashboard or any other page after successful login
        else:
            return HttpResponse("Username or Password is Incorrect!!!")
  return render(request, "main/loginA.html")

def user_logout(request):
    logout(request)
    return redirect('home')



####################################################################################

