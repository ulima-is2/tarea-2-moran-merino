#Tarea 3

Moran Merino Marcos Anthony 20132982 amoran961

- Se adjunta un MD con la explciaci�n de los 3 proncipios SOLID.

- Se tienen 4 archicos .py 

 1. factory_cine.py: Se us� este patr�n debido a que se estaban creando dos clases cine de manera innecesaria. Por ello

se cre� una sola clase cine y se us� una clase factory para esponer los cines cuando se los requiera.

 2. singleton_cine.py: Se consider� que el factory cine s�lo deber�a ser instanciado una vez.

 3. state_cine.py: Se simplific� la interacci�n del usuario mediante estados. Se ajusta al caso porque el proceso de
compra presenta varios estados, por ejmplo: en men� principal, listando cine, etc.

 4. factory_cine_sql_lite.py: La misma l�gica del factory, pero usando una base de datos SQL Lite