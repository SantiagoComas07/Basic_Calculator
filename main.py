"""Basic Calculator"""

import time


print(" ")
print("Bienvenido a Basic Calculator")
print(" ")


#Company

print("By:")
print("---------------------------------------")
print("|     -----  -----  ----   --  --     |")
print("|     -      -   -  -   -  -    -     |")  
print("|     -      -   -  -   -  -    -     |")
print("|     - - -  - - -  - -     -  -      |")
print("---------------------------------------")
print(" ")

variableOne=float(input("Por favor, ingrese el primer  número: "))
variableTwo=float(input("Por favor, ingresa el segundo numero: "))


#Menu de opciones

print(" ")
print(" ---------------------- ")
print("|   Menu de opciones   |")
print("|----------------------|")
print("| Suma            (1)  |")
print("| Resta           (2)  |")
print("| Multiplicación  (3)  |")
print("| Division        (4)  |")
print("|----------------------|")
print("")

op=int(input("Elige la operacion deseada "))
print("")
time.sleep(0.5)
print("Calculando...")
print("")
time.sleep(2)


if op<=0 :
    print("Error... Ingresa opcion del menú")

else:
    if op==1:
        suma=(variableOne+variableTwo)
        print(f"El resultado de la suma de los numeros {variableOne} y {variableTwo} es {suma} ") 
    elif op==2:
        resta=(variableOne-variableTwo)
        print(f"El resultado de la resta de los numeros {variableOne} y {variableTwo} es {resta} ")
    elif op==3:
        multiplicacion=(variableOne*variableTwo)  
        print(f"El resultado de la multiplicación de los numeros {variableOne} y {variableTwo} es {multiplicacion} ") 
    elif op==4:
        if  variableTwo<= 0:
            print("Error... Resultado indeterminado ")
        else:
         division=(variableOne/variableTwo)
         print(f"El resultado de la division de los numeros {variableOne} y {variableTwo} es {division} ") 
print(" ")
print("Gracias por usar nuestro software")
       
       
       
       
       
       
       
       
       
       

