var = 0

gen = (i + 1 for i in range (100) if i % 2==0)
for x in gen:
    print(x)

arreglo_num=[1,2,3]

arreglo_num.append(4)
arreglo_num.extend([5,6])
print(arreglo_num)


tupla=(1,2,3)
print(tupla)

comp= [i +1 for i in range(100) if i %2 != 0]
comp.append(101)
print(comp)

dic = {'color': 'red', 'size': 123, 'width': 205.60}
for key in dic:
    print(key)
    print(dic[key])

    if 'color' in dic:
        print(dic['color'])

def multiplicacion(a1,a2):
    return a1 * a2

print(multiplicacion(2,540))

def mult(a1, a2, i=0, r=0):
    if i < a2:
        return mult(a1, a2, i+1, a1 + r)
    else:
        return r

print(mult(2,6))


def mult2(*args): 
    res =1
    for i in args:
        res*= i
    return res

print(mult2(2,6))

print(mult2(2,6,4,3))

def mult3(**kwargs):
    res=1
    for key in kwargs:
        print(key)
        res*= kwargs[key]
    return res

print(mult3(num1=2, num2=6))

print(mult3(num1=2, num2=6, num3=4, num4=3))

def mult4(*args, **kwargs):
    res =1
    for key in kwargs:
        print(key)
        res *=kwargs[key]

    for i in args:
        res*= i
    return res

print(mult4(3,4, num1=2, num2=6))

def mult5(*args):
    acum=0
    n=args[1]/2
    i=args[0]
    i2=args[0]+1
    for h in range(int(n)):
        print(i * i2)
        i+=2
        i2+=2
        acum+= (i * i2)
    
    return acum
    
mult5(1,100)    

#Lectura de archivos
file = open('archivo1.txt', 'r')
print(file.read())
file.close()

#Escritura
file2 = open('archivo2.txt', 'w')
file2.write('Archivo2 prueba DE NUEVO')
file2.close()

file3 = open('archivo3.txt', 'a')
file3.write('Archivo 3 prueba DE NUEVO')
file3.close()

#Modo Protegido
file4= None
try:
    file4 = open('archivo4.txt', 'a')
    file4.write('\nNueva linea de texto')
    file4.close()
except Exception as e:
    print('Ocurrió un error:', e)
finally: 
    print('Se intentó abrir el archivo')
    
#No necesita close
#Contexto Manager
#with open('archivo4.txt', 'r') as f:
 #   print(f.read())

def abreArchivo():
    with open('archivo4.txt', 'r') as f:
        yield f.readlines()
for line in abreArchivo():
    print(line)