from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import sys
import csv
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage
from numpy.core.fromnumeric import mean
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse, HttpResponseRedirect
from urllib.request import urlopen
import json
from numpy import isnan


def report(request):
    if request.method == 'POST':
        inp2 = request.POST.get("param2")
        reporte = run([sys.executable, 'pdf_report.py'], shell =False, stdout= PIPE)
        print(reporte)
        data=[]
        with open("inferencia.csv") as file:
            reader=csv.reader(file,delimiter=";")
            for row in reader:
                data.append(row)
        threshold=[]
        [threshold.append(float(data[l][2])) for l in range(1,len(data))]
        number_of_roses=len(data)-1
        mean_accuracy=round(mean(threshold),2)

        return render(request,'pdf.html', {'accuracy':mean_accuracy, 'roses':number_of_roses})
    else:
        return redirect('/')


def resultados(): 
    data=[]
    with open("inferencia.csv") as file:
        reader=csv.reader(file,delimiter=";")
        for row in reader:
            data.append(row)
    threshold=[]
    [threshold.append(float(data[l][2])) for l in range(1,len(data))]
    number_of_roses=len(data)-1
    mean_accuracy=mean(threshold)
    return data

def image_upload(request):  
    if request.method == 'POST':
        try:
            image= request.FILES['image']
        except:
            image_path=request.POST['src']
            image = NamedTemporaryFile()
            image.write(urlopen(image_path).read())
            image.flush()
            image = File(image)
            name = 'camera_img'
            name += '.png'  # store image in png format
            image.name = name
        finally:
            fs = FileSystemStorage()
            filename= fs.save(image.name,image)
            fileurl=fs.open(filename)
            templateurl = fs.url(filename)
            nameofInput=templateurl.split("/")[:-1]
            nameofInput = '/'.join(nameofInput)+"/"+"img.png"
            image = run([sys.executable,'Inference.py',str(filename)],shell=False,stdout=PIPE)
            data=[]
            with open("inferencia.csv") as file:
                reader=csv.reader(file,delimiter=";")
                for row in reader:
                    data.append(row)
            threshold=[]
            [threshold.append(float(data[l][2])) for l in range(1,len(data))]
            number_of_roses=len(data)-1
            mean_accuracy=round(mean(threshold),2)
            if isnan(mean_accuracy):
                mean_accuracy='No roses found'
            return  HttpResponse(json.dumps({'raw_url':templateurl,'edit_url':nameofInput,'roses':number_of_roses,'accuracy':mean_accuracy}))
    else:
        return render(request,'home.html', {} )