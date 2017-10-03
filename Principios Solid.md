# Principios Solid

## 1. Principio Open/Closed: 

Se viola este principio debido a que se crean dos clases Cine, ambas tienen caracter�sticas en com�n por lo que 
la duplicaci�n de c�digo es innecesaria. Asimismo, nuevas funcionalidades implicar�an la modificaci�n de la clase, para solucionar este 
problema la mejor opci�n ser�a al aplicaci�n de la herencia.

## 2.Principio de responsabilidad �nica: 

Dentro de las clases cine se declaran los m�todos listar_peliculas, listar_funciones y  guardar_entrada. Estos m�todos 
corresponden a la l�gica de la aplicaci�n mas no a la de la clase.

## 3.Dependency Inversion: 

Las clases Cine dependen de las clases pel�cula y entrada, las cuales se encuentran instanciadas en su constructor. En caso se desee agregar
nuevas pel�culas o modificar las existentes, ser�a necesario modificar dicho c�digo.