#Tarea 3

Moran Merino Marcos Anthony 20132982 amoran961

- Se adjunta un MD con la explciación de los 3 proncipios SOLID.

- Se tienen 4 archicos .py 

 1. factory_cine.py: Se usó este patrón debido a que se estaban creando dos clases cine de manera innecesaria. Por ello

se creó una sola clase cine y se usó una clase factory para esponer los cines cuando se los requiera.

 2. singleton_cine.py: Se consideró que el factory cine sólo debería ser instanciado una vez.

 3. state_cine.py: Se simplificó la interacción del usuario mediante estados. Se ajusta al caso porque el proceso de
compra presenta varios estados, por ejmplo: en menú principal, listando cine, etc.

 4. factory_cine_sql_lite.py: La misma lógica del factory, pero usando una base de datos SQL Lite