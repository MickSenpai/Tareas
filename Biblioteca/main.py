class Usuarios:
    def __init__(self):
        self.cuentas = []

    def registrar_cuenta(self, cantidad):
        self.cantidad = cantidad
        
        for x in range(self.cantidad):
            id_c = input("ID Cuenta: ")
            nombre = input("Nombre del usuario: ")
            tipo = input("Tipo de cuenta: ")
            saldo = input("Saldo inicial: ")
            fecha = input("Fecha apertura: ")
            estado = input("Estado: ")

            usuario = f"ID Cuenta: {id_c}, Nombre: {nombre}, Tipo de cuenta: {tipo}, Saldo: {saldo}, Estado de la cuenta: {estado}, Fecha de Apertura: {fecha}"

            self.cuentas.append(usuario)

    def consultar_cuentas(self):
        for i in range(len(self.cuentas)):
            print(f"{i + 1} - {self.cuentas[i]}")
    

class Banco:
    def __init__(self):
        pass

    def abrir_cuenta(self):
        print("Bienvenido a la apertura de cuenta")
        self.cantidad = int(input("Ingrese la cantidad de cuentas que quiere crear: "))

        Usuarios().registrar_cuenta(self.cantidad)

    def consultar_saldo(self):
        pass

    def deposito(self):
        pass

    def retiro(self):
        pass

    def cancelar_cuenta(self):
        pass

class main:
    def __init__(self):
        thiscuentas = Banco()
        thisuser = Usuarios()

        thiscuentas.abrir_cuenta()

        print(thisuser.consultar_cuentas())
        
if __name__ == "__main__":
    main()