clave = "0414"
contraseña = input("ingrese su clave: ")
saldo = 3000000
if contraseña == clave:
    print ("clave correcta ")
    print ("menu transaccional")
    print ("1: cambiar clave")
    print ("2: mostrar saldo")
    print ("3: realizar retiro")
    print ("4: salir")
    opcion = input("digita una opcion:" " ")
    print(".: digite opcion ")
else :
    while contraseña  == clave :
        contraseña = input("ingrese su clave:")
        intentos += 1
        if intentos == 3 :
            print ("clave no valida,")
            break
if opcion == "1" :
    print("cambio de clave")
contraseña = ("ingrese suclave")
if opcion == "2" :
    print ("mostrar saldo")
saldo = print("su saldo es: ", saldo )
if opcion == "3" :
    print("submenu")
    print("1. $ 10000")
    print("2. $ 20000")
    print("3. $ 50000")
    print("4. $ 100000")
    print("5. $ 200000")
    print("6. $ 400000")
    print("7. $ 600000")
    print("8. $ 1000000")
    monto = input("digite el saldo a retirar: " " ")
    if monto == "1" :
        saldo = saldo - 10000
        print("retiro exitoso ")
    if monto == "2" :
        saldo = saldo - 20000
        print("retiro exitoso ")
    if monto == "3" :
        saldo = saldo - 50000
        print("retiro exitoso ")
    if monto == "4" :
        saldo = saldo - 100000
        print("retiro exitoso ")
    if monto == "5" :
        saldo = saldo - 200000
        print("retiro exitoso ")
    if monto == "6" :
        saldo = saldo - 400000
        print("retiro exitoso ")
    if monto == "7" :
        saldo = saldo - 600000
        print("retiro exitoso ")
    if monto == "8" :
        saldo = saldo - 1000000
        print("retiro exitoso ")
   
