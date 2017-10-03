# Principios Solid

## 1. Principio Open/Closed: 

Se viola este principio debido a que se crean dos clases Cine, ambas tienen características en común por lo que 
la duplicación de código es innecesaria. Asimismo, nuevas funcionalidades implicarían la modificación de la clase, para solucionar este 
problema la mejor opción sería al aplicación de la herencia.

## 2.Principio de responsabilidad única: 

Dentro de las clases cine se declaran los métodos listar_peliculas, listar_funciones y  guardar_entrada. Estos métodos 
corresponden a la lógica de la aplicación mas no a la de la clase.

## 3.Dependency Inversion: 

Las clases Cine dependen de las clases película y entrada, las cuales se encuentran instanciadas en su constructor. En caso se desee agregar
nuevas películas o modificar las existentes, sería necesario modificar dicho código.