"""Generate production texts from the authored scenes; does not generate audio or video."""

import json
from pathlib import Path
import re


def timecode(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def main():
    scripts = Path(__file__).resolve().parent
    scenes = json.loads((scripts / "escenas.json").read_text(encoding="utf-8"))
    voices = scripts / "elevenlabs"
    voices.mkdir(exist_ok=True)
    titles = {
        1: "Tu primer programa", 2: "Datos y operaciones", 3: "Decisiones y repeticiones",
        4: "Metodos y entrada de datos", 5: "Clases, objetos y encapsulacion",
        6: "Arrays y proyecto final",
    }
    pause_after = {
        "01-02": "En unos segundos las utilizaremos.",
        "01-05": "si necesitas más tiempo, pausa el video.",
        "02-03": "Antes de ejecutar, intenta calcular los resultados tú mismo.",
        "02-06": "Pausa si necesitas más tiempo.",
        "03-02": "¿qué mensaje esperas?",
        "03-04": "Antes de ejecutar un bucle, anota los valores que tendrá su variable.",
        "03-06": "Tómate un momento o pausa el video.",
        "04-06": "Tienes un momento para probar.",
        "05-04": "Enseguida comprobaremos esa predicción.",
        "05-06": "Cuando pedimos establecer ciento cincuenta, el objeto termina con cien.",
        "05-08": "Puedes pausar para completar el reto.",
        "06-02": "son números diferentes.",
        "06-06": "Puedes pausar el video para completar ambas partes.",
    }
    outline = ["# Guion de producción: Aprende Java creando una mascota virtual", "",
               "**Montaje previsto: 45:00.** Seis capítulos. Los tiempos incluyen voz, demostraciones y pausas.", "",
               "Los tiempos de voz son orientativos. Para la duración de los archivos y la ubicación de los clips "
               "consulta la guía de montaje. Los 45 minutos corresponden al video previsto.", "",
               "Las indicaciones de pantalla son para producción y no se leen. "
               "Todos los programas se demuestran en un editor Java en línea. "
               "El tiempo sin voz se utiliza para escribir, ejecutar, leer resultados y practicar; no para congelar imágenes.", ""]
    rows = ["| Escena | Inicio | Fin | Segundos | Palabras | Práctica mínima | Voz estimada a 125 ppm |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: |"]
    elapsed = 0
    chapters = {}
    chapter_durations = {}
    warnings = []
    total_words = 0
    chapter_counts = {}
    for scene in scenes:
        chapter = scene["chapter"]
        if chapter not in chapters:
            chapters[chapter] = []
            chapter_durations[chapter] = 0
            chapter_counts[chapter] = 0
            outline += [f"## Capítulo {chapter}. {titles[chapter]}", ""]
        chapter_counts[chapter] += 1
        scene_id = f"{chapter:02d}-{chapter_counts[chapter]:02d}"
        start, end = elapsed, elapsed + scene["duration"]
        words = len(re.findall(r"\b[\wáéíóúñü]+\b", scene["narration"]))
        speech_seconds = words / 125 * 60
        total_words += words
        if speech_seconds + scene["practice_seconds"] > scene["duration"]:
            warnings.append({"scene": scene_id, "reason": "speech plus practice exceeds slot",
                             "over_by_seconds": round(speech_seconds + scene["practice_seconds"] - scene["duration"], 1)})
        outline += [f"### {scene_id} · {timecode(start)}–{timecode(end)} · {scene['title']}", "",
                    f"**En pantalla:** {scene['screen']}", "",
                    f"**Narración:** {scene['narration']}", ""]
        if scene["practice_seconds"]:
            assert pause_after[scene_id] in scene["narration"], scene_id
            outline += [f"**Reserva de práctica:** {scene['practice_seconds']} segundos sin narración. "
                        f"Insertar la pausa después de «{pause_after[scene_id]}» y antes de la siguiente frase. "
                        "Cortar la pista de voz en ese punto; mostrar la solución después de la pausa. "
                        "Puede ampliarse al pausar el reproductor.", ""]
        outline += [f"**Tiempo de escena:** {scene['duration']} s. Voz orientativa: "
                    f"{speech_seconds:.1f} s a 125 palabras/minuto; el resto se dedica a la demostración.", ""]
        (voices / f"{scene_id}.txt").write_text(scene["narration"] + "\n", encoding="utf-8")
        chapters[chapter].append(scene["narration"])
        chapter_durations[chapter] += scene["duration"]
        rows.append(f"| {scene_id} | {timecode(start)} | {timecode(end)} | {scene['duration']} | "
                    f"{words} | {scene['practice_seconds']} s | {speech_seconds:.1f} s |")
        elapsed = end
    assert elapsed == 2700, elapsed
    assert chapter_durations == {1: 300, 2: 420, 3: 420, 4: 420, 5: 600, 6: 540}, chapter_durations
    for chapter, paragraphs in chapters.items():
        (voices / f"capitulo-{chapter:02d}.txt").write_text("\n\n".join(paragraphs) + "\n", encoding="utf-8")
    outline += ["## Hoja de tiempos", ""] + rows + ["",
                f"**Total:** {timecode(elapsed)}, {len(scenes)} escenas y {total_words} palabras de narración.", "",
                "Estas estimaciones no sustituyen la medición del audio generado ni garantizan el tiempo de la exportación.", ""]
    (scripts / "guion-45-minutos.md").write_text("\n".join(outline), encoding="utf-8")
    report = {"planned_duration_seconds": elapsed, "scene_count": len(scenes),
              "narration_words": total_words, "estimated_voice_seconds_at_125_wpm": round(total_words / 125 * 60, 1),
              "chapter_durations_seconds": chapter_durations, "warnings": warnings,
              "scope": "planning estimate, separate from production status"}
    (scripts / "tiempos-previstos.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
