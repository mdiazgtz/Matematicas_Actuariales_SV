import os
class FileUtil:
    def CrearArchivo(self, NombreArchivo):
        archivo= open(NombreArchivo, 'w')
        archivo.close()
    
    def LeerArchivo(self, NombreArchivo):
        archivo= open(NombreArchivo, 'r')
        lineas= archivo.readlines()
        archivo.close()
        return lineas
    
    def EscribirArchivo(self, NombreArchivo, Datos):
        archivo= open(NombreArchivo,'w')
        archivo.write(Datos + '\n')
        archivo.close()
    
    def AgregarAlArchivo(self, NombreArchivo, Datos):
        archivo= open(NombreArchivo, 'a')
        archivo.write(Datos + '\n')
        archivo.close()

    def EscribirArchivoLista(self, NombreArchivo, Datos):
        archivo= open(NombreArchivo, 'w')
        if len(Datos) != 0:
            for dato in Datos:
                archivo.write((dato + '\n'))
            archivo.close()
    
    def AgregarAlArchivoLista (self, NombreArchivo, Datos):
        archivo= open(NombreArchivo, 'a')
        if len(Datos) != 0:
            for dato in Datos:
                archivo.write((dato + '\n'))
            archivo.close()
    