import os
from Util.ArchivosUtilClases import FileUtil
fileutil = FileUtil()
NombreDelArchivoTabla="Proyecto Masvi/Tabla.csv"



class Tabla:
    def __init__ (self, Edad, lx, qx, px, dx, Sx):
        self.Edad= Edad
        self.lx= lx
        self.qx= qx
        self.px= px
        self.dx= dx
        self.Sx= Sx
    
    def __str__ (self):
        return str(self.Edad) + "," + str(self.lx) + "," + str(self.qx) + "," + str(self.px) + "," + str(self.dx) + "," + str(self.Sx)


class Manipulacion:
    def VerMisDatos(self):
        ListaTabla=[]
        DatosTabla=fileutil.LeerArchivo(NombreDelArchivoTabla)
        for i in DatosTabla:
            DatosTabla= i.strip().split(',')
            DatoNuevo= Tabla(DatosTabla[0], DatosTabla[1], DatosTabla[2], DatosTabla[3], DatosTabla[4], DatosTabla[5])
            ListaTabla.append(DatoNuevo)
        return ListaTabla


Manipular=Manipulacion()
Lista=Manipular.VerMisDatos()


opc='s'
while opc=='s':
    os.system("cls")
    Edad1=int(input("Ingrese Edad de la Persona 1: "))
    Edad2=int(input("Ingrese Edad de la Persona 2: "))
    ListaMax=[]
    ListaMin=[]
    Listaaux=[]
    ListaEVC=[]
    ListaEVCAnualidad=[]
    ListaAnualidadAx=[]
    ListaAnualidadAy=[]
    cont=0
    cont2=0
    tasa=.05
    Ax=0.0
    Ay=0.0
    AxyVC=0.0
    AxyUS=0.0
    AxAnticipado=0.0
    AxVencida=0.0
    AyAnticipada=0.0
    AyVencida=0.0
    AxyVCAnAnticipada=0.0
    AxyVCAnVencida=0.0
    AxyUSAnAnticipada=0.0
    AxyUSVencida=0.0
    acumaux=0
    if Edad1 > Edad2:#Creacion de Matriz para cuando la edad 1 es mayor a la edad 2
        for i in Lista:
            if int(i.Edad) >= Edad1:#En este caso edad 1 es mayor por lo tanto sus datos se almacenaran en la matriz con datos mayores
                Listaaux.append(cont)
                edadux=i.Edad
                Listaaux.append(edadux)
                qxaux=i.qx
                Listaaux.append(qxaux)
                lxaux=i.lx
                Listaaux.append(lxaux)
                if cont==0:
                    lxtemporalMin=int(lxaux)
                Sx=float(lxaux)/lxtemporalMin
                Listaaux.append(Sx)
                Descuentoaux=1/((1+tasa)**(cont+1))
                Listaaux.append(Descuentoaux)
                ListaMin.append(Listaaux)
                Listaaux=[]
                cont=cont+1
            if int(i.Edad) >= Edad2:
                Listaaux.append(cont2)
                edadux=i.Edad
                Listaaux.append(edadux)
                qxaux=i.qx
                Listaaux.append(qxaux)
                lxaux=i.lx
                Listaaux.append(lxaux)
                if cont2==0:
                    lxtemporalMax=int(lxaux)
                Sx=float(lxaux)/lxtemporalMax
                Listaaux.append(Sx)
                Descuentoaux=1/((1+tasa)**(cont2+1))
                Listaaux.append(Descuentoaux)
                ListaMax.append(Listaaux)
                Listaaux=[]
                cont2=cont2+1
        cont=0
        cont2=0
    else:
        for i in Lista:#Creacion de la Matriz para cuando la edad 2 es mayor o igual a la edad 1
            if int(i.Edad) >= Edad2:#se asignan valores a la lista de edad maxima que en este caso corresponden a nuestra edad 2
                Listaaux.append(cont)
                edadux=i.Edad
                Listaaux.append(edadux)
                qxaux=i.qx
                Listaaux.append(qxaux)
                lxaux=i.lx
                Listaaux.append(lxaux)
                if cont==0:
                    lxtemporalMin=int(lxaux)
                Sx=float(lxaux)/lxtemporalMin
                Listaaux.append(Sx)
                Descuentoaux=1/((1+tasa)**(cont+1))
                Listaaux.append(Descuentoaux)
                ListaMin.append(Listaaux)
                Listaaux=[]
                cont=cont+1
            if int(i.Edad) >= Edad1:#Se asignan los valores a la matriz de edad minima que en este caso corresponde a nuestra edad 1
                Listaaux.append(cont2)
                edadux=i.Edad
                Listaaux.append(edadux)
                qxaux=i.qx
                Listaaux.append(qxaux)
                lxaux=i.lx
                Listaaux.append(lxaux)
                if cont2==0:
                    lxtemporalMax=int(lxaux)
                Sx=float(lxaux)/lxtemporalMax
                Listaaux.append(Sx)
                Descuentoaux=1/((1+tasa)**(cont2+1))
                Listaaux.append(Descuentoaux)
                ListaMax.append(Listaaux)
                Listaaux=[]
                cont2=cont2+1
        cont=0
        cont2=0
    for i in ListaMax:
        Ax=float(ListaMax[cont][2])*float(ListaMax[cont][4])*float(ListaMax[cont][5])+Ax
        cont=cont+1
    cont=0
    cont2=0
    for i in ListaMin:
        Ay=float(ListaMin[cont][2])*float(ListaMin[cont][4])*float(ListaMin[cont][5])+Ay
        cont=cont+1
    cont=0
    cont2=0
    for i in ListaMin:
        Listaaux.append(cont)
        Sxy=(float(ListaMax[cont][3])/float(ListaMax[0][3]))*(float(ListaMin[cont][3])/float(ListaMin[0][3]))
        Listaaux.append(Sxy)
        qxy=(float(ListaMax[cont][2])+float(ListaMin[cont][2]))-(float(ListaMin[cont][2])*float(ListaMax[cont][2]))
        Listaaux.append(qxy)
        FlujoEsperado=Sxy*qxy
        Listaaux.append(FlujoEsperado)
        FactorDescuento=1/((1+tasa)**(cont+1))
        Listaaux.append(FactorDescuento)
        ListaEVC.append(Listaaux)
        AxyVC=float(ListaEVC[cont][3])*float(ListaEVC[cont][4])+AxyVC
        cont=cont+1
        Listaaux=[]
    cont=0
    AxyUS=Ax+Ay-AxyVC
    for i in ListaMax:
        Dato1=ListaMax[cont][0]
        Listaaux.append(Dato1)
        Dato2=ListaMax[cont][1]
        Listaaux.append(Dato2)
        Dato3=ListaMax[cont][2]
        Listaaux.append(Dato3)
        Dato4=ListaMax[cont][3]
        Listaaux.append(Dato4)
        Dato5=float(ListaMax[cont][4])
        Listaaux.append(Dato5)
        Dato6=1/((1+tasa)**(cont))
        Listaaux.append(Dato6)
        ListaAnualidadAx.append(Listaaux)
        AxAnticipado=Dato5*float(Listaaux[5])+AxAnticipado
        cont=cont+1
        Listaaux=[]
    cont=0
    for i in ListaMin:
        Dato1=ListaMin[cont][0]
        Listaaux.append(Dato1)
        Dato2=ListaMin[cont][1]
        Listaaux.append(Dato2)
        Dato3=ListaMin[cont][2]
        Listaaux.append(Dato3)
        Dato4=ListaMin[cont][3]
        Listaaux.append(Dato4)
        Dato5=float(ListaMin[cont][4])
        Listaaux.append(Dato5)
        Dato6=1/((1+tasa)**(cont))
        Listaaux.append(Dato6)
        ListaAnualidadAy.append(Listaaux)
        AyAnticipada=Dato5*float(Listaaux[5])+AyAnticipada
        cont=cont+1
        Listaaux=[]
    cont=0
    AxVencida=AxAnticipado-1
    AyVencida=AyAnticipada-1
    print("Ax Vencida: ", AxVencida)
    print("AX Anticipada: ", AxAnticipado)
    print("Ay Vencida: ", AyVencida)
    print("Ay Anticipada: ", AyAnticipada)
    for i in ListaAnualidadAy:
        Listaaux.append(cont)
        Sxy=(float(ListaAnualidadAx[cont][3])/float(ListaAnualidadAx[0][3]))*(float(ListaAnualidadAy[cont][3])/float(ListaAnualidadAy[0][3]))
        Listaaux.append(Sxy)
        qxy=(float(ListaAnualidadAx[cont][2])+float(ListaAnualidadAy[cont][2]))-(float(ListaAnualidadAy[cont][2])*float(ListaAnualidadAx[cont][2]))
        Listaaux.append(qxy)
        FlujoEsperado=Sxy
        Listaaux.append(FlujoEsperado)
        FactorDescuento=1/((1+tasa)**(cont))
        Listaaux.append(FactorDescuento)
        ListaEVCAnualidad.append(Listaaux)
        AxyVCAnAnticipada=float(ListaEVCAnualidad[cont][3])*float(ListaEVCAnualidad[cont][4])+AxyVCAnAnticipada
        cont=cont+1
        Listaaux=[]
    cont=0
    AxyVCAnVencida=AxyVCAnAnticipada-1
    AxyUSAnAnticipada=(AxAnticipado+AyAnticipada)-AxyVCAnAnticipada
    AxyUSVencida=(AxVencida+AyVencida)-AxyVCAnVencida
    print("Axy VC Vencida: ", AxyVCAnVencida)
    print("Axy VC Anticipada: ", AxyVCAnAnticipada)
    print("Axy US Vencida: ", AxyUSVencida)
    print("Axy US Anticipada: ", AxyUSAnAnticipada)

    os.system("pause")




