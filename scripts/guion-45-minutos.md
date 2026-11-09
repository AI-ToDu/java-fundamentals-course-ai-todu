# Guion de producción: Aprende Java creando una mascota virtual

**Montaje previsto: 45:00.** Seis capítulos. Los tiempos incluyen voz, demostraciones y pausas.

Los tiempos de voz son orientativos. Para la duración de los archivos y la ubicación de los clips consulta la guía de montaje. Los 45 minutos corresponden al video previsto.

Las indicaciones de pantalla son para producción y no se leen. Todos los programas se demuestran en un editor Java en línea. El tiempo sin voz se utiliza para escribir, ejecutar, leer resultados y practicar; no para congelar imágenes.

## Capítulo 1. Tu primer programa

### 01-01 · 00:00–01:00 · Bienvenida y objetivo

**En pantalla:** Abre completed-examples/01/Main.java en el editor Java del navegador. Muestra la consola y adelanta brevemente la salida del proyecto final; vuelve al ejemplo 1.

**Narración:** ¿Te gustaría crear una mascota que tenga nombre, energía y acciones propias? En este curso vamos a construirla con Java. Empezaremos con un mensaje en pantalla y avanzaremos paso a paso hasta manejar varias mascotas. No necesitas saber programar. Programar consiste en escribir instrucciones precisas para que una computadora realice una tarea. Java es un lenguaje que permite expresar esas instrucciones y se utiliza para crear muchos tipos de aplicaciones. Hoy construiremos un programa de consola: nos comunicaremos con él mediante texto. Solo necesitas tu navegador y ganas de probar.

**Tiempo de escena:** 60 s. Voz orientativa: 43.2 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 01-02 · 01:00–02:00 · Preparar el editor en línea

**En pantalla:** Muestra JDoodle, selecciona Java y una versión 17 o posterior. Pega el ejemplo 1. Señala editor, entrada y salida sin activar asistentes de IA.

**Narración:** Abre el editor Java que aparece en los recursos de esta lección. En él encontrarás un espacio para escribir el programa, una opción para ejecutarlo y una zona donde aparecerá el resultado. El navegador envía el código a una computadora que tiene Java preparado y nos devuelve la salida. Por eso no necesitamos instalar herramientas. Copia el primer ejemplo y conserva el nombre de la clase: Main. Si ya hay otro programa, reemplázalo por completo para evitar mezclar dos ejemplos. Ubica la opción de ejecutar y la zona de salida. En unos segundos las utilizaremos.

**Reserva de práctica:** 8 segundos sin narración. Insertar la pausa después de «En unos segundos las utilizaremos.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 60 s. Voz orientativa: 45.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 01-03 · 02:00–03:00 · Leer la estructura inicial

**En pantalla:** Amplía el código a tamaño legible. Resalta public class Main, main y las llaves; después resalta solo las dos instrucciones println.

**Narración:** Observa la estructura del programa. La primera línea declara una clase llamada Main. Dentro aparece un método llamado main, que será el punto de entrada de estos ejemplos. No necesitas memorizar ahora todas las palabras que lo acompañan. Conservaremos esa estructura mientras aprendemos. Las llaves agrupan instrucciones: una pareja delimita la clase y otra delimita el método. Dentro escribimos dos instrucciones que muestran mensajes. Cada una termina con punto y coma. Las comillas indican dónde empieza y termina el texto. Los espacios y la sangría nos ayudan a ver qué instrucciones pertenecen al mismo bloque.

**Tiempo de escena:** 60 s. Voz orientativa: 45.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 01-04 · 03:00–04:00 · Ejecutar y corregir un error

**En pantalla:** Ejecuta y muestra las dos líneas. Quita solo el punto y coma del primer println, ejecuta, señala el error y restáuralo antes de continuar.

**Narración:** Pulsa ejecutar. La consola muestra primero Hola, mundo y después el segundo mensaje. El programa siguió el orden de nuestras instrucciones. Ahora quitaremos un punto y coma para ver un error frecuente. Al ejecutar, Java detecta un problema y nos da información para localizarlo. Un error no significa que no puedas programar: significa que tenemos algo concreto que revisar. Busca la línea indicada y observa también la línea anterior. Recupera el punto y coma y ejecuta otra vez. Cuando cambies un programa, comprobar su resultado es tan importante como escribirlo.

**Tiempo de escena:** 60 s. Voz orientativa: 43.2 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 01-05 · 04:00–05:00 · Primer reto y cierre

**En pantalla:** Abre starter-files/01/Main.java. Mantén el reto visible 20 segundos. Después agrega el segundo println de la solución y ejecuta.

**Narración:** Tu primer reto es cambiar el mensaje y agregar una segunda instrucción para presentar a tu futura mascota. Puedes escribir: Mi mascota se llama Luna. Conserva las comillas, los paréntesis y el punto y coma. Tienes un momento para intentarlo; si necesitas más tiempo, pausa el video. Al ejecutar deberías ver dos líneas. Ya sabes abrir un editor, modificar instrucciones y comprobar la salida. Ahora vamos a guardar información para que el programa pueda trabajar con ella.

**Reserva de práctica:** 20 segundos sin narración. Insertar la pausa después de «si necesitas más tiempo, pausa el video.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 60 s. Voz orientativa: 37.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Capítulo 2. Datos y operaciones

### 02-01 · 05:00–06:10 · Variables y tipos

**En pantalla:** Abre completed-examples/02/Main.java. Señala nombre, energia, comida, costoDeJugar, peso y tieneHambre. Relaciona cada tipo con su valor.

**Narración:** Una variable nos permite guardar un dato y darle un nombre para utilizarlo después. Nuestra mascota necesita un nombre y una cantidad de energía. String representa texto, por eso Luna va entre comillas. El tipo int representa números enteros, como cuarenta o veinte. El tipo double permite representar números con parte decimal, como el peso de tres punto cinco. En el código usamos punto para escribir ese decimal. El tipo boolean representa uno de dos valores: verdadero o falso. Elegir el tipo ayuda a expresar qué dato esperamos. El nombre de cada variable debe explicar su propósito.

**Tiempo de escena:** 70 s. Voz orientativa: 46.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 02-02 · 06:10–07:20 · Asignación y lectura de variables

**En pantalla:** Resalta int energia = 40 y luego energia + comida. Cambia temporalmente energia a 50, ejecuta y vuelve a 40. Muestra que el nombre no lleva comillas al usar la variable.

**Narración:** Lee esta declaración de izquierda a derecha: necesitamos un entero, lo llamamos energía y le asignamos el valor cuarenta. El signo igual guarda el valor de la derecha en la variable de la izquierda. No pregunta si dos cosas son iguales; más adelante usaremos una comparación para eso. Cuando escribimos el nombre de una variable sin comillas, usamos el dato que contiene. Si ponemos ese nombre entre comillas, obtenemos solamente el texto. Podemos cambiar el valor inicial y volver a ejecutar. Observa que los cálculos se actualizan porque usan las variables. No es necesario reescribir cada resultado a mano.

**Tiempo de escena:** 70 s. Voz orientativa: 47.5 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 02-03 · 07:20–08:30 · Operaciones con energía

**En pantalla:** Muestra las expresiones energia + comida y energiaDespuesDeComer - costoDeJugar. Predice 60 y 45, ejecuta y relaciona salida con cada expresión.

**Narración:** Los operadores nos permiten combinar valores. Si la energía empieza en cuarenta y la comida aporta veinte, una suma produce sesenta. Guardamos ese resultado en otra variable. Después restamos quince para representar el costo de jugar y obtenemos cuarenta y cinco. Antes de ejecutar, intenta calcular los resultados tú mismo. Así puedes comprobar si el programa hace lo que esperabas. También podemos multiplicar: el asterisco representa la multiplicación y nos permite calcular el doble de una cantidad. Una expresión es una combinación de valores y operadores que produce un resultado. Usaremos expresiones tanto para calcular como para tomar decisiones.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «Antes de ejecutar, intenta calcular los resultados tú mismo.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 47.5 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 02-04 · 08:30–09:40 · División entera y decimal

**En pantalla:** Resalta las dos últimas instrucciones. Ejecuta 5 / 2 y 5.0 / 2; señala 2 y 2.5. Mantén visibles los paréntesis de las expresiones.

**Narración:** La división merece atención. Cuando dividimos dos enteros, como cinco entre dos, Java realiza una división entera y el resultado es dos. La parte fraccionaria no aparece en ese resultado. Si uno de los valores es decimal, como cinco punto cero, la división produce dos punto cinco. No son resultados contradictorios: dependen de los tipos que participan. Los paréntesis ayudan a indicar qué operación queremos resolver primero y a mostrarla claramente dentro de un mensaje. Si un resultado te sorprende, revisa los valores y sus tipos antes de cambiar todo el programa. Esa costumbre evitará muchos errores.

**Tiempo de escena:** 70 s. Voz orientativa: 46.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 02-05 · 09:40–10:50 · Comparaciones y mensajes

**En pantalla:** Muestra energia < 50 y la salida Tiene hambre: true. Cambia el valor inicial a 70 para obtener false y restáuralo. Señala el + entre texto y variables.

**Narración:** La expresión energía menor que cincuenta produce un booleano. Con energía cuarenta, la comparación es verdadera; con energía setenta, es falsa. En la consola verás las palabras true y false, que son los valores de Java. Para comparar números también existen mayor que, menor o igual y doble igual. Recuerda: un igual asigna, dos iguales comparan. El signo más también puede unir texto y datos en un mensaje. En Nombre más la variable nombre, construye una frase. Mira el contexto para distinguir una suma numérica de una unión de texto. En ambos casos podemos predecir la salida antes de ejecutar.

**Tiempo de escena:** 70 s. Voz orientativa: 48.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 02-06 · 10:50–12:00 · Reto de variables

**En pantalla:** Abre starter-files/02/Main.java. Mantén el reto 25 segundos. Completa energiaFinal = energia + comida - 15 y muestra el resultado; deja claro que aún no se aplican límites de energía.

**Narración:** Ahora cambia el nombre de la mascota y calcula su energía después de comer y jugar. Empieza con cuarenta, suma veinte y resta quince. Agrega también una variable decimal para el peso. Pausa si necesitas más tiempo. Compara tu respuesta con la solución: la energía final es cuarenta y cinco. En este ejemplo todavía no limitamos la energía a cien; agregaremos esa regla cuando construyamos la clase. Ya sabemos guardar datos y calcular. El siguiente paso es elegir qué instrucciones ejecutar según esos datos.

**Reserva de práctica:** 25 segundos sin narración. Insertar la pausa después de «Pausa si necesitas más tiempo.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 40.3 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Capítulo 3. Decisiones y repeticiones

### 03-01 · 12:00–13:10 · Elegir con if

**En pantalla:** Abre completed-examples/03/Main.java. Señala la condición energia < 50 y el bloque if. Ejecuta con 40 y relaciona el primer mensaje con la condición.

**Narración:** Una decisión permite que el programa responda a una situación. Si la mascota tiene menos de cincuenta puntos de energía, mostraremos que necesita comer. La palabra if introduce esa decisión y dentro de los paréntesis escribimos una condición. Si la condición es verdadera, se ejecutan las instrucciones entre las llaves que siguen. Con energía cuarenta, el mensaje aparece porque cuarenta es menor que cincuenta. Observa que la condición utiliza una comparación, no una asignación. El bloque puede contener una instrucción o varias. La sangría nos ayuda a reconocer cuáles pertenecen a esa decisión.

**Tiempo de escena:** 70 s. Voz orientativa: 44.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 03-02 · 13:10–14:20 · La alternativa else y el límite

**En pantalla:** Cambia energia a 70 y ejecuta para mostrar else. Prueba 50, explica la frontera y restaura 40 para continuar con los bucles.

**Narración:** La palabra else indica qué hacer cuando la condición anterior es falsa. Si la energía no es menor que cincuenta, mostraremos que la mascota puede jugar. Prueba mentalmente con setenta: ¿qué mensaje esperas? Ahora piensa en cincuenta exactamente. Como cincuenta no es menor que cincuenta, también se ejecuta la alternativa. Si quisiéramos incluir el cincuenta entre los valores que necesitan comida, cambiaríamos la comparación a menor o igual. Los valores que están justo en el límite son buenos casos de prueba. Nos ayudan a comprobar si nuestra regla expresa lo que realmente queremos.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «¿qué mensaje esperas?» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 44.6 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 03-03 · 14:20–15:30 · Repetir con for

**En pantalla:** Resalta for (int paso = 1; paso <= 3; paso++). Señala inicio, condición y actualización por separado; muestra las tres líneas de salida.

**Narración:** Cuando una tarea se repite, podemos usar un bucle. Este for muestra tres pasos. Tiene tres partes: comienza con una variable llamada paso que vale uno; continúa mientras paso sea menor o igual que tres; y después de cada vuelta aumenta paso en uno. La expresión paso más más es una forma breve de hacer ese aumento. El cuerpo del bucle contiene el mensaje que se repite. No escribimos tres instrucciones casi iguales: escribimos una instrucción y explicamos cuántas veces debe repetirse. Este tipo de bucle resulta útil cuando conocemos la cantidad o el intervalo que queremos recorrer.

**Tiempo de escena:** 70 s. Voz orientativa: 47.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 03-04 · 15:30–16:40 · Seguir un bucle paso a paso

**En pantalla:** Sobre el mismo código, señala paso = 1, luego 2, 3 y 4 con anotaciones simples. Relaciona 1, 2 y 3 con las salidas; 4 con condición falsa.

**Narración:** Vamos a seguir el recorrido sin prisa. Primero paso vale uno y la condición es verdadera, así que se muestra Paso uno. Después aumenta a dos y se repite el proceso. Con tres todavía cumple la condición y aparece el tercer mensaje. Luego aumenta a cuatro. Cuatro ya no es menor o igual que tres y el bucle termina. Aunque el último valor revisado fue cuatro, solo imprimimos uno, dos y tres. Antes de ejecutar un bucle, anota los valores que tendrá su variable. Seguir un ejemplo pequeño suele ser más claro que intentar comprender muchas repeticiones a la vez.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «Antes de ejecutar un bucle, anota los valores que tendrá su variable.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 48.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 03-05 · 16:40–17:50 · Repetir con while

**En pantalla:** Señala while (energia < 60). Con energia inicial 40, muestra los estados 40, 50 y 60. No ejecutes un bucle al que se haya quitado la actualización.

**Narración:** El bucle while repite su bloque mientras una condición sea verdadera. Aquí seguimos alimentando a la mascota mientras su energía sea menor que sesenta. Empieza en cuarenta. La primera vuelta suma diez y muestra cincuenta. La segunda suma diez y muestra sesenta. Al revisar otra vez, la condición es falsa y terminamos. La actualización de energía es importante: permite avanzar hacia el final. Si la energía nunca cambiara, la condición seguiría siendo verdadera y tendríamos un bucle infinito. No hace falta ejecutarlo para reconocer ese problema. Primero debemos explicar qué dato cambia y por qué el bucle va a detenerse.

**Tiempo de escena:** 70 s. Voz orientativa: 48.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 03-06 · 17:50–19:00 · Reto de decisiones y bucles

**En pantalla:** Mantén el reto 25 segundos: predecir for con paso <= 4 y while con energia inicial 60. Luego realiza ambos cambios, ejecuta y restaura el ejemplo.

**Narración:** Tu reto tiene dos partes. Cambia el for para mostrar cuatro pasos. Después imagina que la energía comienza en sesenta: ¿cuántas veces entrará al while? Tómate un momento o pausa el video. El for debe mostrar cuatro líneas. El while no entra ninguna vez, porque su condición ya es falsa desde el inicio. Un bucle puede ejecutarse cero veces. Ya podemos decidir y repetir. Ahora organizaremos tareas con métodos para que nuestro programa resulte más fácil de entender y reutilizar.

**Reserva de práctica:** 25 segundos sin narración. Insertar la pausa después de «Tómate un momento o pausa el video.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 38.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Capítulo 4. Metodos y entrada de datos

### 04-01 · 19:00–20:10 · Separar tareas en métodos

**En pantalla:** Abre completed-examples/04/Main.java. Contrae visualmente main y señala saludar y calcularEnergia como métodos dentro de la clase Main.

**Narración:** Un método agrupa instrucciones para realizar una tarea. En vez de reunir todo dentro del método principal, podemos separar acciones y darles nombres claros. Aquí tenemos un método para saludar y otro para calcular energía. Declarar un método describe lo que hará; llamarlo indica que queremos realizar esa tarea en ese momento. Los métodos de este ejemplo están dentro de la clase Main, al mismo nivel que main. No van dentro del cuerpo de otro método. Usamos static para llamarlos directamente desde main en este ejemplo. Más adelante veremos métodos que pertenecen a cada objeto de nuestra clase Mascota.

**Tiempo de escena:** 70 s. Voz orientativa: 47.5 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 04-02 · 20:10–21:20 · Enviar parámetros

**En pantalla:** Señala static void saludar(String nombre), su cuerpo y la llamada saludar(nombre). Explica la llamada temporal saludar("Sol") sin mezclarla con la entrada real.

**Narración:** El método saludar recibe un dato llamado nombre. Ese dato de entrada es un parámetro y declaramos su tipo como String. Cuando llamamos a saludar con Luna, el método construye un mensaje usando ese valor. Si lo llamamos con Sol, usa Sol. La tarea es la misma y el dato cambia. La palabra void indica que este método no devuelve un resultado a quien lo llamó. Puede mostrar un mensaje, pero mostrar y devolver son acciones diferentes. Los parámetros ayudan a reutilizar una tarea sin escribir dentro de ella un nombre fijo. En la llamada entregamos valores compatibles con los tipos que espera el método.

**Tiempo de escena:** 70 s. Voz orientativa: 50.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 04-03 · 21:20–22:30 · Devolver un resultado

**En pantalla:** Señala los parámetros int energiaActual, int cantidad y las dos instrucciones return. Muestra la llamada calcularEnergia(40, cantidad) y la variable energiaFinal.

**Narración:** El método calcular energía recibe dos enteros y devuelve un entero. Por eso aparece int antes de su nombre. Sumamos la energía actual y la cantidad de comida. Si el resultado supera cien, devolvemos cien; en otro caso devolvemos la suma. La palabra return termina la ejecución de esa llamada y entrega el valor. En main guardamos ese valor en energía final y después lo mostramos. El método del cálculo no necesita imprimirlo. Esta separación permite utilizar el mismo resultado para otras decisiones. Observa que cada camino posible del método termina devolviendo un entero, tal como promete su declaración.

**Tiempo de escena:** 70 s. Voz orientativa: 47.5 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 04-04 · 22:30–23:40 · Leer texto con Scanner

**En pantalla:** Señala import java.util.Scanner, new Scanner(System.in) y nextLine. Prepara entrada estándar con Luna y 30 en líneas separadas. Explica los campos de entrada del editor.

**Narración:** Hasta ahora escribimos los datos dentro del programa. Scanner permite leerlos desde la entrada estándar. La primera línea importa esa clase de la biblioteca estándar de Java. Después creamos un lector llamado entrada y lo conectamos con la entrada del programa. La llamada nextLine lee una línea de texto, que guardamos como nombre. En este editor podemos preparar los datos antes de ejecutar: escribe Luna en la primera línea y treinta en la segunda. El programa consumirá esos datos en orden. Leeremos primero el texto y después el entero, así evitamos aquí la confusión del salto de línea que puede quedar al combinar lecturas en el orden contrario.

**Tiempo de escena:** 70 s. Voz orientativa: 51.8 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 04-05 · 23:40–24:50 · Validar la entrada numérica

**En pantalla:** Señala hasNextInt, !, nextInt y cantidad < 0 || cantidad > 100. Ejecuta con abc, después con -1 y finalmente con Luna y 30. No omitas restaurar la entrada válida.

**Narración:** Antes de leer la cantidad, preguntamos si el próximo dato puede interpretarse como entero. El signo de exclamación niega esa respuesta. Si no es entero, mostramos un mensaje y terminamos con return. En un método void, return puede terminar sin devolver un valor. Después comprobamos el rango: una cantidad menor que cero o mayor que cien no se acepta. Las dos barras verticales significan o: basta con que una condición sea verdadera. Validar evita que un dato inesperado arruine la experiencia. Al terminar cerramos el lector porque este programa de consola ya no necesita más entrada.

**Tiempo de escena:** 70 s. Voz orientativa: 46.1 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 04-06 · 24:50–26:00 · Reto de métodos y entrada

**En pantalla:** Mantén el reto 20 segundos. Ejecuta Luna/30 y luego Luna/5. Muestra 70 y 45. Cierra con el método calcularEnergia visible.

**Narración:** Prueba el programa con tu propio nombre de mascota y treinta como cantidad. Con energía inicial cuarenta, el resultado esperado es setenta. Ahora cambia solamente la cantidad a cinco. Predice el resultado antes de ejecutar. Tienes un momento para probar. El nuevo resultado es cuarenta y cinco. Si escribes texto donde se espera un entero, aparece una explicación en lugar de continuar con un dato incorrecto. Ya tenemos entrada, cálculos y tareas separadas. Nos falta reunir los datos y las acciones de cada mascota en una estructura propia. Para eso usaremos clases y objetos.

**Reserva de práctica:** 20 segundos sin narración. Insertar la pausa después de «Tienes un momento para probar.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 70 s. Voz orientativa: 45.1 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Capítulo 5. Clases, objetos y encapsulacion

### 05-01 · 26:00–27:15 · De datos sueltos a una clase

**En pantalla:** Abre completed-examples/05/Main.java. Muestra Main y class Mascota en el mismo archivo. Señala nombre, energia y alimentar como datos y comportamiento.

**Narración:** Hasta ahora el nombre y la energía estaban separados. Si queremos varias mascotas, necesitamos organizar qué datos pertenecen a cada una y qué acciones pueden realizar. Una clase define ese modelo. Podemos imaginarla como una descripción que indica que toda mascota tendrá nombre, energía y una acción para alimentarse. Un objeto es una mascota concreta creada a partir de esa clase. La clase no es una mascota particular: permite construir distintas mascotas. En nuestro archivo mantendremos una clase pública llamada Main y otra clase llamada Mascota. Así podemos copiar todo en un solo archivo del editor y concentrarnos en los conceptos.

**Tiempo de escena:** 75 s. Voz orientativa: 48.5 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-02 · 27:15–28:30 · Atributos y acceso privado

**En pantalla:** Resalta private String nombre y private int energia. Indica que cada objeto tiene sus propios valores. No dejes en el programa una lectura externa de luna.energia.

**Narración:** Dentro de Mascota declaramos dos atributos: nombre y energía. Son datos que forman parte del estado de cada objeto. Dos mascotas pueden compartir la misma definición de clase y guardar valores diferentes. La palabra private limita el acceso directo a esos atributos desde fuera de la clase. Por ejemplo, main no podrá cambiar energía escribiendo directamente el atributo privado de Luna. Esto nos permite establecer una forma controlada de leer y modificar ese dato. Encapsular consiste en reunir estado y comportamiento y controlar el acceso al estado. Lo veremos con una regla concreta: la energía siempre debe quedar entre cero y cien.

**Tiempo de escena:** 75 s. Voz orientativa: 49.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-03 · 28:30–29:45 · Construir el estado inicial

**En pantalla:** Señala Mascota(String nombre, int energia), this.nombre = nombre y setEnergia(energia). Diferencia el constructor de los métodos con tipo de retorno.

**Narración:** El constructor prepara una mascota cuando la creamos. Tiene el mismo nombre que la clase y no declara un tipo de retorno. Recibe el nombre y la energía inicial. En la instrucción this punto nombre, this se refiere al objeto que se está construyendo. A la derecha, nombre se refiere al parámetro recibido. Aunque se llaman igual, representan cosas distintas. Para la energía llamamos a set energía, de modo que el valor inicial también respete los límites. Un constructor nos ayuda a evitar objetos a medio preparar. En lugar de crear una mascota y recordar luego qué datos faltaban, entregamos sus datos al construirla.

**Tiempo de escena:** 75 s. Voz orientativa: 49.9 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-04 · 29:45–31:00 · Crear dos objetos independientes

**En pantalla:** Resalta las dos expresiones new Mascota de main. Antes de alimentar, muestra mediante impresiones temporales Luna 40 y Sol 70; después restaura la solución.

**Narración:** La palabra new crea un objeto y llama al constructor correspondiente. Creamos Luna con cuarenta de energía y Sol con setenta. Las variables luna y sol nos permiten trabajar con esos objetos. Cada uno guarda su propio estado. Si alimentamos solo a Luna, esperamos que cambie la energía de Luna y que la de Sol permanezca igual. Esa independencia es una idea central de los objetos. Piensa en dos mascotas reales: ambas pueden comer, pero alimentar a una no alimenta automáticamente a la otra. Antes de ejecutar, predice los valores que deberían aparecer para cada una. Enseguida comprobaremos esa predicción.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «Enseguida comprobaremos esa predicción.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 75 s. Voz orientativa: 48.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-05 · 31:00–32:15 · Consultar con getters

**En pantalla:** Muestra getNombre y getEnergia. Relaciona return con las impresiones de main. Señala String e int como tipos de retorno.

**Narración:** Un getter es un método que permite consultar un dato. El nombre suele comenzar con get y continuar con el atributo que queremos leer. Get nombre devuelve un String y get energía devuelve un int. Desde main llamamos a esos métodos sobre la mascota correspondiente. El punto conecta la variable del objeto con la acción que solicitamos. Consultar no modifica la energía: solo obtiene su valor. Hicimos públicos estos métodos para utilizarlos desde fuera de Mascota y mantuvimos privados los atributos. No necesitamos crear un setter para cada atributo por obligación. En este programa el nombre se establece al construir y después solo lo consultamos.

**Tiempo de escena:** 75 s. Voz orientativa: 50.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-06 · 32:15–33:30 · Cambiar con un setter y una regla

**En pantalla:** Muestra setEnergia y sus tres ramas. Ejecuta la solución: luna.setEnergia(150) produce 100. Señala por qué no se puede saltar esa regla mediante acceso directo al atributo.

**Narración:** El setter permite cambiar un dato aplicando una regla. Nuestro set energía recibe un entero. Si es menor que cero, guarda cero. Si es mayor que cien, guarda cien. Si está dentro del rango, guarda el valor recibido. No es la única política posible, pero es la elegida para este programa. Cuando pedimos establecer ciento cincuenta, el objeto termina con cien. La regla no queda repartida en cada parte que usa la mascota: vive dentro de la clase. Eso reduce el riesgo de olvidar una validación. La encapsulación tiene aquí una utilidad visible: proteger un estado válido mientras ofrecemos operaciones claras para consultarlo y cambiarlo.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «Cuando pedimos establecer ciento cincuenta, el objeto termina con cien.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 75 s. Voz orientativa: 50.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-07 · 33:30–34:45 · Un comportamiento del objeto

**En pantalla:** Muestra alimentar, su parámetro, validación y llamada a setEnergia. Ejecuta Luna 40 + 20 = 60 y Sol 70. Distingue alimentar de setEnergia.

**Narración:** El método alimentar representa un comportamiento de la mascota. Recibe una cantidad, comprueba que esté entre cero y cien y suma esa cantidad a la energía actual. Después utiliza el setter para respetar el límite final. Alimentar con veinte significa agregar veinte; establecer energía en veinte significa reemplazarla por veinte. Son operaciones diferentes. En main pedimos alimentar a Luna con veinte. Luna pasa de cuarenta a sesenta y Sol permanece en setenta. Como el método trabaja con el estado del objeto que recibe la llamada, no necesitamos pasar el nombre ni la energía de la mascota como parámetros adicionales. El objeto ya contiene esos datos.

**Tiempo de escena:** 75 s. Voz orientativa: 50.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 05-08 · 34:45–36:00 · Reto de objetos y encapsulación

**En pantalla:** Mantén el reto 25 segundos. En starter-files/05 agrega Sol y las operaciones pendientes. Después compara con la solución y señala 60, 70 y 100 en la salida.

**Narración:** Crea una segunda mascota y alimenta solamente a la primera. Comprueba que los resultados sean diferentes. Luego intenta establecer una energía de ciento cincuenta mediante el setter. Puedes pausar para completar el reto. Con los valores del ejemplo, Luna queda en sesenta, Sol en setenta y el cambio posterior de Luna queda limitado a cien. Ya construiste una clase con atributos, constructor y métodos. También creaste objetos y controlaste cómo cambia su estado. En el último capítulo reuniremos varias mascotas y reutilizaremos estas mismas operaciones.

**Reserva de práctica:** 25 segundos sin narración. Insertar la pausa después de «Puedes pausar para completar el reto.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 75 s. Voz orientativa: 40.8 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Capítulo 6. Arrays y proyecto final

### 06-01 · 36:00–37:15 · Guardar varias mascotas en un array

**En pantalla:** Abre completed-examples/06/Main.java. Resalta Mascota[] mascotas y las dos construcciones. Señala que la clase Mascota conserva las mismas reglas del capítulo anterior.

**Narración:** Un array permite reunir varios elementos del mismo tipo en una estructura ordenada. Aquí escribimos Mascota seguido de corchetes para indicar un array de referencias a objetos Mascota. Dentro colocamos dos mascotas: una usa el nombre que escribe el usuario y la otra se llama Sol. No copiamos de nuevo el código de la clase para cada mascota; creamos objetos de la misma clase. El array que acabamos de crear tiene dos posiciones y su tamaño queda fijo. Si queremos un ejemplo con tres mascotas, podemos cambiar esta inicialización antes de ejecutar. Más adelante existen otras estructuras para colecciones que cambian de tamaño, pero hoy trabajaremos con arrays.

**Tiempo de escena:** 75 s. Voz orientativa: 51.8 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-02 · 37:15–38:30 · Índices y longitud

**En pantalla:** Anota índice 0 sobre la primera mascota e índice 1 sobre la segunda. Señala mascotas.length. Explica mascotas[2] como acceso inválido sin dejar el error activo.

**Narración:** Cada posición del array tiene un índice. En Java los índices comienzan en cero. Con dos mascotas, los índices válidos son cero y uno. La propiedad length nos indica cuántas posiciones tiene el array: en este caso devuelve dos. Esa cantidad no es el último índice. Si intentáramos acceder al índice dos, estaríamos fuera del array y el programa fallaría. Esta diferencia explica por qué muchos recorridos usan menor que la longitud y no menor o igual. Puedes imaginar dos casillas numeradas desde cero. Cuenta las casillas y después observa la etiqueta de la última: son números diferentes.

**Reserva de práctica:** 5 segundos sin narración. Insertar la pausa después de «son números diferentes.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 75 s. Voz orientativa: 47.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-03 · 38:30–39:45 · Recorrer y alimentar

**En pantalla:** Resalta el for completo. Relaciona mascotas[indice] con la variable mascota. Con entrada Luna/30, sigue primero Luna y luego Sol hasta la salida 70 y 100.

**Narración:** Recorremos el array con un for que comienza en cero y continúa mientras el índice sea menor que la longitud. En cada vuelta obtenemos la mascota de esa posición. La variable mascota representa el objeto que estamos atendiendo en esa vuelta. Mostramos su energía, lo alimentamos y mostramos el resultado. Con treinta de comida, Luna pasa de cuarenta a setenta y Sol pasa de setenta a cien. El mismo bloque funciona para ambas. No necesitamos preguntar manualmente si estamos en la primera o la segunda mascota. El recorrido selecciona cada elemento y la clase se encarga de aplicar su comportamiento y sus reglas.

**Tiempo de escena:** 75 s. Voz orientativa: 49.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-04 · 39:45–41:00 · Trabajar con cadenas de los objetos

**En pantalla:** Señala mascota.getNombre().length(). Compara la propiedad mascotas.length sin paréntesis con el método de String con paréntesis. Usa Luna y Sol como nombres simples.

**Narración:** El nombre que devuelve get nombre es una cadena, un String. Podemos usar sus métodos para trabajar con ese texto. En el ejemplo consultamos length y mostramos la longitud del nombre. Luna tiene cuatro letras y Sol tiene tres. Observa una diferencia de escritura: para el array usamos length sin paréntesis; para String llamamos al método length con paréntesis. No son la misma operación aunque sus nombres se parezcan. En estos nombres simples el resultado coincide con el número de letras; con algunos símbolos y emojis el conteo de una cadena puede ser más complejo. Hoy usaremos palabras sencillas para concentrarnos en cómo obtener el dato de cada objeto.

**Tiempo de escena:** 75 s. Voz orientativa: 52.3 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-05 · 41:00–42:15 · La ejecución completa

**En pantalla:** Ejecuta desde el inicio con Luna/30. Sigue entrada, validación, creación del array, recorrido y salida. Luego prueba Luna/100 para mostrar el límite de ambos objetos.

**Narración:** Sigamos el programa completo. Primero leemos el nombre y una cantidad entera. Validamos esa cantidad antes de crear las mascotas. Después construimos los dos objetos y los guardamos en el array. Finalmente recorremos el array y trabajamos con cada mascota. Cada parte tiene una responsabilidad que ya conocemos. Si la entrada es texto en lugar de un entero, mostramos el mensaje y terminamos. Si la cantidad está fuera del rango, también terminamos. Si la cantidad es cien, ambas mascotas quedan con energía cien porque el setter limita la suma. Probar casos normales, límites y entradas incorrectas nos ayuda a verificar el comportamiento desde distintas situaciones.

**Tiempo de escena:** 75 s. Voz orientativa: 50.4 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-06 · 42:15–44:00 · Reto final y errores frecuentes

**En pantalla:** Abre starter-files/06 y da 35 segundos de práctica. Agrega new Mascota("Nube", 20), completa el recorrido y ejecuta. Luego compara con la solución integrada. Muestra brevemente punto y coma, mayúsculas, condición del bucle y rango del array.

**Narración:** Tu reto final es agregar una tercera mascota llamada Nube con veinte de energía y hacer que el programa muestre sus datos. Si recorres el array usando su longitud, no necesitas escribir un recorrido diferente para tres elementos. Después integra la entrada que aprendiste en la lección cuatro. Puedes pausar el video para completar ambas partes. Al revisar errores, empieza por algo pequeño: comprueba puntos y coma, comillas, llaves y mayúsculas. Java distingue Main de main y String de string. Si un bucle no termina, revisa qué variable cambia. Si accedes a un array, comprueba sus índices válidos. Cambia una cosa a la vez y vuelve a ejecutar para entender qué corrigió el problema.

**Reserva de práctica:** 35 segundos sin narración. Insertar la pausa después de «Puedes pausar el video para completar ambas partes.» y antes de la siguiente frase. Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. Puede ampliarse al pausar el reproductor.

**Tiempo de escena:** 105 s. Voz orientativa: 54.7 s a 125 palabras/minuto; el resto se dedica a la demostración.

### 06-07 · 44:00–45:00 · Cierre y siguientes pasos

**En pantalla:** Mantén visible el programa final y su salida, sin nombres ni logos de autores. Destaca variable, condición, método, clase, objeto y array sobre sus líneas reales.

**Narración:** Empezamos mostrando un mensaje y terminamos con un programa que lee datos, calcula, decide, repite y trabaja con objetos. Una variable guarda información. Un método organiza una tarea. Una clase define estado y comportamiento; cada objeto tiene su propio estado. Un array reúne elementos para recorrerlos. La encapsulación nos permitió mantener la energía dentro de un rango válido. No necesitas memorizar cada línea para seguir aprendiendo. Vuelve a los ejemplos, cambia un dato y predice el resultado antes de ejecutar. Como siguiente reto, diseña una acción para jugar que reduzca la energía sin bajar de cero. Ya tienes las herramientas para intentarlo.

**Tiempo de escena:** 60 s. Voz orientativa: 49.0 s a 125 palabras/minuto; el resto se dedica a la demostración.

## Hoja de tiempos

| Escena | Inicio | Fin | Segundos | Palabras | Práctica mínima | Voz estimada a 125 ppm |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 01-01 | 00:00 | 01:00 | 60 | 90 | 0 s | 43.2 s |
| 01-02 | 01:00 | 02:00 | 60 | 95 | 8 s | 45.6 s |
| 01-03 | 02:00 | 03:00 | 60 | 95 | 0 s | 45.6 s |
| 01-04 | 03:00 | 04:00 | 60 | 90 | 0 s | 43.2 s |
| 01-05 | 04:00 | 05:00 | 60 | 77 | 20 s | 37.0 s |
| 02-01 | 05:00 | 06:10 | 70 | 97 | 0 s | 46.6 s |
| 02-02 | 06:10 | 07:20 | 70 | 99 | 0 s | 47.5 s |
| 02-03 | 07:20 | 08:30 | 70 | 99 | 5 s | 47.5 s |
| 02-04 | 08:30 | 09:40 | 70 | 97 | 0 s | 46.6 s |
| 02-05 | 09:40 | 10:50 | 70 | 100 | 0 s | 48.0 s |
| 02-06 | 10:50 | 12:00 | 70 | 84 | 25 s | 40.3 s |
| 03-01 | 12:00 | 13:10 | 70 | 93 | 0 s | 44.6 s |
| 03-02 | 13:10 | 14:20 | 70 | 93 | 5 s | 44.6 s |
| 03-03 | 14:20 | 15:30 | 70 | 98 | 0 s | 47.0 s |
| 03-04 | 15:30 | 16:40 | 70 | 100 | 5 s | 48.0 s |
| 03-05 | 16:40 | 17:50 | 70 | 100 | 0 s | 48.0 s |
| 03-06 | 17:50 | 19:00 | 70 | 80 | 25 s | 38.4 s |
| 04-01 | 19:00 | 20:10 | 70 | 99 | 0 s | 47.5 s |
| 04-02 | 20:10 | 21:20 | 70 | 105 | 0 s | 50.4 s |
| 04-03 | 21:20 | 22:30 | 70 | 99 | 0 s | 47.5 s |
| 04-04 | 22:30 | 23:40 | 70 | 108 | 0 s | 51.8 s |
| 04-05 | 23:40 | 24:50 | 70 | 96 | 0 s | 46.1 s |
| 04-06 | 24:50 | 26:00 | 70 | 94 | 20 s | 45.1 s |
| 05-01 | 26:00 | 27:15 | 75 | 101 | 0 s | 48.5 s |
| 05-02 | 27:15 | 28:30 | 75 | 102 | 0 s | 49.0 s |
| 05-03 | 28:30 | 29:45 | 75 | 104 | 0 s | 49.9 s |
| 05-04 | 29:45 | 31:00 | 75 | 100 | 5 s | 48.0 s |
| 05-05 | 31:00 | 32:15 | 75 | 105 | 0 s | 50.4 s |
| 05-06 | 32:15 | 33:30 | 75 | 105 | 5 s | 50.4 s |
| 05-07 | 33:30 | 34:45 | 75 | 105 | 0 s | 50.4 s |
| 05-08 | 34:45 | 36:00 | 75 | 85 | 25 s | 40.8 s |
| 06-01 | 36:00 | 37:15 | 75 | 108 | 0 s | 51.8 s |
| 06-02 | 37:15 | 38:30 | 75 | 98 | 5 s | 47.0 s |
| 06-03 | 38:30 | 39:45 | 75 | 103 | 0 s | 49.4 s |
| 06-04 | 39:45 | 41:00 | 75 | 109 | 0 s | 52.3 s |
| 06-05 | 41:00 | 42:15 | 75 | 105 | 0 s | 50.4 s |
| 06-06 | 42:15 | 44:00 | 105 | 114 | 35 s | 54.7 s |
| 06-07 | 44:00 | 45:00 | 60 | 102 | 0 s | 49.0 s |

**Total:** 45:00, 38 escenas y 3734 palabras de narración.

Estas estimaciones no sustituyen la medición del audio generado ni garantizan el tiempo de la exportación.
