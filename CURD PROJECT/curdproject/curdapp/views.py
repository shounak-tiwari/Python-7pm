from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Enquiry
from .forms import *

# create enquiry 
def Create_enquiry(request):
    form = Enquiry_forms(request.POST)
    if request.method =="POST":
        if form.is_valid():
              form.save()
              return render(request,'index.html',{'form':Enquiry_forms()})
        else:
              form = Enquiry_forms()
    return render(request,'index.html',{'form':form})

# read enquiry 
def read(request):
    enquires =  Enquiry.objects.all()
    return render(request,'enquires.html', {'enquires': enquires})

# update enquiry
def update_enquires(request,id):
    enquires = get_object_or_404(Enquiry,id=id)
    if request.method =="POST":
        form = Enquiry_forms(request.POST,instance=enquires)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form=Enquiry_forms(instance=enquires)
    return render(request,'update_enquires.html',{'form':form , 'enquires' : enquires})

# delete enquiry
def delete_enquiry(request,id):
    enquires = get_object_or_404(Enquiry,id=id)
    if request.method =="POST":
        enquires.delete()
        return redirect('read')
    return render(request,'delete_enquiry.html',{'enquiry':enquires})

