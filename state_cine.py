import sys

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.funciones=[]

class Cine:
    def __init__(self,nombre):
        self.nombre= nombre
        self.lista_peliculas = []
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


class CineFactory:
    def obtener_cine(self, cine):
        if cine == '1':
            peliculaIT = Pelicula(1, 'IT')
            peliculaHF = Pelicula(2, 'La Hora Final')
            peliculaD = Pelicula(3, 'Desparecido')
            peliculaDeep = Pelicula(4, 'Deep El Pulpo')

            peliculaIT.funcion = ['19:00', '20.30', '22:00']
            peliculaHF.funcion = ['21:00']
            peliculaD.funcion = ['20:00', '23:00']
            peliculaDeep.funcion = ['16:00']

            cinePlaneta= Cine("Cine Planeta")
            cinePlaneta.lista_peliculas.append(peliculaIT)
            cinePlaneta.lista_peliculas.append(peliculaHF)
            cinePlaneta.lista_peliculas.append(peliculaD)
            cinePlaneta.lista_peliculas.append(peliculaDeep)

            return cinePlaneta

        elif cine == '2':
            peliculaD = Pelicula(1, 'Desparecido')
            peliculaDeep = Pelicula(2, 'Deep El Pulpo')

            peliculaD.funcion = ['20:00', '23:00']
            peliculaDeep.funcion = ['16:00']

            cineStark = Cine("Cine Stark")

            cineStark.lista_peliculas.append(peliculaD)
            cineStark.lista_peliculas.append(peliculaDeep)

            return cineStark()
        else:
            return None


class EstadoCliente:
    def __init__(self, cliente):
        self.cliente = cliente

    def ejecutar(self):
        pass


class EstadoPorIniciar(EstadoCliente):
    def ejecutar(self):
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if(opcion==1):
            self.cliente.estado=EstadoListarCine(self)
        elif(opcion==2):
            self.cliente.estado=EstadoListarCartelera(self)
        elif(opcion==3):
            self.cliente.estado=EstadoComprarEntrada(self)
        elif(opcion==0):
            self.cliente.estado=EstadoAtendido(self)

        return False

class EstadoListarCine(EstadoCliente):
    def ejecutar(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        self.cliente.estado=EstadoPorIniciar(self)
        return True
class EstadoListarCartelera(EstadoCliente):
    def ejecutar(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        factory = CineFactory()

        cine = input('Primero elija un cine:')

        cine = factory.obtener_cine(cine)

        peliculas = cine.listar_peliculas()
        print('********************')
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')
        self.cliente.estado=EstadoPorIniciar(self)
        return True
class EstadoComprarEntrada(EstadoCliente):
    def ejecutar(self):

        print('********************')
        print('COMPRAR ENTRADA')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        cine = input('Primero elija un cine:')
        factory = CineFactory()
        cine = factory.obtener_cine(cine)
        peliculas = cine.listar_peliculas()
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        pelicula_elegida = input('Elija pelicula:')
        # pelicula = obtener_pelicula(id_pelicula)
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in cine.listar_funciones(pelicula_elegida):
            print('Función: {}'.format(funcion))
        funcion_elegida = input('Funcion:')
        cantidad_entradas = input('Ingrese cantidad de entradas: ')
        codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
        print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        self.cliente.estado=EstadoAtendido(self)
        return True
class EstadoAtendido(EstadoCliente):
    def ejecutar(self):
        return False
class Cliente:
    def __init__(self):
        self.estado = EstadoPorIniciar(self)

def main():
    terminado = False;
    cliente = Cliente()
    while not terminado:

        terminado=cliente.estado.ejecutar()

if __name__ == '__main__':
    main()