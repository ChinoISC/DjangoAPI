from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL


# Create your views here.
@login_required(login_url=LOGING_URL)
def task_views(request):
    template_name = "register_task.html"
    
    return render(request,template_name)