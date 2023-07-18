import csv
class Vehiculo():
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def guardar_datos_csv(self):
        datos = [str(self.__class__), str(self.__dict__)]
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow(datos)
        except IOError as e:
            print(f"Error al guardar los datos en el archivo: {e}")
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_ruedas} ruedas"
    
    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehiculos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print(item[1])
        except IOError as e:
            print(f"Error al leer los datos del archivo: {e}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{Vehiculo.__str__(self)} , {self.velocidad} km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.puestos = puestos

    def get_puestos(self):
        return self.puestos
    
    def set_puestos(self, puestos_new):
        self.puestos = puestos_new

    def __str__(self):
        return f"{Automovil.__str__(self)} , Puestos: {self.puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{Automovil.__str__(self)} , Carga: {self.carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"{Vehiculo.__str__(self)} , Tipo: {self.tipo_bicicleta}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{Bicicleta.__str__(self)}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"