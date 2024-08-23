from django.shortcuts import render

# Create your views here.

from .forms import RegistrationForm

def home(request):
    # form =Registration()
    form =RegistrationForm()
    # return render(request,"home.html",{"form":form})
    if request.method=="POST":
        form=RegistrationForm(request.POST)

        if form.is_valid():
            fname=form.cleaned_data["fname"]
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(fname,lname,email,contact)
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
            # RegistrationForm.object.create()
            form.save()

    return render(request,"home.html",{"form":form})        

