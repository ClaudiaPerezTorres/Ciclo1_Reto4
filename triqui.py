#{"4": "O", "6": "X", "2": "O", "5": "X", "3": "O"}
import json
#IMPRIMIR PIRAMIDE
def imprimirPiramide(a):
    # Primera Fila
    print("  {0}  ".format(a[0]))
    # Segunda Fila
    print(" {0}{1}{2} ".format(*a[1:4]))
    # Tercera Fila
    print("{0}{1}{2}{3}{4}".format(*a[4:9]))


#RELLENA LISTA  Y LA ORDENA 
def listaOrdenada(l):
  d=json.loads(l)
  arreglo=list(d.items())
  arreglo.sort(key = lambda t:t[0])
  for i in range(10):
    if int(arreglo[i][0]) != i:
      arreglo.insert(i,(i,"*"))
  arreglo.remove(arreglo[0])
  print(arreglo)
  imprimirPiramide(list(map(lambda t:t[1], arreglo)))

  if arreglo[0][1] == 'O' and arreglo[1][1]  == 'O' and arreglo[4][1] =='O':
    print("El Ganador es [O]")
  
  elif arreglo[0][1] == 'X' and arreglo[1][1]  == 'X' and arreglo[4][1] =='X':
    print("El Ganador es [X]")
  
  elif arreglo[0][1] == 'O' and arreglo[3][1]  == 'O' and arreglo[8][1] =='O':
    print("El Ganador es [O]")

  elif arreglo[0][1] == 'X' and arreglo[3][1]  == 'X' and arreglo[8][1] =='X':
    print("El Ganador es [X]")
  
  elif arreglo[0][1] == 'O' and arreglo[2][1]  == 'O' and arreglo[6][1] =='O':
    print("El Ganador es [O]")
  
  elif arreglo[0][1] == 'X' and arreglo[2][1]  == 'X' and arreglo[6][1] =='X':
    print("El Ganador es [X]")

  elif arreglo[4][1] == 'X' and arreglo[5][1]  == 'X' and arreglo[6][1] =='X':
    print("El Ganador es [X]")
    
  elif arreglo[4][1] == 'O' and arreglo[5][1]  == 'O' and arreglo[6][1] =='O':
    print("El Ganador es [O]")
  
  elif arreglo[6][1] == 'X' and arreglo[7][1]  == 'X' and arreglo[8][1] =='X':
    print("El Ganador es [X]")
  
  elif arreglo[6][1] == 'O' and arreglo[7][1]  == 'O' and arreglo[8][1] =='O':
    print("El Ganador es [O]")
  
  elif arreglo[5][1] == 'X' and arreglo[6][1]  == 'X' and arreglo[7][1] =='X':
    print("El Ganador es [X]")
  
  elif arreglo[5][1] == 'O' and arreglo[6][1]  == 'O' and arreglo[7][1] =='O':
    print("El Ganador es [O]")
  
  elif arreglo[1][1] == 'X' and arreglo[2][1]  == 'X' and arreglo[3][1] =='X':
    print("El Ganador es [X]")

  elif arreglo[1][1] == 'O' and arreglo[2][1]  == 'O' and arreglo[3][1] =='O':
    print("El Ganador es [O]")

  else:
    print("Sin Ganador [EMPATE]")


entrada =input(""" """)
listaOrdenada(entrada)