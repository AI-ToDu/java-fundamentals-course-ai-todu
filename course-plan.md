# Fundamentos de Java: crea tu mascota virtual

## Resumen del curso

En este curso pasarás de imprimir «Hola, mundo» a construir un programa de consola que recibe datos y permite alimentar a varias mascotas virtuales. Cada lección presenta un ejemplo, te deja predecir qué pasará al ejecutarlo y termina con una práctica para comprobarlo.

- **Duración total:** 45:00, distribuidos en seis videos de entre 5 y 10 minutos.
- **Público:** estudiantes de secundaria de 13 a 17 años.
- **Prerrequisitos:** ninguno.
- **Herramientas:** un navegador y [el editor gratuito de Java en JDoodle](https://www.jdoodle.com/online-java-compiler-ide). Los ejemplos son compatibles con Java 17. Puedes escribir y ejecutar el código desde el navegador.
- **Repositorio público del curso:** [AI-ToDu/java-fundamentals-course-ai-todu](https://github.com/AI-ToDu/java-fundamentals-course-ai-todu).

Al terminar podrás declarar variables, tomar decisiones con condiciones, repetir instrucciones, escribir métodos, leer datos de la consola y construir clases que protejan el estado de sus objetos. El proyecto final reúne esas ideas en un arreglo de mascotas.

## Secuencia de lecciones

Los tiempos del montaje indican dónde empieza y termina cada lección en el video maestro. Los tiempos del reto se cuentan desde el inicio del video de la lección.

| Lección | Tramo del video maestro | Duración | Reto dentro de la lección |
| --- | --- | --- | --- |
| [1. Tu primer programa](#lección-1-tu-primer-programa) | 00:00–05:00 | 05:00 | 04:00 · Agregar un mensaje de bienvenida |
| [2. Datos y operaciones](#lección-2-datos-y-operaciones) | 05:00–12:00 | 07:00 | 05:50 · Calcular la energía de la mascota |
| [3. Decisiones y bucles](#lección-3-decisiones-y-bucles) | 12:00–19:00 | 07:00 | 05:50 · Cambiar un umbral y el número de pasos |
| [4. Métodos y entrada de datos](#lección-4-métodos-y-entrada-de-datos) | 19:00–26:00 | 07:00 | 05:50 · Leer y validar el nombre y la cantidad de comida |
| [5. Clases, objetos y encapsulación](#lección-5-clases-objetos-y-encapsulación) | 26:00–36:00 | 10:00 | 08:45 · Crear dos mascotas y comprobar el límite de energía |
| [6. Arreglos y proyecto final](#lección-6-arreglos-y-proyecto-final) | 36:00–45:00 | 09:00 | 06:15 · Agregar una tercera mascota al arreglo |

### Lección 1. Tu primer programa

**Qué aprenderás.** Programar es escribir instrucciones que una computadora puede ejecutar. En el editor de Java verás dónde escribir código, cómo pulsar **Execute** y dónde leer el resultado. La clase `Main` contiene el método `main`, que es el punto de entrada de estos ejemplos. Las llaves agrupan bloques, las comillas delimitan el texto y el punto y coma termina cada instrucción `System.out.println(...)`.

**Práctica.** Cambia el mensaje de bienvenida y agrega una línea que diga «Luna está lista para jugar». Ejecuta y verifica el orden de los mensajes. Quita el punto y coma de una instrucción y vuelve a ejecutar. Busca el mensaje `';' expected`, restaura el signo y comprueba que vuelven a aparecer las líneas de salida.

**Video no listado:** [Ver la lección 1 en YouTube](https://youtu.be/XbAOK7YL3-4).\
**Editor precargado:** [Hola, mundo en JDoodle](https://www.jdoodle.com/ia/z8sv-f9z7-pzga).\
**Código:** [archivo inicial](starter-files/01/Main.java) · [ejemplo resuelto](completed-examples/01/Main.java).

### Lección 2. Datos y operaciones

**Qué aprenderás.** Guarda el nombre en un `String`, la energía en un `int`, el peso en un `double` y el resultado de una comparación en un `boolean`. Usa `=` para asignar y `==` para comparar números. Verás sumas, restas, multiplicación y división, además de cómo unir texto y valores con `+`. Los paréntesis permiten calcular una expresión antes de añadir su resultado a un mensaje.

**Práctica.** Empieza con 40 puntos de energía, suma 20 por comer y resta 15 por jugar. La energía final será 45. Predice qué muestran `5 / 2` y `5.0 / 2`, y compara la salida con 2 y 2.5. Cambia el nombre y comprueba qué pasa con `energia < 50` al usar una energía inicial de 70.

**Video no listado:** [Ver la lección 2 en YouTube](https://youtu.be/mP6We6c_Ujc).\
**Editor precargado:** [Variables y operaciones en JDoodle](https://www.jdoodle.com/ia/k329-7vxu-392q).\
**Código:** [archivo inicial](starter-files/02/Main.java) · [ejemplo resuelto](completed-examples/02/Main.java).

### Lección 3. Decisiones y bucles

**Qué aprenderás.** Usa `if/else` para elegir entre alimentar a la mascota y dejarla jugar. Usa un `for` con contador para mostrar tres pasos y un `while` para sumar energía mientras sea menor que 60. El `while` comprueba la condición antes de cada vuelta, así que puede ejecutarse cero veces. Cambiar la energía dentro del bucle permite que la condición llegue a ser falsa.

**Práctica.** Cambia el umbral de hambre y la cantidad de pasos. Observa cómo el `while` lleva la energía de 40 a 50 y después a 60. Predice cuántas vueltas dará si empieza con energía 60 y comprueba tu respuesta.

**Video no listado:** [Ver la lección 3 en YouTube](https://youtu.be/aL9wKP04aVU).\
**Editor precargado:** [Decisiones y bucles en JDoodle](https://www.jdoodle.com/ia/sxv3-czsf-6y3j).\
**Código:** [archivo inicial](starter-files/03/Main.java) · [ejemplo resuelto](completed-examples/03/Main.java).

### Lección 4. Métodos y entrada de datos

**Qué aprenderás.** Un método reúne instrucciones para una tarea. `saludar(nombre)` recibe un argumento e imprime un mensaje. `calcularEnergia(40, cantidad)` devuelve un número con `return` y limita el resultado a 100. En la consola, `Scanner` lee el nombre con `nextLine()`. Antes de llamar a `nextInt()`, comprueba con `hasNextInt()` que el siguiente dato sea un entero. Luego valida que la cantidad esté entre 0 y 100.

**Práctica.** Escribe `Luna` en la primera línea de la entrada estándar de JDoodle y `30` en la segunda. La energía final será 70. Cambia la cantidad y comprueba el resultado. Prueba con texto y con un entero fuera del rango para comparar los mensajes de validación.

**Video no listado:** [Ver la lección 4 en YouTube](https://youtu.be/2Hczr1QxwKQ).\
**Editor precargado:** [Métodos y Scanner en JDoodle](https://www.jdoodle.com/ia/d5zu-hep8-bpgy).\
**Código:** [archivo inicial](starter-files/04/Main.java) · [ejemplo resuelto](completed-examples/04/Main.java).

### Lección 5. Clases, objetos y encapsulación

**Qué aprenderás.** La clase `Mascota` define los datos que guarda cada mascota y las acciones que puede realizar. `new Mascota("Luna", 40)` crea un objeto y llama a su constructor. `this.nombre` se refiere al atributo del objeto que estamos inicializando. Los atributos privados se consultan con `getNombre()` y `getEnergia()`. El setter `setEnergia(...)` aplica el límite de 0 a 100, y `alimentar(...)` usa la misma regla al sumar energía.

**Práctica.** Crea a Luna con 40 de energía y a Sol con 70. Alimenta a Luna con 20 y comprueba que llega a 60 y Sol sigue en 70. Intenta asignar 150 a Luna y consulta su energía. El resultado será 100.

**Video no listado:** [Ver la lección 5 en YouTube](https://youtu.be/25sUcyeevg4).\
**Editor precargado:** [Clases y encapsulación en OneCompiler](https://onecompiler.com/java/458r2fxdw).\
**Código:** [archivo inicial](starter-files/05/Main.java) · [ejemplo resuelto](completed-examples/05/Main.java).

### Lección 6. Arreglos y proyecto final

**Qué aprenderás.** El programa final lee y valida la entrada, crea los objetos, los guarda en un arreglo `Mascota[]` y los alimenta en un recorrido. Un arreglo de dos elementos tiene índices 0 y 1. Acceder a `mascotas[2]` produce `ArrayIndexOutOfBoundsException` al ejecutar. Recorre el arreglo con `indice < mascotas.length`. Para consultar la longitud del nombre usa `mascota.getNombre().length()`: el arreglo usa `length` y la cadena usa el método `length()`.

**Práctica.** Ejecuta con `Luna` y `30` en líneas separadas. Luna pasa de 40 a 70 y Sol de 70 a 100. El programa muestra 4 para la longitud de «Luna» y 3 para «Sol». Agrega a Nube con 20 de energía y repite con 10 de comida. El mismo recorrido visita las tres mascotas y muestra 50, 80 y 30, respectivamente. Prueba también con 100 para comprobar el límite y con `abc` para revisar el mensaje de entrada inválida.

**Video no listado:** [Ver la lección 6 en YouTube](https://youtu.be/kYl6aDT8rO8).\
**Editor precargado:** [Proyecto final en OneCompiler](https://onecompiler.com/java/458r2gmga).\
**Código:** [archivo inicial](starter-files/06/Main.java) · [proyecto completo](completed-examples/06/Main.java).

## Repaso y recursos

1. Ante un error de compilación, lee la línea indicada y revisa también la anterior. Comprueba puntos y coma, comillas, llaves y mayúsculas.
2. Si un resultado numérico te sorprende, revisa los valores y tipos de los operandos. Predice la salida antes de ejecutar.
3. Si un bucle no termina, sigue el valor que controla su condición. Si falla un acceso al arreglo, comprueba que el índice sea menor que su longitud.
4. Prueba entradas normales, límites y valores incorrectos. Cambia una cosa a la vez y vuelve a ejecutar.
5. Como siguiente reto, agrega una acción para jugar que reduzca la energía sin bajar de cero.

El curso alterna explicaciones con texto en pantalla, capturas de ejecución, narración y pausas para practicar. Los retos permiten predecir la salida y comparar el resultado con el ejemplo resuelto.

En el repositorio, `starter-files/` contiene los retos, `completed-examples/` reúne las soluciones y `scripts/` guarda el [guion del contenido base](scripts/guion-45-minutos.md) y los materiales de producción. El [README](README.md) explica cómo abrir los ejemplos y cargar la entrada estándar.

## Elaboración en equipo

**Universidad Peruana de Ciencias Aplicadas** · Ingeniería de Software\
**Periodo:** 202620 · **Curso:** 1ASI0729 Desarrollo de Aplicaciones Open Source\
**NRC:** 7750 · **Startup:** AI ToDu\
**Líder e integrante:** Kevin Salazar Marquina\
**Fecha de entrega:** 13 de noviembre de 2026

Kevin definió el enfoque en Java y la estructura del curso. La edición final sigue la indicación del docente de presentar 45 minutos en seis videos independientes para esta entrega individual. El material comprende el plan, los programas iniciales y resueltos, las capturas de ejecución y las seis lecciones narradas. [Historial de cambios del curso](https://github.com/AI-ToDu/java-fundamentals-course-ai-todu/commits/main/).
