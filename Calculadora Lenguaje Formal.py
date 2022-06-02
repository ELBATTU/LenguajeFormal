##Author: BATTU
Cadena = input("Introduce el alfabeto: ");
Alfabeto = Cadena.split()
print(Alfabeto);

Lenguaje1 = input("Introduce el lenguaje 1: ");
Lenguaje2 = input("Introduce el lenguaje 2: ");

PrimerLenguaje = Lenguaje1.split();
SegundoLenguaje = Lenguaje2.split();

print(PrimerLenguaje);
print(SegundoLenguaje);

#Menu
def Menu():
    print("****    MENU    ****");
    print("1.Union\n 2.Interseccion\n 3.Diferencia\n 4.Complemento\n 5.Concatenacion");
    print("8.M-esima potencia\n 9.Estrella de Kleene\n 10.Operador mas\n 11.I-esima m-ava parte");
    print("12.M-esima repeticion\n 13.Raiz M-esima\n 14.Cociente Izquierdo\n 15.Derivada Izquierda");
    print("16.Cociente Derecho\n 17.Derivada Derecha\n 18.Reverso");

def Union(pPrimerLenguaje, pSegundoLenguaje):
    Respuesta = pPrimerLenguaje + pSegundoLenguaje;
    ## Aux = Respuesta.copy();
    ## Inter = Interseccion(pPrimerLenguaje, pSegundoLenguaje);
    ## for k in range(len(Aux)):
    ##     for i in range(len(Inter)):
    ##          if(Aux[k] is Inter[j]):
    ##            Respuesta.remove(Inter[i]);
    ## Respuesta = Respuesta + Inter;
    return Eliminar_Repetidos(Respuesta);

def Interseccion(pPrimerLenguaje, pSegundoLenguaje):
    Respuesta = [];
    for i in range(len(pPrimerLenguaje)):
        for j in range(len(pSegundoLenguaje)):
            if (pPrimerLenguaje[i] == pSegundoLenguaje[j]):
                Respuesta.append(pPrimerLenguaje[j]);
    return Respuesta;

def Complemento(pPrimerLenguaje, pSegundoLenguaje):
    print("Complemento de [L1 = Σ* - ", pPrimerLenguaje);
    print("Complemento de [L2 = Σ* - ", pSegundoLenguaje);

def Concatenacion(pPrimerLenguaje, pSegundoLenguaje):
    Respuesta = [];
    for i in range(len(pPrimerLenguaje)):
         for k in range(len(pSegundoLenguaje)):
             Respuesta.append(pSegundoLenguaje[k] + pPrimerLenguaje[i]);
    return Respuesta;

def Diferencia(pPrimerLenguaje, pSegundoLenguaje):
    Respuesta = [];
    Inter = Interseccion(pPrimerLenguaje, pSegundoLenguaje);
    for i in range(len(pPrimerLenguaje)):
            for j in range(len(Inter)):
                if (pPrimerLenguaje[i] != Inter[j]):
                    Respuesta.append(pPrimerLenguaje[i]);
    return Respuesta;

def Potencia_Lenguaje(L1,exp):
    if(exp == 1):
        return L1;
    if(exp == 0):
        Null = []
        Null.append("λ")
        return Null;
    Aux = L1.copy();
    if(len(L1) > 1):
        exp = exp - 1;
        while(exp > 0):
            for i in range(len(L1)):
                Aux[i] += L1[i]
                exp = exp - 1
        L1 = Aux
    else:
        Aux = L1;
        return Aux;
    return Eliminar_Repetidos(Examinar_Lenguaje_Nil(Aux))

def Clausura_Positiva(L1):
    LAux = []
    LAux = L1
    i = 2
    while(i<=4):
        LAux=Union(LAux,Potencia_Lenguaje(L1,i))
        i+=1
        LAux.append("........")
        return Eliminar_Repetidos(LAux)

def EstrellaDeKleene(L1):
    LAux = []
    LAux = L1
    LAux=Union(Potencia_Lenguaje(L1,0),Clausura_Positiva(L1))
    LAux.append("........")
    return Eliminar_Repetidos(LAux)

def i_Esima_m_Ava_Parte(L,parte,fraccion):
    L2 = []
    for i in range(len(L)):
        if(parte<=fraccion and Multiplo(len(L[i]),fraccion)==True):
           L2.append(Reducir_Palabra_m_ava_Parte(L[i],parte,fraccion))
    return Eliminar_Repetidos(L2)

def Multiplo(A,B):
    if(A%B==0):
        return True
    else:
        return False

def Reducir_Palabra_m_ava_Parte(palabra,parte,fraccion):
    if(parte<=fraccion and Multiplo(len(palabra),fraccion)==True):
        while(fraccion>parte):
            palabra=Eliminar_Elementos_Cadena_Atras(palabra,len(palabra)//fraccion)
            fraccion-=1
        i=1
        while(i<parte):
            palabra=Eliminar_Elementos_Cadena_Delante(palabra,len(palabra)//fraccion)
            i+=1
        return palabra

def Eliminar_Elementos_Cadena_Atras(Cadena,cantidad):
    Invertir_Cadena(Cadena)
    for i in range(cantidad):
        Cadena=Cadena[:len(Cadena)-1]
    Invertir_Cadena(Cadena)
    return Cadena

def Invertir_Cadena(Cadena):
    Aux=""
    for i in range(len(Cadena)-1,-1,-1):
        Aux+=Cadena[i];
        return Aux

def Eliminar_Elementos_Cadena_Delante(Cadena,cantidad):
    for i in range(cantidad):
        Cadena=Cadena[1:]
    return Cadena

def Examinar_Lenguaje_Nil(L):
    L2 = []
    for i in range(len(L)):
        Aux =  Examinar_Palabra_Nil(L[i])
        if(Aux != ""):
            L2.append(Aux)
    return Eliminar_Repetidos(L2)

def Examinar_Palabra_Nil(Palabra):
    if(Palabra.find("nill")):
        Palabra=Palabra.replace("nil","")
    if(len(Palabra) == 0):
        Palabra = "nil"
    return Palabra

def Copiar_Leguaje(L1):
    L2 = []
    for i in range(len(L1)):
        if(L1[i] != -1):
            L2.append(L1[i])
    return L2

def Eliminar_Repetidos(L1):
    rang = len(L1)
    for i in range(0,rang):
        for j in range(0,rang):
            if(i != j):
                if(L1[i] == L1[j]):
                    L1[j] = -1
    L2 = Copiar_Leguaje(L1)
    L1 = L2
    return L1

def m_Esima_Repeticion(L1,rep):
    L2=[]
    for i in range(len(L1)):
        x = rep
        Aux = L1[i]
        while(x>1):
            Aux += L1[i]
            x-=1
        L2.append(Aux)
    return Eliminar_Repetidos(L2)

def Raiz_m_Esima(Evaluar,L1,raiz):
    L3 = []
    for i in range(len(L1)):
        for j in range(len(Evaluar)):
            if(m_Esima_Repeticion(L1[i],raiz) == Evaluar[j]):
                L3.append(L1[i])
    return Eliminar_Repetidos(L3)

def Cociente_Izquierdo(L1,L2):
    L3 = []
    k = 0
    if(Existe_Nil(L2) == True):
        L3 = L1
        L3.insert(0,"nil")
        k = len(L1) + 1
    for i in range(len(L1)):
        x = -1
        X = ""
        for j in range(len(L2)):
            if(len(L1[i]) >= len(L2[j])):
                if(L1[i] == L2[j]):
                    X = "nil"
                    x = 1
                else:
                    if(X == ""):
                        X = Eliminar_Elementos_Cadena_Atras(L1[i],len(L2[j]))
                        if((X + L2[j]) == L1[i]):
                            x=1
                        else:
                            X=""
        if(x == 1):
            if(Existe_Elemento(L3,X) == False):
                L3.append(X)
        k += 1
    return Eliminar_Repetidos(L3)

def Existe_Elemento(L1,Elem):
    T=False
    for i in range(len(L1)):
        if(L1[i]==Elem):
            T=True
    return T

def Existe_Nil(L1):
    exp = False
    for i in range(len(L1)):
        if(L1[i]=="nil"):
            exp = True
    return exp

def Derivada_Izquierda(L1,x):
    L2=[]
    if(x=="nil"):
        L2=L1
    else:
        for i in range(len(L1)):
            if(L1[i]==x):
                L2.append("nil")
            else:
                if(Eliminar_Elementos_Cadena_Delante(L1[i],len(L1[i])-len(x))==x):
                    L2.append(Eliminar_Elementos_Cadena_Atras(L1[i],len(x)))
    return Eliminar_Repetidos(L2)

def Cociente_Derecho(L1,L2):
    L3 = []
    k=0
    if(Existe_Nil(L2) == True):
        L3 = L1
        L3.insert(0,"nil")
        k = len(L1) + 1
    for i in range(len(L1)):
        x =- 1
        X = ""
        for j in range(len(L2)):
            if(len(L1[i]) >= len(L2[j])):
                if(L1[i] == L2[j]):
                    X = "nil"
                    x = 1
                else:
                    if(X == ""):
                        X = Eliminar_Elementos_Cadena_Delante(L1[i],len(L2[j]))
                        if((L2[j] + X) == L1[i]):
                            x=1
                        else:
                            X=""
        if(x==1):
            if(Existe_Elemento(L3,X)==False):
                L3.append(X)
        k += 1
        return Eliminar_Repetidos(L3)

def Derivada_Derecha(L1,x):
    L2=[]
    if(x=="nil"):
        L2=L1
    else:
        for i in range(len(L1)):
            if(L1[i]==x):
                L2.append("nil")
            else:
                if(Eliminar_Elementos_Cadena_Atras(L1[i],len(L1[i])-len(x))==x):
                    L2.append(Eliminar_Elementos_Cadena_Delante(L1[i],len(x)))
    return Eliminar_Repetidos(L2)

Menu();
print("Union L1 U L2 = ",Union(PrimerLenguaje,SegundoLenguaje));
print("Interseccion L1 ∩ L2 = ",Interseccion(PrimerLenguaje,SegundoLenguaje));
Complemento(PrimerLenguaje,SegundoLenguaje);
print("Concatenacion: = ",Concatenacion(PrimerLenguaje,SegundoLenguaje));
print("Diferencia L1 - L2 = ",Diferencia(PrimerLenguaje,SegundoLenguaje));
print("Potencia: = ",Potencia_Lenguaje(PrimerLenguaje,5));
print("Estrella de kleene: = ",EstrellaDeKleene(PrimerLenguaje));
print("Operador: = ",Clausura_Positiva(PrimerLenguaje));
print("1-esima-ava-parte: = ",i_Esima_m_Ava_Parte(PrimerLenguaje,1,2));
print("M-esima-parte: = ",m_Esima_Repeticion(PrimerLenguaje,2));
print("Raiz_m_Esima: = ",Raiz_m_Esima(SegundoLenguaje,PrimerLenguaje,2));
print("Cociente_Izquierdo: = ",Cociente_Izquierdo(PrimerLenguaje,SegundoLenguaje));
print("Derivada_Izquierda: = ",Derivada_Izquierda(PrimerLenguaje,"a"));
print("Cociente_Derecho: = ",Cociente_Derecho(PrimerLenguaje,SegundoLenguaje));
print("Derivada_Derecha: = ",Derivada_Derecha(PrimerLenguaje,"a"));
print("Reverso: = ",Invertir_Cadena(PrimerLenguaje));
