from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
# Create your views here.
def index(request):
    return render(request,'fit/index.html')
def show(request):
    return render(request,'fit/show.html') 
def movie(request):
    return render(request,'fit/movie.html')              
def topics(request):
    topics=Topic.objects.order_by('date_add')  
    context={'topics':topics} 
    return render(request,'fit/topics.html',context) 
def new_topics(request):
    if request.method =='POST':   
        form=TopicForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('fit:topics')
    else:
        form=TopicForm()
    return render(request,'fit/new_topics.html',{'form':form})   
           
