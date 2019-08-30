from .models import Task
from django.views.generic import (CreateView,UpdateView,DeleteView,ListView,DetailView)
from django.contrib.auth.models import User
from .forms import NewUser,UpdateUser,Profile_form
from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'app/create.html'
    fields = ['label','description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)

class CreateUser(CreateView):
    model = User
    form_class = NewUser
    template_name = 'app/register.html'
    success_url = reverse_lazy('app:login')

class TaskDetail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Task
    template_name = 'app/detail.html'

    def test_func(self):
        task =self.get_object()
        if self.request.user==task.user:
            return True
        return False

class DeleteTask(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    context_object_name = 'obj'
    template_name = 'app/delete.html'
    success_url = reverse_lazy('app:home')

    def test_func(self):
        task =self.get_object()
        if self.request.user==task.user:
            return True
        return False

class TaskEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Task
    template_name = 'app/create.html'
    fields = ['label', 'description']

    def test_func(self):
        task =self.get_object()
        if self.request.user==task.user:
            return True
        return False

class Home(ListView):
    model = Task
    template_name = 'app/home.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(user__username=self.request.user).order_by('-create_date')

@login_required()
def deleteso(request):
    obj = Task.objects.filter(user__username=request.user)
    obj.delete()
    return HttpResponseRedirect(reverse('app:home'))

@login_required()
def showprofile(request):
    
    if request.method=='POST':
        u_form= UpdateUser(request.POST,instance=request.user)
        p_form =Profile_form(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('app:show')
        
    else:
        u_form= UpdateUser(instance=request.user)
        p_form=Profile_form(instance=request.user.profile)
        
    return render(request,'app/profile_page.html',{'u_form':u_form,'p_form':p_form})
