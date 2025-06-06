from django.shortcuts import render, HttpResponse
from.models import TodoItem
from django.contrib.auth.decorators import login_required
from .forms import taskform

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request,"todos.html",{"todos":items} )

def create_task(request):
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('todos')
    else:
        form = taskform()
    return render(request, "createtask.html", {'form':form})        