from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetView
from django.contrib import messages

# Create your views here.
def register(request):
    r1=RegisterForm()
    if request.method=='POST':
        r1=RegisterForm(request.POST)
        if r1.is_valid():
            r1.save()
            username=r1.cleaned_data.get('username')
            password=r1.cleaned_data.get('password')
            email = r1.cleaned_data['email']
            user=authenticate(request,username=username,password=password,email=email)
            login(request, user)
            return redirect('myapp:home')
    return render(request,'register.html',{'form':r1})

@login_required
def home(request):
    return render(request,'home.html')

def loginview(request):
    l1=loginForm()
    if request.method=='POST':
        l1=loginForm(request.POST)
        if l1.is_valid():
            username=l1.cleaned_data.get('username')
            password=l1.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('myapp:home')
            else:
                error = "Invalid username or password"
                return render(request, "login.html", {"error": error})
    return render(request,'login.html',{'form1':l1})

def logoutview(request):
    logout(request)
    return redirect('myapp:home')  

@login_required
def create(request):
    c1=createForm()
    if request.method=='POST':
        c1=createForm(request.POST,request.FILES)
        if c1.is_valid():
            c1.save()
            return redirect('myapp:home')
    return render(request,'create.html',{'form2':c1})

@login_required
def retrieve(request):
    data=createModel.objects.all()
    return render(request,'retrieve.html',{'data':data})

@login_required
def update(request,id):
    obj=createModel.objects.get(id=id)
    if request.method=='POST':
        u=createForm(request.POST,request.FILES,instance=obj)
        if u.is_valid():
            u.save()
            return redirect('myapp:retrieve')
    else:
        form = createForm(instance=obj)  
    return render(request, 'update.html', {'form3': form})
           
@login_required
def delete(request,id):
    obj=createModel.objects.get(id=id)
    obj.delete()
    return redirect('myapp:retrieve')
    
def send_test_email():
    send_mail(
        "Subject here",
        "Here is the message.",
        "your-email@gmail.com",
        ["recipient@example.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully!")

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_done.txt'
    form_class=CustomPasswordResetForm  

    def form_valid(self, form):
        form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            email_template_name=self.email_template_name,
            subject_template_name=self.subject_template_name,
        )
        context = self.get_context_data(form=form)
        context['email_sent'] = True  
        return self.render_to_response(context)



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

    def form_valid(self, form):
        """
        When the form is valid, save the new password and render
        the same template with a success message.
        """
        form.save()
        context = self.get_context_data(form=form)
        context['reset_success'] = True  # Flag to indicate success
        return self.render_to_response(context)
