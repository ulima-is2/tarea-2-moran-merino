import sys
import sqlite3

class Conector():
    def __init__(self,dbname):
        self.dbname=dbname
        self.conn = sqlite3.connect(self.dbname)
    def getCursor(self):
        cursor=self.conn.cursor()
        return cursor
    def close(self):
        self.conn.close()
    def cargar_datos(self):
        self.getCursor().execute('''CREATE TABLE tb_cine
                            (id text, nombre text)''')
        self.getCursor().execute('''CREATE TABLE tb_pelicula
                    (id text, nombre text)''')
        self.getCursor().execute('''CREATE TABLE tb_funcion
                            (id text,pelicula text, cine text,horario text)''')
        self.getCursor().execute('''CREATE TABLE tb_entrada
                                    (id text, funcion text, cantidad int)''')

        cines = [('1', 'CinePlaneta'), ('2', 'CineStark' )]

        self.getCursor().executemany('INSERT INTO tb_cine VALUES (?,?)', cines)

        peliculas=[('1', 'IT'), ('2', 'La Hora Final' ),('3', 'Desaparecido'),('4', 'Deep el Pulpo')]
        self.getCursor().executemany('INSERT INTO tb_cine VALUES (?,?)', peliculas)

        funciones=[("1","1","1","19:00"),("2","1","1","20:30"),("3","1","1","22:00"),("4","2","1","21:00"),
                   ("5","3","1","20:00"),("6","3","1","23:00"),("7","4","1","16:00"),("8","3","2","21:00"),("9","4","2","21:00")]
        self.getCursor().executemany('INSERT INTO tb_cine VALUES (?,?)', peliculas)

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
        self.c = Conector.getCursor()

    def cargar_funciones(self):
        t = (self.nombre,)
        funciones = self.c.execute('SELECT f.horario FROM tb_funcion f INNER JOIN tb_pelicula p ON c.id=f.pelicula WHERE p.nombre=?', t)


class Cine:
    def __init__(self,nombre):
        self.nombre= nombre
        self.lista_peliculas = []
        self.entradas = []
        self.c=Conector.getCursor()

    def listar_peliculas(self):
        t = (self.nombre,)
        self.lista_peliculas =self.c.execute('SELECT p.nombre FROM tb_funcion f INNER JOIN tb_cine c on f.cine=c.id INNER JOIN tb_pelicula p on f.pelicula = p.id  WHERE c.nombre=?', t)
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):

        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        entrada=[(id_pelicula_elegida,funcion_elegida,cantidad)]
        self.c.executemany('INSERT INTO tb_cine VALUES (?,?)', entrada)
        return len(self.entradas)

class CineFactory:
    def obtener_cine(self, cine):
        con = Conector('CineDB')
        cur=con.getCursor()



        if cine == '1':
            peliculaIT = Pelicula(1, 'IT')
            peliculaHF = Pelicula(2, 'La Hora Final')
            peliculaD = Pelicula(3, 'Desparecido')
            peliculaDeep = Pelicula(4, 'Deep El Pulpo')

            peliculaIT.funcion = ['19:00', '20:30', '22:00']
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

            return cineStark
        else:
            return None
def main():
    factory= CineFactory()

    terminado = False;
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

            cine = input('Primero elija un cine:')

            cine=factory.obtener_cine(cine)

            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            cine = input('Primero elija un cine:')
            cine = factory.obtener_cine(cine)
            peliculas = cine.listar_peliculas()
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()