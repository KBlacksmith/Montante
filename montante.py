#Funciones o Métodos

#Validar que regrese un entero positivo
def numVariables()->int: 
    while True: 
        try: 
            num = int(input("¿Cuántas variables tiene el sistema de ecuaciones (0 para salir)?: "))
            pass
        except ValueError: 
            print("Error, debe ingresar un número entero positivo")
        else: 
            if num >= 0: 
                return num
            else: 
                print("El número debe ser mayor o igual a 0")

# Preguntar al usuario si desea seguir en el programa o salir
def continuar()->str: 
    # Puede regresar una cadena o un booleano
    sn = ""
    sn = input("Desea ingresar otro sistema de ecuaciones? S/n: ").lower()
    while sn != "s" and sn != "n": 
        sn = input("S/n: ").lower()
    return sn == "s"

def imprimirMatriz(matriz: list): 
    # Solamente imprime la matriz, dandole formato para que sea legible
    pass

def imprimirMatrizYAdjunta(matriz: list, adj: list): 
    # Similar a la anterior, pero ahora da formato para imprimir una matriz y su matriz adjunta
    pass

def validarInt(x_i)->int: 
    while True: 
        try: 
            coef = int(input("Coeficiente de x"+str(x_i)+": "))
        except ValueError: 
            print("Entrada inválida, ingrese un número entero como coeficiente")
        else: 
            return coef

def validarFloat(ecuacion: str)->float: 
    while True: 
        try: 
            val = float(input(ecuacion))
            pass
        except: 
            print("Entrada inválida, ingrese un número entero o flotante")
            pass
        else: 
            return val

# Generar la matriz correspondiente al problema, preguntando por los coeficientes
#Generar la matriz identidad asociada a la matriz del problema
def inicializar(num: int)->tuple:
    #Python puede regresar una tupla que puede ser "desempacada" al recibirla 
    #return matriz, vector
    pass

# Método principal
# Decidir si será un método recursivo o solamente iterativo
# Revisar excepciones. 
def montante(matriz: "list[list]")->list:
    #imprimirMatriz(matriz)
    print(matriz)
    #Almacenar el tamaño de la matriz cuadrada
    n = len(matriz)
    #Inicializar la matriz adjunta como una matriz identidad de tamaño nXn
    adjunta = [[0 if i!=j else 1 for i in range(n)] for j in range(n)]
    #Inicializar el pivote anterior
    pivote_ant = 1
    #Inicializar las matrices auxiliares para realizar las operaciones
    nueva_m = [["x" for i in range(n)] for j in range(n)]
    nueva_adj = [["x" for i in range(n)] for j in range(n)]
    #En caso de haber un cambio de renglon, cambiaría el signo del determinante
    #Con la variable "signo" podemos llevar el control para obtener el determinante de la matriz original
    signo = 1
    #Ciclo para controlar cuantas veces se debe de realizar el proceso
    for k in range(n):
        #Verifica que el pivote no sea 0, pues causaría problemas en la siguiente iteracion
        if matriz[k][k] == 0: 
            for i in range(k+1, n): 
                if matriz[i][k] != 0:
                    #Cuando se encuentra un renglón que cumpla con la confición deseada, se intercambian sus contenidos
                    aux = matriz[k].copy()
                    matriz[k] = matriz[i].copy()
                    matriz[i] = aux.copy()
                    aux = adjunta[k].copy()
                    adjunta[k] = adjunta[i].copy()
                    adjunta[i] = aux.copy()
                    del aux
                    #Actualizamos el signo del determinante
                    signo *=-1
                    break
            else: 
                if matriz[k][k] == 0: 
                    #Si el pivote = 0 persiste, el método regresa una matriz vacía
                    return []
        #Ciclos del método principal
        for i in range(n): 
            for j in range(n): 
                if i == k: 
                    #Si el renglon de la iteración es igual al del pivote actual, se copian los numeros a la matriz nueva
                    nueva_m[i][j] = matriz[i][j]
                    nueva_adj[i][j] = adjunta[i][j]
                else:
                    #Si no, se realizan las operaciones
                    nueva_m[i][j] = (matriz[k][k]*matriz[i][j] - matriz[i][k]*matriz[k][j])/pivote_ant
                    nueva_adj[i][j] = (adjunta[i][j]*matriz[k][k] - matriz[i][k]*adjunta[k][j])/pivote_ant
        #Se copian los elementos de las matrices auxiliares a las principales
        for i in range(n): 
            for j in range(n): 
                matriz[i][j] = nueva_m[i][j]
                adjunta[i][j] = nueva_adj[i][j]
        print("\nPivote anterior: "+str(pivote_ant))
        pivote_ant = matriz[k][k]
        #No hay necesidad de una variable "pivote actual" pues es el elemento ubicado en k,k
        print("Pivote actual: "+str(matriz[k][k]))
        print("\n=>\n")
        print("Matriz: ")
        print(matriz)
        print("Adjunta: ")
        print(adjunta)
        #imprimirMatriz(matriz)
    print("\nDeterminante: "+str(matriz[n-1][n-1]*signo))
    for i in range(n): 
        for j in range(n): 
            adjunta[i][j] = adjunta[i][j]/matriz[n-1][n-1]
    print("Matriz inversa: ")
    #imprimirMatriz(adjunta)
    print(adjunta)
    return adjunta

#Llamada al programa, lo equivalente a la función main() en otros lenguajes
if __name__=="__main__": 
    # Inicializar variables
    cont = True
    while cont: 
        #Decidir tamaño de la matriz
        num = numVariables()
        if num > 0: 
            # matriz, vector = inicializar(num)
            # montante(matriz)
            montante([[3, 6, -1], [7, -1, 2], [-2, -1, -1]])
        #Preguntar si desea continuar
        cont = continuar()
    # Fin