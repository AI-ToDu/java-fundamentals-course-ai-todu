# Fundamentos de Java: crea tu mascota virtual

## Resumen del curso

En este curso pasarás de imprimir «Hola, mundo» a construir un programa de consola que recibe datos y permite alimentar a varias mascotas virtuales. Cada lección presenta un ejemplo, te deja predecir qué pasará al ejecutarlo y termina con una práctica para comprobarlo.

- **Duración total:** 60:00. Seis lecciones con 45 minutos de contenido base y 15 minutos de demostraciones, retos y remates.
- **Público:** estudiantes de secundaria de 12 a 17 años.
- **Prerrequisitos:** ninguno.
- **Herramientas:** un navegador y [el editor gratuito de Java en JDoodle](https://www.jdoodle.com/online-java-compiler-ide). Los ejemplos son compatibles con Java 17. Puedes escribir y ejecutar el código desde el navegador.
- **Repositorio público del curso:** [AI-ToDu/java-fundamentals-course-ai-todu](https://github.com/AI-ToDu/java-fundamentals-course-ai-todu).

Al terminar podrás declarar variables, tomar decisiones con condiciones, repetir instrucciones, escribir métodos, leer datos de la consola y construir clases que protejan el estado de sus objetos. El proyecto final reúne esas ideas en un arreglo de mascotas.

## Secuencia de lecciones

Los tiempos de esta tabla se cuentan desde el inicio del video maestro. Cada lección tiene su propio reto y puede verse por separado siguiendo el orden del curso.

| Lección | Tramo del video maestro | Duración | Práctica de ejecución |
| --- | --- | --- | --- |
| [1. Tu primer programa](#lección-1-tu-primer-programa) | 00:00–07:30 | 07:30 | 04:00–06:30 · Corregir un punto y coma |
| [2. Datos y operaciones](#lección-2-datos-y-operaciones) | 07:30–17:00 | 09:30 | 12:10–14:40 · Comparar división entera y decimal |
| [3. Decisiones y bucles](#lección-3-decisiones-y-bucles) | 17:00–26:30 | 09:30 | 22:50–25:20 · Predecir cuántas veces se repite un bucle |
| [4. Métodos y entrada de datos](#lección-4-métodos-y-entrada-de-datos) | 26:30–36:00 | 09:30 | 32:20–34:50 · Probar una entrada inválida |
| [5. Clases, objetos y encapsulación](#lección-5-clases-objetos-y-encapsulación) | 36:00–48:30 | 12:30 | 43:30–46:00 · Comprobar los límites de energía |
| [6. Arreglos y proyecto final](#lección-6-arreglos-y-proyecto-final) | 48:30–60:00 | 11:30 | 56:30–59:00 · Corregir un índice fuera de rango |

### Lección 1. Tu primer programa

**Qué aprenderás.** Programar es escribir instrucciones que una computadora puede ejecutar. En el editor de Java verás dónde escribir código, cómo pulsar **Execute** y dónde leer el resultado. La clase `Main` contiene el método `main`, que es el punto de entrada de estos ejemplos. Las llaves agrupan bloques, las comillas delimitan el texto y el punto y coma termina cada instrucción `System.out.println(...)`.

**Práctica.** Cambia el mensaje de bienvenida y agrega una línea que diga «Luna está lista para jugar». Ejecuta y verifica el orden de los mensajes. Quita el punto y coma de una instrucción y vuelve a ejecutar. Busca el mensaje `';' expected`, restaura el signo y comprueba que vuelven a aparecer las líneas de salida.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** [Hola, mundo en JDoodle](https://www.jdoodle.com/ia/z8sv-f9z7-pzga). Acceso sin iniciar sesión pendiente de confirmar.\
**Código:** [archivo inicial](starter-files/01/Main.java) · [ejemplo resuelto](completed-examples/01/Main.java).

### Lección 2. Datos y operaciones

**Qué aprenderás.** Guarda el nombre en un `String`, la energía en un `int`, el peso en un `double` y el resultado de una comparación en un `boolean`. Usa `=` para asignar y `==` para comparar números. Verás sumas, restas, multiplicación y división, además de cómo unir texto y valores con `+`. Los paréntesis permiten calcular una expresión antes de añadir su resultado a un mensaje.

**Práctica.** Empieza con 40 puntos de energía, suma 20 por comer y resta 15 por jugar. La energía final será 45. Predice qué muestra `7 / 2` y qué muestra `7.0 / 2`. Luego repite con 9. Los resultados son 3 y 3.5 en la primera prueba, y 4 y 4.5 en la segunda. Cambia también el nombre y comprueba qué pasa con `energia < 50` al usar una energía inicial de 70.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** enlace pendiente. Puedes pegar el archivo inicial en [JDoodle](https://www.jdoodle.com/online-java-compiler-ide).\
**Código:** [archivo inicial](starter-files/02/Main.java) · [ejemplo resuelto](completed-examples/02/Main.java).

### Lección 3. Decisiones y bucles

**Qué aprenderás.** Usa `if/else` para elegir entre alimentar a la mascota y dejarla jugar. Usa un `for` con contador para mostrar tres pasos y un `while` para sumar energía mientras sea menor que 60. El `while` comprueba la condición antes de cada vuelta, así que puede ejecutarse cero veces. Cambiar la energía dentro del bucle permite que la condición llegue a ser falsa.

**Práctica.** Cambia el umbral de hambre y la cantidad de pasos. Luego compara el `while` con energías iniciales de 40, 60 y 55. Con 40 imprime 50 y 60, con 60 no entra y con 55 entra una vez y llega a 65. Explica por qué el `for` sigue mostrando los pasos aunque el `while` no entre.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** enlace pendiente. Puedes pegar el archivo inicial en [JDoodle](https://www.jdoodle.com/online-java-compiler-ide).\
**Código:** [archivo inicial](starter-files/03/Main.java) · [ejemplo resuelto](completed-examples/03/Main.java).

### Lección 4. Métodos y entrada de datos

**Qué aprenderás.** Un método reúne instrucciones para una tarea. `saludar(nombre)` recibe un argumento e imprime un mensaje. `calcularEnergia(40, cantidad)` devuelve un número con `return` y limita el resultado a 100. En la consola, `Scanner` lee el nombre con `nextLine()`. Antes de llamar a `nextInt()`, comprueba con `hasNextInt()` que el siguiente dato sea un entero. Luego valida que la cantidad esté entre 0 y 100.

**Práctica.** Escribe `Luna` en la primera línea de la entrada estándar de JDoodle y `30` en la segunda. La energía final será 70. Repite con `abc`, `-1` y `20`. El programa rechaza el texto porque no es un entero y rechaza el número negativo por el rango. Con 20 muestra 60.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** enlace pendiente. Puedes pegar el archivo inicial en [JDoodle](https://www.jdoodle.com/online-java-compiler-ide).\
**Código:** [archivo inicial](starter-files/04/Main.java) · [ejemplo resuelto](completed-examples/04/Main.java).

### Lección 5. Clases, objetos y encapsulación

**Qué aprenderás.** La clase `Mascota` define los datos que guarda cada mascota y las acciones que puede realizar. `new Mascota("Luna", 40)` crea un objeto y llama a su constructor. `this.nombre` se refiere al atributo del objeto que estamos inicializando. Los atributos privados se consultan con `getNombre()` y `getEnergia()`. El setter `setEnergia(...)` aplica el límite de 0 a 100, y `alimentar(...)` usa la misma regla al sumar energía.

**Práctica.** Crea a Luna con 40 de energía y a Sol con 70. Alimenta a Luna con 20 y comprueba que llega a 60 y Sol sigue en 70. Intenta asignar 150 a Luna y consulta su energía. El resultado será 100. Alimenta a Sol con 10 y llama a `luna.setEnergia(-15)`. Sol queda en 80 y Luna en 0.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** enlace pendiente. Puedes pegar el archivo inicial en [JDoodle](https://www.jdoodle.com/online-java-compiler-ide).\
**Código:** [archivo inicial](starter-files/05/Main.java) · [ejemplo resuelto](completed-examples/05/Main.java).

### Lección 6. Arreglos y proyecto final

**Qué aprenderás.** El programa final lee y valida la entrada, crea los objetos, los guarda en un arreglo `Mascota[]` y los alimenta en un recorrido. Un arreglo de dos elementos tiene índices 0 y 1. Acceder a `mascotas[2]` produce `ArrayIndexOutOfBoundsException` al ejecutar. Recorre el arreglo con `indice < mascotas.length`. Para consultar la longitud del nombre usa `mascota.getNombre().length()`: el arreglo usa `length` y la cadena usa el método `length()`.

**Práctica.** Ejecuta con `Luna` y `30` en líneas separadas. Luna pasa de 40 a 70 y Sol de 70 a 100. El programa muestra 4 para la longitud de «Luna» y 3 para «Sol». Agrega a Nube con 20 de energía y repite con 10 de comida. El mismo recorrido visita las tres mascotas y muestra 50, 80 y 30, respectivamente. Prueba también con 100 para comprobar el límite y con `abc` para revisar el mensaje de entrada inválida.

**Video no listado:** enlace de YouTube pendiente.\
**Editor precargado:** enlace pendiente. Puedes pegar el archivo inicial en [JDoodle](https://www.jdoodle.com/online-java-compiler-ide).\
**Código:** [archivo inicial](starter-files/06/Main.java) · [proyecto completo](completed-examples/06/Main.java).

## Repaso y recursos

1. Ante un error de compilación, lee la línea indicada y revisa también la anterior. Comprueba puntos y coma, comillas, llaves y mayúsculas.
2. Si un resultado numérico te sorprende, revisa los valores y tipos de los operandos. Predice la salida antes de ejecutar.
3. Si un bucle no termina, sigue el valor que controla su condición. Si falla un acceso al arreglo, comprueba que el índice sea menor que su longitud.
4. Prueba entradas normales, límites y valores incorrectos. Cambia una cosa a la vez y vuelve a ejecutar.
5. Como siguiente reto, agrega una acción para jugar que reduzca la energía sin bajar de cero.

El curso alterna explicaciones con texto en pantalla, capturas de ejecución, narración y pausas. Los remates acompañan lo que ocurre en la consola. Woody aparece junto al error de compilación y la ardilla reacciona al acceso fuera del arreglo. Las seis prácticas incluyen una pregunta o predicción y un resultado para comparar.

En el repositorio, `starter-files/` contiene los retos, `completed-examples/` reúne las soluciones y `scripts/` guarda el [guion del contenido base](scripts/guion-45-minutos.md) y los materiales de producción. El [README](README.md) explica cómo abrir los ejemplos y cargar la entrada estándar.

## Elaboración en equipo

**Universidad Peruana de Ciencias Aplicadas** · Ingeniería de Software\
**Periodo:** 202620 · **Curso:** 1ASI0729 Desarrollo de Aplicaciones Open Source\
**NRC:** 7750 · **Startup:** AI ToDu\
**Líder e integrante:** Kevin Salazar Marquina\
**Fecha de entrega:** 13 de noviembre de 2026

Kevin definió el enfoque en Java, la duración y el uso de humor en las prácticas, y seleccionó los memes que acompañan las demostraciones. El material del curso comprende el plan de seis lecciones, los programas iniciales y resueltos, las capturas de ejecución, la narración y el montaje de 60 minutos. [Historial de cambios del curso](https://github.com/AI-ToDu/java-fundamentals-course-ai-todu/commits/main/).

## Datos por completar antes de la entrega

- Publicar seis videos no listados en YouTube. Añadir en cada descripción el enlace a su práctica precargada y sustituir aquí los seis campos pendientes.
- Publicar y comprobar los enlaces directos a las seis prácticas desde una sesión sin iniciar sesión. Hay un enlace guardado para la primera lección y quedan cinco por crear. La prueba del índice fuera de rango del montaje usa una salida local de Java. Para ajustarla al requisito de demostrar código solo en editores en línea, repetir la prueba en JDoodle y sustituir esa evidencia antes de publicar la lección 6.
- Exportar este plan a `upc-pre-202620-1asi0729-7750-ai-todu-course-plan.pdf`. El líder completa por separado el informe de participación en Word y PDF.
