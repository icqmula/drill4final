from clases import Vehiculo, Automovil

cantidad = int(input("¿Cuántos Vehículos desea insertar?: "))
instancias = []

for i in range(cantidad):
    
    print(f"Datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo del automóvil: ")
    numero_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    print("")
    auto = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
    instancias.append(auto)

print("Imprimiendo por pantalla los Vehículos:")

for index, item in enumerate(instancias):
        print(f"Datos del automóvil {index +1} : Marca {item.marca}, Modelo {item.modelo}, {item.numero_ruedas} ruedas, {item.velocidad} km/h, {item.cilindrada} cc")