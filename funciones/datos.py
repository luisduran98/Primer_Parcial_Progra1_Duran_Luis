from UTN_Heroes_Dataset.utn_pp import get_original_matrix

matriz_concesionaria =  get_original_matrix()
garages = []


def limpiar():
    from os import system
    system("cls") 
    
def pausar():
    from os import system
    system("pause")

def carga_de_datos():
    if len(garages) == 0:
        for elem in matriz_concesionaria[0]:
            garages.append([elem])
    
        for i in range(0, len(garages)):
            garages[i].append(matriz_concesionaria[1][i])
    
        for i in range(0, len(garages)):
            garages[i].append(matriz_concesionaria[2][i])

        for i in range(0, len(garages)):
            garages[i].append(matriz_concesionaria[3][i])


def mostrar_datos():
        limpiar()
        print("----------------------------- Informe de Garajes ---------------------------------")
        print("Garage               Marca              Modelo                    Cantidades      ")
        for i in range(0,len(garages)):
             print(f"|{i+1:^3}|           {garages[i][0]:^20}{garages[i][1]:^20}{garages[i][2]:^30}")
        pausar()


def cantidad_de_vehiculos():
    limpiar()
    suma = 0 
    for i in range(0,20):
        suma += garages[i][2]
    print(f"La cantidad total de vehiculos es {suma}")
    pausar()

def vehiculos_menor():
    limpiar()
    cache_indice = 1
    menor = garages[0][2]
    for i in range(1,20):
        if menor > garages[i][2]:
            cache_indice = i
            menor = garages[i][2]
    print(f"Marca: {garages[cache_indice][0]}, Modelo: {garages[cache_indice][1]}, Cantidad: {garages[cache_indice][2]}")
    pausar()

def vehiculos_mayor():
    limpiar()
    cache_indice = None
    mayor = 0
    for i in range(0,20):
        if garages[i][2] > mayor:
            cache_indice = i
            mayor = garages[i][2]
    
    print(f"Marca: {garages[cache_indice][0]}, Modelo: {garages[cache_indice][1]}, Cantidad: {garages[cache_indice][2]}")
    pausar()

def recaudacion_unitaria():
    limpiar()
    print("-------------------- Informe de Garajes -----------------------")
    print("Garage   Marca          Modelo          Cantidades        Total")
    for i in range(0,20):
        print(f"|{i+1}| {garages[i][0]:<15} {garages[i][1]:10} {garages[i][2]:20} {garages[i][2] * garages[i][3]}")
    pausar()

def mas_de_seis():
    limpiar()
    mayor = 6
    grupo = []
    for i in range(0,20):
        if garages[i][2] >= mayor:
            grupo.append(i)
    print(f"{len(grupo)} garages tienen 6 o mas vehiculos")    
    pausar()

