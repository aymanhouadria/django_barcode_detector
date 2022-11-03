from django.http import HttpResponse
from django.shortcuts import render
import sys
import os
import subprocess as sp

extProc = None

def index(request):
    try:
        request.POST['stop']
        sp.Popen.terminate(extProc)
    except:
        pass
    return render(request, 'detecction_settings.html')


def running(request):
    global extProc
    h="d"
    try:
        if request.POST['barcode'] and request.POST['OCR']:

            extProc = sp.Popen(['python', 'djangoCodebarApp\\scanner.py'])
    except:
        try:
            if request.POST['barcode']:

                extProc = sp.Popen(['python', 'djangoCodebarApp\\scanner.py','barcode'])
        except:
            try:
                if request.POST['OCR']:
                    extProc = sp.Popen(['python', 'djangoCodebarApp\\scanner.py','OCR'])
            except:
                extProc = sp.Popen(['python', 'djangoCodebarApp\\scanner.py'])


    return render(request, 'running.html')

# Create your views here.
