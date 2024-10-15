def limpiar():
    from os import system
    system("cls") 
    
def pausar():
    from os import system
    system("pause")

def menu()->None:
    limpiar()
    print("|1| Cargar datos")
    print("|2| Cantidad total de unidades almacenadas")
    print("|3| Informe completo del garaje con menos unidades de vehiculos")
    print("|4| Informe de garaje con mayor cantidad de vehiculos")
    print("|5| Calcular recaudacion de garajes")
    print("|6| Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos")
    print("|7| Porcentaje de unidades de cada marca")
    print("|8| informe de recaudacion de cada garaje ")
    print("|9| Salir")
    return input("Coloca un numero: ")
    


