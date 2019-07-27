from django.shortcuts import render,redirect
from django import forms
from .iupscnaming import callbridge
import threading,multiprocessing
class form1(forms.Form):
    iupsc = forms.CharField(max_length=250,label="IUPSC",help_text='Enter IUPSC Name')


def thread(strval):
    try :
        process = multiprocessing.Process(target=callbridge, args=(str(strval),))
        process.start()
        process.join()
    except Exception as p:
        process.terminate()
        return
        



def index(request):
     if request.method == 'POST':
        formobj = form1(request.POST)

        if formobj.is_valid():
            strval =formobj.cleaned_data['iupsc']
            print(formobj.cleaned_data['iupsc'])
            thread(strval)
            return redirect('start') 
        else:
            formobj = form1()
            return render(request,'one.html',{'form':formobj})
     else:
         formobj = form1()
         return render(request,'one.html',{'form':formobj})