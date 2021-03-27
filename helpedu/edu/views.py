from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document
from .models import School

# Create your views here.
def index(request):
   
    return render(request,'edu/index.html')
    

def schools(request):
    schools = School.objects.all()
    params ={'range':range(len(schools)),'schools':schools}
    return render(request,'edu/schools.html',params)



def donate(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = DocumentForm()
    return render(request, 'edu/donate.html', {
        'form': form
    })
def content(request):
    docs = Document.objects.all()
    len_docs = len(docs)
    params = {'docs':docs,'range':range(len_docs)}
    return render(request,'edu/content.html',params)

    