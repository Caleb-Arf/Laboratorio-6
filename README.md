# Callbacks en Python
Para el enunciado referente a callbacks en python se editó los dos archivos brindados por la profesora. Primeramente no se realizaron cambios en el el archivo EventManager.py ya que este proporcionaba las funciones necesarias para el correcto funcionamiento del programa, posteriormente se importó de EventManager.py la clase EventManager al archivo datamanager.py, donde se tiene la clase RealTimeDataManager donde se añadió una variable en el método de iniciación de la clase que naturalmente se encuentra en False y además se crea una instancia de la clase EventManager en la clase RealTimeDataManager.

La variable llamada stop_data es la condición necesaria del bucle while que inicia las actualizaciones de datos en tiempo real, que además llama a la función que genera datos aleatorios de temperatura y humedad, posteriormente se encuentra el módulo ejecutable donde se define y se suscribe la función de data_update que tiene como función imprimir los datos que se encuentran en el diccionario "data".

Por último se genera el thread para realizar las actualizaciones de la información y se inicia la actualización de los datos, y finalmente se tiene un try except en el cual si se ejecuta el KeyboardInterrupt como shortcut del teclado imprime que el programa ha terminado, y la función .join() evita que queden datos sueltos después de imprimir el mensaje "Programa terminado".

# Funciones Lambda en Python
El código proporcionado calc.py se editó para utilizar funciones lambda en la función de calc_operation donde se revisa que tipo de operación se desea realizar y se ejecuta una función lambda que cumple con la operación a realiar, además en la función ejecutar_opreación se utilizó como parámetro una función callback en la que se realiza la operación deseada por el usuario.

En la función main se define un bucle while en el cual se lee constantemente la entrada proporcionada por el usuario mediante el uso de la función get_user_input que lee la entrada al programa donde se le solicita al usuario dos número en formato float y un operador que corresponda al tipo de operación a realizar entre los dos números proporcionados, cuando se obtiene la entrada del usuario esta se guarda en una lista llamada user_input, luego se clasifica la entrada proporcionada, si se proporcionó "exit" en el espacio correspondiente a operación entonces se rompe el ciclo y el programa termina, si no entonces se procesa la operación a realizar y si esta es válida entonces se procede a calcular el resultado, si no es válida entonces se le dice al usuario que digite una opción válida o que en su defecto se cierre el programa, finalmente se ejecuta main en el módulo ejecutable.

# Ejemplos de los resultados obtenidos
## Callbacks en Python 
En este caso se obtuvieron las salidas: 
  1. PS C:\Users\c4leb\.vscode\python\Pruebas> python -u "c:\Users\c4leb\.vscode\python\Pruebas\datamanager.py"
   
   Datos en tiempo real actualizados: {'temperatura': 24.503336252926577, 'humedad': 58.55561934231239}

   Datos en tiempo real actualizados: {'temperatura': 24.86942574751851, 'humedad': 59.735507041396275}
   
   Datos en tiempo real actualizados: {'temperatura': 25.055239439413278, 'humedad': 59.1039008906405}
   
   Datos en tiempo real actualizados: {'temperatura': 25.09428882264794, 'humedad': 58.907983514597134}

   Programa terminado.
   
  2. PS C:\Users\c4leb\.vscode\python\Pruebas> python -u "c:\Users\c4leb\.vscode\python\Pruebas\datamanager.py"

   Datos en tiempo real actualizados: {'temperatura': 24.880214946962735, 'humedad': 60.88190002581447}

   Datos en tiempo real actualizados: {'temperatura': 24.667256688492557, 'humedad': 60.833266138622285}
   
   Datos en tiempo real actualizados: {'temperatura': 24.33768537453754, 'humedad': 62.793167960973854}


   Programa terminado.

## Funciones Lambda en Python
para este enunciado se obtuvieron los siguientes salidas:

  1. PS C:\Users\c4leb\.vscode\python\Pruebas> python -u "c:\Users\c4leb\.vscode\python\Pruebas\calc.py"
     
   Ingrese un numero: 10

   Ingrese otro numero: 10
   
   Elija una operacion (+, -, *, /) o escriba 'exit' para salir: -

   Calculando...
   
   Resultado: 0.0
   
  2. PS C:\Users\c4leb\.vscode\python\Pruebas> python -u "c:\Users\c4leb\.vscode\python\Pruebas\calc.py"
     
   Ingrese un numero: 100
   
   Ingrese otro numero: 50
   
   Elija una operacion (+, -, *, /) o escriba 'exit' para salir: *
   

   Calculando...

   Resultado: 5000.0
   
  3. PS C:\Users\c4leb\.vscode\python\Pruebas> python -u "c:\Users\c4leb\.vscode\python\Pruebas\calc.py"
     
   Input invalido. Por favor ingrese numeros.
   
   Ingrese un numero: 15
   
   Ingrese otro numero: 25
   
   Elija una operacion (+, -, *, /) o escriba 'exit' para salir: -
   

   Calculando...
   
   Resultado: -10.0
   

   
