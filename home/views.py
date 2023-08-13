from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PostModel, PostCommentsModel
from django.urls import reverse_lazy
from .forms import RegForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User
    # home views
class HomeView(TemplateView):
    template_name = 'home.html'
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all().order_by("-id")
        return context
    
    # users views
class UserView(DetailView):
    model = User
    template_name = 'userview.html'
    context_object_name = 'other_user'
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all().order_by("-id")
        return context
    
class ProfilView(TemplateView):
    template_name = 'profilview.html'
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all().order_by("-id")
        return context

class PostCreateView(CreateView):
    model = PostModel
    template_name = 'createview.html'
    fields = ['image', 'summury', 'text']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
class PostUpdateView(UpdateView):
    model = PostModel
    template_name = 'editpost.html'
    fields = ['image', 'text', 'summury']
    context_object_name = 'post'

class PostDeleteView(DeleteView):
    model = PostModel
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'

def regView(request):
    errors = ''
    if request.method == "POST":
        form = RegForm(request.POST)
        # print(request.POST['last_name'])
        if form.is_valid():      
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(username,password)
            user = authenticate(request,username = username,password = password)
            print(user)
            if user:
                print("user -------------->",user)  
                login(request,user)   
                return redirect('home')
        else:
            errors = form.errors
    print(errors)
    return render(request,'sign_up.html',{'errors':errors}) 


def PostDetailView(request, pk):
    post = PostModel.objects.get(id=pk)
    comments = PostCommentsModel.objects.filter(post=post).order_by("-id")
    if request.user.is_authenticated:
        if request.method == "POST":
            text = request.POST.get('text')
            
            if text:      
                formmodel=PostCommentsModel()
                formmodel.text = text
                formmodel.post = post
                formmodel.commenter = request.user
                formmodel.save()
                return redirect(post.get_absolute_url())
    else:
        return redirect('login')
        
    return render(request,'detialview.html',{'post':post, 'comments':comments}) 