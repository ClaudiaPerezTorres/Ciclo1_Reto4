# Ciclo1_Reto4
Triqui Piramidal. 
El triqui piramidal  se basa en el popular juego “tres en línea”, consiste en  vencer a un oponente  en un tablero de juego de 9 casillas  que se presentan   con una disposición   de pirámide.  Cada  casilla del  tablero  se encuentra identificada por in numero. 
   1
 234
56789
En el tablero  se van llenando paulatinamente las casillas  hasta   que uno de los 2 jugadores  con su carácter  seleccionado “x” o “o” haya    completado 
Triqui horizontal tres casillas 
Triqui vertical tres casillas
Triqui diagonal  de izquierda a derecha, tres casillas
Triqui diagonal  de derecha a izquierda, tres casillas
Nota 1. No se puede ocupar  una casilla  del tablero  9ya ocupada  por una jugada previa. 
Nota 2. Si no hay un ganador  y se acaban las casillas  del tablero  se declara un empate
Objetivo. Escribir un programa en Python  que reciba una única entrada  que representa  el transcurso de un juego  en formato JSON  en  donde  cada índice  representa  la casilla del  tablero  y su valor  el  carácter   que la ocupa. A partir de  dicha entrada:
1.	Imprima el tablero de juego  con el juego descrito. Cada   fila del  tablero  debe tener el carácter  cada   casilla. Las  casillas   que no han sido ocupadas  deben ser representadas   por el carácter *
2.	Imprima la cadena “El ganador es [n]  donde  n es el carácter   correspondiente.   En caso de no haber  ganador  debe imprimir  la cadena “Sin ganador {EMPATE”
