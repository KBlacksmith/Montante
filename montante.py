#Funciones o Métodos

#Validar que regrese un entero positivo
def numVariables()->int: 
    while True: 
        try: 
            num = int(input("¿Cuántas variables tiene el sistema de ecuaciones (0 para salir)?: "))
        except ValueError: 
            print("Error, debe ingresar un número entero positivo")
        else: 
            if num > 0: 
                return num
            else: 
                print("El número de variables debe ser mayor a 0")

# Preguntar al usuario si desea seguir en el programa o salir
def continuar()->str: 
    # Puede regresar una cadena o un booleano
    sn = ""
    sn = input("Desea ingresar otro sistema de ecuaciones? S/n: ").lower()
    while sn != "s" and sn != "n": 
        sn = input("S/n: ").lower()
    #Al devolver una comparación, regresa un booleano
    return sn == "s"

#Validar que el coeficiente ingresado sea entero
def validarInt(x_i)->int: 
    while True: 
        try: 
            coef = int(input("Coeficiente de x"+str(x_i)+": "))
        except ValueError: 
            print("Entrada inválida, ingrese un número entero como coeficiente")
        else: 
            return coef

#Validar que el vector de términos independientes sea un número flotante
def validarFloat(ecuacion: str)->float: 
    while True: 
        try: 
            val = float(input(ecuacion))
        except: 
            print("Entrada inválida, ingrese un número entero o flotante")
        else: 
            return val

def imprimirMatriz(matriz: list):
    for vec in matriz: 
        renglon = "|"
        for num in vec: 
            renglon +=" "+str(num)+" "
        renglon += "|"
        print(renglon)
    print("")

def imprimirMatrizYAdjunta(matriz: list, adj: list): 
    n = len(matriz)
    for i in range(n): 
        renglon = "|"
        for j in range(n): 
            renglon +=" "+str(matriz[i][j])+" "
        renglon += "|"
        for j in range(n): 
            renglon += " "+str(adj[i][j])+" "
        renglon += "|"
        print(renglon)

# Generar la matriz correspondiente al problema, preguntando por los coeficientes
#Generar la matriz identidad asociada a la matriz del problema
def ingresarEcuaciones(num: int)->tuple:
    #Inicializar la matriz cuadrada
    matriz = [[0 for j in range(num)] for i in range(num)]
    #Inicializar el vector
    vector = [0 for i in range(num)]
    
    for i in range(num): 
        ecuacion = ""
        print("\nEcuación #"+str(i+1))
        for j in range(num): 
            matriz[i][j] = validarInt(j+1)
            if j > 0 and matriz[i][j] >= 0: 
                ecuacion += "+"
            ecuacion += str(matriz[i][j])+"x"+str(j+1)+" "
        ecuacion += "= "
        vector[i] = validarFloat(ecuacion)
        print("-"*20)
    #Python puede regresar una tupla que puede ser "desempacada" al recibirla 
    return matriz, vector

# Método principal
# Decidir si será un método recursivo o solamente iterativo
# Revisar excepciones. 
def montante(matriz: "list[list]")->list:
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
    imprimirMatrizYAdjunta(matriz, adjunta)
    for k in range(n):
        print("\nPivote anterior: "+str(pivote_ant))
        #No hay necesidad de una variable "pivote actual" pues es el elemento ubicado en k,k
        print("Pivote actual: "+str(matriz[k][k]))
        #Verifica que el pivote no sea 0, pues causaría problemas en la siguiente iteracion
        if matriz[k][k] == 0: 
            for i in range(k+1, n): 
                if matriz[i][k] != 0:
                    print("\n=>")
                    print("Cambio de renglón\n\n=>\n")
                    #Cuando se encuentra un renglón que cumpla con la confición deseada, se intercambian sus contenidos
                    aux = matriz[k].copy()
                    matriz[k] = matriz[i].copy()
                    matriz[i] = aux.copy()
                    aux = adjunta[k].copy()
                    adjunta[k] = adjunta[i].copy()
                    adjunta[i] = aux.copy()
                    imprimirMatrizYAdjunta(matriz, adjunta)
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
        pivote_ant = matriz[k][k]
        print("\n=>\n")
        imprimirMatrizYAdjunta(matriz, adjunta)
    print("-"*20)
    print("Determinante: "+str(matriz[n-1][n-1]*signo))
    for i in range(n): 
        for j in range(n): 
            adjunta[i][j] = adjunta[i][j]/matriz[n-1][n-1]
    print("-"*20)
    print("Matriz inversa: ")
    imprimirMatriz(adjunta)
    return adjunta

#Con la matriz inversa ya podemos calcular los valores de las variables
def calcularVariables(inversa: list, vector: list): 
    print("-"*20)
    for i in range(len(vector)): 
        x = 0
        for j in range(len(vector)): 
            x += vector[j]*inversa[i][j]
        print("x"+str(i+1)+" = "+str(x))
    print("-"*20)

#Llamada al programa, lo equivalente a la función main() en otros lenguajes
if __name__=="__main__": 
    print("Método Bareiss-Montante")
    # Inicializar variables
    cont = True
    while cont: 
        #Decidir tamaño de la matriz
        num = numVariables()
        #Desempacamos tuplas para recibir dos componentes de la respuesta
        matriz, vector = ingresarEcuaciones(num)
        inversa = montante(matriz)
        if len(inversa) > 0: 
            calcularVariables(inversa, vector)
        else: 
            print("No se pudo resolver el sistema de ecuaciones, porque el pivote actual es igual a 0")
        #Preguntar si desea continuar
        cont = continuar()
    # Fin