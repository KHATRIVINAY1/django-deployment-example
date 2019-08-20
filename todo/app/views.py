from .models import Task
from django.views.generic import (CreateView,UpdateView,DeleteView,ListView,DetailView)
from django.contrib.auth.models import User
from .forms import NewUser
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'app/detail.html'

class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'obj'
    template_name = 'app/delete.html'
    success_url = reverse_lazy('app:home')

class TaskEdit(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'app/create.html'
    fields = ['label', 'description']

class Home(ListView):
    model = Task
    template_name = 'app/home.html'

    def get_queryset(self):
        return Task.objects.filter(user__username=self.request.user)

@login_required()
def deleteso(request):
    obj = Task.objects.filter(user__username=request.user)
    obj.delete()
    return HttpResponseRedirect(reverse('app:home'))
