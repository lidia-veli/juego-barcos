from clases import Case
from clases.Case import *
from clases.Barco import *
from clases import Conventions
from clases.Conventions import *

  
# performance / legibilidad:
num_lineas = tablero_num_lineas
num_columnas = tablero_num_columnas
num2l = generar_num_linea
num2c = generar_num_columna


def __init__(self):
  # Creamos las casillas:
  generar_casillas() # viene de Case
  # Creamos los barcos:
  generar_barcos(self) # viene de Barco
  
  # Creamos la herramienta para poder seguir la situación
  self.casillas_jugadas = set()
  self.casillas_tocadas = set()
  self.casillas_hundidas = set()
  self.casillas_agua = set()
  self.casillas_ocupadas = set()
  self.casillas_libres = set()
  self.casillas_libres.update(Case.instances.values())
  
  # Generamos aquí los etiquetas para facilitar la visualización
  self.etiqueta_lineas = [num2l(x) for x in range(num_lineas)]
  self.etiqueta_columnas = [num2c(x) for x in range(num_columnas)]
  
  trazo_horizontal = " --" + "+---" * 10 + "+"


@classmethod
def ver(self):
  print("   |", " | ".join(self.etiqueta_columnas), "|")
  
  iter_etiqueta_lineas = iter(self.etiqueta_lineas)
  
  for x, y in product(range(Conventions.tablero_num_lineas),
                      range(Conventions.tablero_num_columnas)):
  
      # Trazo horizontal para cada nueva línea
      if y == 0:
          print(trazo_horizontal)
          print(" {}".format(next(iter_etiqueta_lineas)), end="")
  
      casilla = Case.instances[x, y]
      print(" |", casilla, end="")
  
      # Ver la barra vertical derecha de la tabla:
      if y == 9:
          print(" |")
  # Ver la última línea horizontal
  print(self.trazo_horizontal + "\n\n")




