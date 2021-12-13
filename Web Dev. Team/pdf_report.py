from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import numpy as np
from os import getcwd
import shutil
import sys
import csv
import datetime

w, h = A4
# create pdf and recover data######### '/home/juanchx/Documentos/UNIVERSIDAD/reporte.pdf
destination = 'webapp/static/buttonpython/Report.pdf'

# if (len(sys.argv))==2:
#    destination = sys.argv[1]
# else:
#    "error de ruta"

# modificar=destination.split("/")[:-1]
# modificar='/'.join(modificar)+"/pdf2.pdf"
# print("----")
# print(modificar)

c = canvas.Canvas(destination, pagesize=A4)
data = []
with open("inferencia.csv") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        data.append(row)


###############Prueba
c.setFillColorRGB(0, 0, 0)
c.drawString(40, h - 17, "--------------------------------------------------------------------------------------------------------------------------------")
c.drawString(40, h - 75, "--------------------------------------------------------------------------------------------------------------------------------")


####################TITLE#############################

title = "Counting Report"
# print(len(title))
c.setFillColorRGB(0, 0, 0)
text = c.beginText(180, h - 55)
text.setFont("Times-Bold", 35)
# Las dos frases aparecen en dos líneas diferentes.
text.textLine(title)
c.drawText(text)

######################################################
dataPaths = []
with open("inferenciapath.csv") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        dataPaths.append(row)
Name_of_input_file = (dataPaths[1][0])
Name_of_output_file = (dataPaths[1][1])
print(Name_of_input_file)
print(Name_of_output_file)

##################HEAD################################
c.setFillColorRGB(0, 0, 0)
N_roses = str(len(data)-1)
Path_of_output_file = destination  # cambiar por el path del archivo
date = datetime.datetime.now()
text2 = c.beginText(50, h - 110)
text2.setFont("Times-Roman", 15)
# Las dos frases aparecen en dos líneas diferentes.
text2.textLine("Date: " + date.strftime("%Y-%m-%d"))
text2.textLine("Roses found: " + N_roses)
#text2.textLine("Name of the of analysis image:  "+str(Name_of_input_file.split('/')[-1]))
c.drawText(text2)


######################################################

###########################Imagenes####################
c.setFont("Times-Bold", 15)
c.drawString(130, h - 160, "Your image")
c.drawImage(Name_of_input_file, 49, h - 360, width=240, height=180)
c.drawString(380, h - 160, "After counting")
c.drawImage(Name_of_output_file, 309, h - 360, width=240, height=180)

#######################################################

############################table  with all roses founded###############


def xport_table():
    c.setFont("Times-Roman", 13)
    x_offset = 60
    y_offset = 390
    # Space between rows.
    max_rows_per_page = 25
    padding = 15
    xlist = [x + x_offset for x in [0, 85, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(len(data)+1)]
    # print("\n")
    # print(ylist)
    # print("\n")
    numero_col = 0
    # print(data[3][0])
    # print(data[3][1])
    # print(data[3][2])
    for rows in range(len(data)):
        c.grid(xlist, ylist)
        for i in range(len(xlist)-1):
            # print(rows,i)
            if (i == 0):
                c.drawString(x_offset + 20, h - 12-y_offset -
                             15*numero_col, data[rows][i])
            if (i == 1):
                c.drawString(x_offset + 110, h - 12-y_offset -
                             15*numero_col, data[rows][i])
            if (i == 2):
                c.drawString(x_offset + 412, h - 12-y_offset -
                             15*numero_col, data[rows][i])
        numero_col += 1


xport_table()
########################Footer##################################
c.setFillColorRGB(0, 0, 0)
date = datetime.datetime.now()
text3 = c.beginText(250, h - 830)
text3.setFont("Times-Bold", 10)
text3.textLine("Made by Carlos, Juan, Leo & Mike")
c.drawText(text3)
################################################################
c.showPage()
c.save()
output = "TODO BIEN"
###############save file in specific directory#######################
