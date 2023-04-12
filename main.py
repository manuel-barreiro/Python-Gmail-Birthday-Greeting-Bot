import datetime as dtime
import random
import pandas as pd
import openpyxl
import yagmail

#Importo speadsheet con la información
df = pd.read_excel('data_limpia.xlsx').drop(columns=['Unnamed: 0'])

#Chequeo si alguien cumple hoy
dia_hoy = dtime.datetime.today().day
mes_hoy = dtime.datetime.today().month
nombre_cumpleanero = []
correo_cumpleanero = []

for i in range(len(df)):
    dia = df['fecha_nac'][i].day
    mes = df['fecha_nac'][i].month
    if dia == dia_hoy and mes == mes_hoy:
        nombre_cumpleanero.append(df['nombre'][i])
        correo_cumpleanero.append(df['email'][i])

if len(nombre_cumpleanero) > 0:

    #Realizado contemplando la posibilidad de que más de un empleado cumpla el mismo día
    for nombre, correo in zip(nombre_cumpleanero, correo_cumpleanero):

        #Defino lista con los nombres de los 3 htmls de los mensajes
        # lista_htmls = ['saludo1.html','saludo2.html','saludo3.html']

        #Hago una elección aleatoria de un archivo html
        # archivo_html = random.choice(lista_htmls)

        archivo_html = 'saludo3.html'

        #Abrimos el archivo html y almacenamos en data el contenido del archivo html, reemplazando [NOMBRE] por el nombre del empleado
        with open(r'{}'.format(archivo_html), 'r') as file:
            data = file.read()
            data = data.replace('[NOMBRE]', nombre)
        #Escribimos ese mismo archivo data (html con el nombre del empleado)
        with open(r'{}'.format(archivo_html), 'w') as file:
            file.write(data)
            file.close()

        #################################### SE ENVIA EL CORREO ##############################################

        yag = yagmail.SMTP(user='comunicacion@weplan-latam.com', password='edarjhehehnozmbf')

        asunto = 'Cumpleaños {}'.format(nombre)

        receptores = list(df.email)

        #En to= va al correo del empleado y se pone en copia oculta (bcc=) a todos, asi no se puede ver la lista de receptores.

        yag.send(to=correo, bcc=receptores, subject=asunto, contents=archivo_html)
        
        ######################################################################################################

        #Abrimos el archivo con el nombre colocado, y le volvemos a poner [NOMBRE], almacenando en variable data
        with open(r'{}'.format(archivo_html), 'r') as file:
            data = file.read()
            data = data.replace(nombre, '[NOMBRE]')
        #Escribimos el mismo archivo sacandole el nombre que le pusimos y poniendole [NOMBRE], escribiendo sobre ese archivo la variable data
        with open(r'{}'.format(archivo_html), 'w') as file:
            file.write(data)
            file.close()  


    




