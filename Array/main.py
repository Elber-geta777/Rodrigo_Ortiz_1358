import xlrd

data=[]

for anio in range(1985,2019):
    anio_lista=[]
    archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
    hoja=archivo.sheet_by_index(0)
    for estado in range(2,34):
        mes_lista=[]
        for mes in range(1,13):
            mes_lista.append("%.2f" % hoja.cell_value(estado,mes))
        anio_lista.append(mes_lista)
    data.append(anio_lista)

print(data)
#main
estado=int(input('Que estado(1-32)?:'))
anio=int(input("año(1985-2019)?:"))
mes=int(input("mes(1-12)?:"))

print(f"el promedio mensual es:{data[anio-1985][estado-1][mes-1]}")
