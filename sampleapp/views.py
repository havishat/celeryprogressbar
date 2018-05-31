from __future__ import absolute_import, unicode_literals
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from celery import uuid
from celery.result import AsyncResult
from . import tasks
from .forms import UserForm
import json


def index(request):
    return render(request, 'index.html')

def poll_state(request):
    """ A view to report the progress to the user """
    data = 'Fail'
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state
        else:
            data = 'No task_id in the request'
    else:
        data = 'This is not an ajax request'

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def index2(request):
    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.get()
        context = {
            'data':data,
            'task_id':job_id,
        }
        return render(request,"show_t.html",context)
    elif 'n' in request.GET:
        n = request.GET['n']
        job = tasks.fft_random.delay(int(n))
        return HttpResponseRedirect(reverse('index2') + '?job=' + job.id)
    else:
        form = UserForm()
        context = {
            'form':form,
        }
        return render(request,"post_form.html",context)

def mycustom(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    respString = "Hello, world. Your name is " + fname + " " + lname
    return render(request, 'post.html', context={'mystring': respString})
    #return HttpResponse(respString)

def mycelerytask(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    print(fname)
    print(lname)
    task_id = uuid()
    res2 = tasks.getnames.apply_async((fname, lname), task_id=task_id)
    respString = "Your data will appear here once the celery task " \
                 + task_id + " processing is completed"
    return render(request, 'post.html',
                  context={'mystring': respString, "task_id": task_id})

"""def taskStatus(request):
    task_id = request.GET.get('taskid')
    result = AsyncResult(id=task_id)
    if not result:
        return render(request, 'post.html',
                      context={'mystring': "Id doesn't exist", "task_id": task_id},
                      status=400)
    if not result.ready():
        return render(request, 'post.html',
                      context={'mystring': "Processing", "task_id": task_id},
                      status=400)
    ans = result.get()
    result_output = "some sample"
    respString = "Hello, Celery Prcessing done, your name is " + result_output
    return render(request, 'post.html',
                  context={'mystring': respString, "task_id": task_id},
                  status=200)"""

def mytaskStatus(request):
    task_id = request.GET.get('taskid')
    print("getting ")
    print(task_id)
    result = AsyncResult(id=task_id)
    if not result:
        return render(request, 'post.html',
                      context={'mystring': "Id doesn't exist", "task_id": task_id},
                      status=400)
    if not result.ready():
        return render(request, 'post.html',
                      context={'mystring': "Processing", "task_id": task_id},
                      status=400)
    if result.status == "FAILURE":
        return render(request, 'post.html',
                      context={'mystring': "Failed", "task_id": task_id},
                      status=400)
    result_output = result.get()
    respString = "Hello, Celery Prcessing done, your name is " + result_output
    return render(request, 'post.html',
                  context={'mystring': respString, "task_id": task_id},
                  status=200)



