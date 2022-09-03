from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Todo_form
from .models import Todo_list

def home(request):
  if request.method=='POST':
      fm=Todo_form(request.POST)
      if fm.is_valid():
         fm.save()
         fm=Todo_form()
         data = Todo_list.objects.all()
  else:
   fm=Todo_form()
   data = Todo_list.objects.all()
  return render(request,'index.html',{'fm':fm,'data':data})

def delete(request,id):
    if request.method=='POST':
     dele=Todo_list.objects.get(pk=id)
     dele.delete()
    return redirect('/')
def update(request,pk):
    if request.method=='POST':
      dele = Todo_list.objects.get(id=pk)
      form=Todo_form(request.POST,instance=dele)
      if form.is_valid():
         form.save()
         return redirect('/')

    else:
        dele =Todo_list.objects.get(id=pk)
        form =Todo_form(request.POST, instance=dele)
    return render(request,'update.html',{'form':form})





