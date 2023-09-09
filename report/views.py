from django.shortcuts import render
from django.http import HttpResponse
from .models import AddRecord
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin')
def home(request):
    all_records = AddRecord.objects.all()
    context = {'all_records': all_records}
    return render(request, 'index.html', context)

def single_record(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'online_record.html', context)

def print_record(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'print_record.html', context)

def generat_image(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'generat_img.html', context)

