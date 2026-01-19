class Usuarios:
    def __init__(self):
        self.cuentas = []

    def registrar_cuenta(self, cantidad):
        for _ in range(cantidad):
            id_c = input("ID Cuenta: ")
            nombre = input("Nombre del usuario: ")
            tipo = input("Tipo de cuenta: ")
            saldo = float(input("Saldo inicial: "))
            fecha = input("Fecha apertura: ")
            estado = input("Estado: ")

            usuario = {
                "id": id_c,
                "nombre": nombre,
                "tipo": tipo,
                "saldo": saldo,
                "fecha": fecha,
                "estado": estado
            }

            self.cuentas.append(usuario)

    def consultar(self):
        if not self.cuentas:
            print("No hay cuentas registradas.")
            return

        for i, cuenta in enumerate(self.cuentas, start=1):
            print(
                f"{i} - ID: {cuenta['id']}, "
                f"Nombre: {cuenta['nombre']}, "
                f"Tipo: {cuenta['tipo']}, "
                f"Saldo: {cuenta['saldo']}, "
                f"Estado: {cuenta['estado']}, "
                f"Fecha: {cuenta['fecha']}"
            )


class Banco:
    def __init__(self):
        self.usuarios = Usuarios()

    def abrir_cuenta(self):
        print("Bienvenido a la apertura de cuenta")
        cantidad = int(input("Ingrese la cantidad de cuentas que quiere crear: "))
        self.usuarios.registrar_cuenta(cantidad)

    def consultar_saldo(self):
        id_c = input("Ingrese el ID de la cuenta: ")

        for cuenta in self.usuarios.cuentas:
            if cuenta["id"] == id_c:
                print(f"Saldo actual: {cuenta['saldo']}")
                return

        print("Cuenta no encontrada.")


    def deposito(self):
        id_c = input("ID de la cuenta: ")
        monto = float(input("Monto a depositar: "))

        for cuenta in self.usuarios.cuentas:
            if cuenta["id"] == id_c:
                cuenta["saldo"] += monto
                print("Depósito realizado con éxito.")
                return
        print("Cuenta no encontrada.")

    def retiro(self):
        id_c = input("ID de la cuenta: ")
        monto = float(input("Monto a retirar: "))

        for cuenta in self.usuarios.cuentas:
            if cuenta["id"] == id_c:
                if cuenta["saldo"] >= monto:
                    cuenta["saldo"] -= monto
                    print("Retiro realizado con éxito.")
                else:
                    print("Fondos insuficientes.")
                return
        print("Cuenta no encontrada.")

    def cancelar_cuenta(self):
        id_c = input("ID de la cuenta a cancelar: ")
        for cuenta in self.usuarios.cuentas:
            if cuenta["id"] == id_c:
                cuenta["estado"] = "Cancelada"
                print("Cuenta cancelada.")
                return
        print("Cuenta no encontrada.")


class main:
    def __init__(self):
        self.banco = Banco()
        self.menu()

    def menu(self):
        while True:
            print("\nBienvenido a Mick's Bank")
            print("1- Abrir cuenta")
            print("2- Consultar Saldo")
            print("3- Deposito")
            print("4- Retiro")
            print("5- Cancelar cuenta")
            print("6- Consultar Cuentas")
            print("7- Salir")

            opcion = int(input("Opcion: "))

            match opcion:
                case 1:
                    self.banco.abrir_cuenta()
                case 2:
                    self.banco.consultar_saldo()
                case 3:
                    self.banco.deposito()
                case 4:
                    self.banco.retiro()
                case 5:
                    self.banco.cancelar_cuenta()
                case 6:
                    self.banco.usuarios.consultar()
                case 7:
                    print("Gracias por usar Mick's Bank")
                    break
                case _:
                    print("Opcion invalida")

if __name__ == "__main__":
    main()
