# Producción del curso de 45 minutos

## Formato y ritmo

El video maestro dura **45:00 como objetivo de edición**, con cortes de capítulo en 00:00, 05:00, 12:00, 19:00, 26:00 y 36:00. Termina en 45:00. Esos mismos cortes permiten exportar seis lecciones de 5, 7, 7, 7, 10 y 9 minutos.

Usar capturas reales de un editor Java en línea. El código ocupa la mayor parte de la pantalla; las anotaciones señalan la línea relevante y desaparecen cuando dejan de ayudar. Grabar a 1920 × 1080 o más, con zoom suficiente para leer el código desde un teléfono. Mantener visibles únicamente las líneas que se explican cuando el archivo es largo.

Las pausas previstas se dedican a ejercicios, cambios de código, ejecución y lectura de resultados. No alargar el curso con pantallas inmóviles ni acelerar la voz hasta hacer difícil seguir los conceptos.

## Voz en Clipchamp

Proyecto: **Curso Java - Narración con Alex**. En **Grabar y crear → Texto a voz**, elegir **Español (Perú)** y **Alex**. Pegar únicamente el texto de la escena y pulsar **Guardar**. Los archivos de `scripts/elevenlabs/` contienen el texto limpio y también sirven para Clipchamp. Para agregar otra escena, mover primero el cabezal a la posición prevista; crear un elemento nuevo en lugar de editar el audio anterior.

Las 38 escenas quedaron guardadas en siete bloques consecutivos: bienvenida y resto del capítulo 1, más un bloque por cada uno de los capítulos 2 a 6. La exportación **Solo audio** está en `audio/narracion-completa-alex-java.m4a` y mide 28:29,923. La bienvenida se conserva además como archivo separado. Las posiciones reales de los bloques y su uso en el video están en `guia-de-montaje.md`.

Durante el montaje, dividir los bloques de voz en las transiciones indicadas por el guion y reservar las pausas de práctica antes de mostrar cada solución. Comprobar la pronunciación de identificadores Java y la sincronización con la grabación. La [guía oficial de texto a voz de Clipchamp](https://support.microsoft.com/es-es/clipchamp/how-to-use-the-text-to-speech-feature) describe el flujo de generación si es necesario rehacer una frase.

## Referencia de la prueba previa en ElevenLabs

- Voz en español latinoamericano, clara y cercana, adecuada para estudiantes de secundaria.
- Referencia inicial de ritmo: 125 palabras por minuto. Ajustar después de escuchar, sin asumir que un control numérico de velocidad equivale exactamente a ese ritmo.
- Generar por escena, usando los archivos `elevenlabs/01-01.txt`, etc. Los archivos `capitulo-01.txt`, etc. reúnen la narración como referencia, pero mezclar un capítulo completo dificulta corregir una escena puntual.
- No enviar al generador los tiempos, las indicaciones de pantalla ni estas instrucciones.
- Escuchar una escena piloto antes de gastar créditos en todo el curso.
- No colocar claves de API en código o recursos públicos. Para este flujo basta generar y descargar las pistas desde la interfaz de ElevenLabs.

Revisar que la voz pronuncie con claridad Java, Main, String, Scanner, boolean, getter y setter. Mantener los identificadores reales en pantalla aunque la narración describa su función en español. Escuchar cada transición entre escenas para conservar volumen y tono coherentes.

Se generó una primera muestra en la cuenta de ElevenLabs del usuario: `audio/01-01-bienvenida.mp3`, voz David - Clear, Warm and Patient, español latinoamericano, modelo Eleven v4, estabilidad 0,5 y similitud 0,75. La interfaz mostró unos 35 segundos de duración. La generación consumió 588 créditos y quedaron 9.412. La duración todavía no se ha ajustado a los 60 segundos previstos para toda la escena; ese bloque también incluye la demostración inicial.

Los guiones suman 22.973 caracteres: con el consumo observado de un crédito por carácter, la cuota de ElevenLabs no alcanzaba para toda la narración. Esta pista queda como referencia. Si se reutiliza al publicar, revisar los requisitos de atribución de ElevenLabs junto con la restricción académica de branding.

Fuentes consultadas el 8 de noviembre de 2026:

- [Planes de ElevenLabs](https://elevenlabs.io/pricing).
- [Condiciones de publicación y atribución](https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform).
- [Editor Java de JDoodle](https://www.jdoodle.com/online-java-compiler-ide).

## Grabación

1. Cargar el archivo Java correspondiente a la lección. Todos los ejemplos son independientes; no compilar todos los `Main.java` como un solo proyecto.
2. Ensayar las acciones de cada escena con los textos de pantalla como guía.
3. Preparar la entrada estándar cuando corresponda. Para las lecciones 4 y 6, la demostración principal usa `Luna` y `30` en líneas separadas.
4. Grabar la escritura progresiva de los fragmentos que se explican. Puede pegarse el archivo completo al iniciar y luego enfocar bloques concretos, sin simular que una imagen ejecuta Java.
5. Mostrar el resultado después de cada cambio significativo. El video debe demostrar la ejecución real del código mostrado.
6. Al provocar un error de sintaxis para explicarlo, restaurar la versión correcta antes de continuar.
7. Mantener fuera del encuadre datos personales de cuentas y notificaciones.

## Montaje a 45:00

Crear una secuencia de 2700 segundos y ubicar cada escena según la hoja de tiempos de `guion-45-minutos.md`. Medir la duración real de cada pista de voz, no solo el número de palabras.

Cuando una escena incluya un reto, el guion identifica la frase exacta después de la cual insertar el silencio de práctica. Cortar el audio en ese punto, mantener el reto visible durante el tiempo indicado y después continuar con la explicación de la solución. No dejar que la pista revele la respuesta antes de la pausa.

Si la voz supera el espacio de una escena, acortar la explicación sin perder el concepto o volver a generar con un ritmo comprensible. Si queda espacio, dedicarlo a una acción visible de código o a la lectura del resultado. Respetar los tiempos de práctica mínimos antes de mostrar la solución.

El guion contiene margen para demostraciones y práctica; el ritmo final depende del audio y de la grabación. No se garantiza una duración audiovisual solo porque las celdas de la hoja de tiempos sumen 45 minutos.

Incluir subtítulos revisados manualmente, especialmente en identificadores Java. Verificar que código, narración y subtítulos expliquen lo mismo. No colocar nombres o logos de autores en el contenido ni comentarios de autoría en los archivos Java.

Al exportar, verificar metadatos y duración reproducible de **45:00**, además de sincronización, legibilidad y ausencia de cortes de palabras. Exportar también las seis lecciones si se desea seguir el formato de secuencia de videos del enunciado.

## Publicación y evidencias

Antes de entregar, crear los enlaces precargados de las seis prácticas y abrirlos desde una ventana privada. El estudiante debe poder ejecutar el ejemplo con herramientas gratuitas en el navegador. El enlace general de JDoodle no sustituye un enlace precargado.

Publicar el código en un repositorio llamado `java-fundamentals-course-[equipo]` de una organización pública de GitHub y conservar las carpetas exigidas. Cada integrante debe aportar mediante commits propios y reales. Subir los videos como no listados a YouTube y agregar enlaces a práctica y repositorio en cada descripción.

Completar los datos del equipo en el plan, exportarlo a PDF y preparar el informe de participación en Word y PDF con la evaluación real del líder. Estos pasos están pendientes y el paquete no debe presentarse como evidencia de su realización.
