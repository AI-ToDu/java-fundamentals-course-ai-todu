# Aprende Java creando una mascota virtual

Curso introductorio de **45 minutos** dirigido a estudiantes de secundaria de 12 a 17 años. Aprenderás con programas de consola en Java y un editor gratuito en el navegador.

## Empezar

1. Abre [JDoodle para Java](https://www.jdoodle.com/online-java-compiler-ide).
2. Usa Java 17 o una versión posterior. Los ejemplos usan sintaxis compatible con Java 17.
3. Copia el contenido de un archivo `Main.java` de `starter-files` o `completed-examples` en el editor. Conserva el nombre de clase `Main`.
4. Ejecuta el programa. En las lecciones 4 y 6, introduce los datos indicados abajo en la entrada estándar del editor.

Para seguir las lecciones y ejecutar las prácticas solo necesitas el navegador.

## Contenido

- [Plan del curso](course-plan.md): seis lecciones, tiempos del video final, prácticas y enlaces.
- `starter-files/01` a `starter-files/06`: programas iniciales y retos comentados.
- `completed-examples/01` a `completed-examples/06`: soluciones completas e independientes.
- `scripts/guion-45-minutos.md`: narración por escenas e indicaciones de grabación.
- `scripts/elevenlabs/`: textos de narración por escena y capítulo, reutilizables en Clipchamp.
- [Galería de capturas](capturas/galeria.md): siete pantallas de los ejemplos ejecutados en JDoodle.
- `scripts/produccion.md`: pronunciación, grabación y montaje.
- `scripts/escenas.json`: tiempos y contenido de las escenas.
- `scripts/verificar.py`: compilación y comprobación de los ejemplos para producción.

## Entradas para las demostraciones

Lección 4:

```text
Luna
30
```

Lección 6:

```text
Luna
30
```

En ambos casos escribe el nombre en la primera línea y la cantidad de comida en la segunda. En JDoodle puede usarse la entrada estándar preparada antes de ejecutar.

## Proyecto final

El programa crea dos objetos `Mascota`, guarda ambos en un array y recorre ese array. Cada mascota tiene nombre y energía privados, un constructor, getters, un setter que mantiene la energía entre 0 y 100 y un método para alimentarla.

Los programas iniciales compilan, pero dejan actividades por completar en comentarios `TODO`. Los ejemplos resueltos permiten contrastar el resultado después de practicar.

## Verificación para quien produce el curso

Esta comprobación local requiere un JDK y Python; no forma parte de los requisitos del estudiante:

```text
python scripts/verificar.py --jdk "RUTA_AL_JDK"
```

El script compila con `--release 17`, ejecuta los programas y comprueba salidas e inputs representativos. El resultado local se guarda en `scripts/validacion-local.json` cuando se indica `--report`.

## Estado

El curso está montado en **seis videos independientes**. Las lecciones duran 5, 7, 7, 7, 10 y 9 minutos, respectivamente.

El plan del curso reúne los enlaces que faltan para la entrega académica.
