"""Compile and execute the course examples. Production check, not a student requirement."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile


def run(command, **kwargs):
    result = subprocess.run(command, text=True, encoding="utf-8", capture_output=True,
                            timeout=30, **kwargs)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}\n{result.stdout}\n{result.stderr}")
    return result.stdout.replace("\r\n", "\n").strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jdk", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    java = args.jdk / "bin" / "java.exe"
    javac = args.jdk / "bin" / "javac.exe"
    results = []
    expected = {
        "01": ["Hola, mundo", "Hoy comienza nuestra aventura con Java."],
        "02": ["Energia despues de comer: 60", "Energia final: 45", "Tiene hambre: true",
               "Division entera 5 / 2: 2", "Division decimal 5.0 / 2: 2.5"],
        "03": ["La mascota necesita comer.", "Paso 1", "Paso 2", "Paso 3",
               "Energia al comer: 50", "Energia al comer: 60", "Energia final: 60"],
        "04": ["Hola, Luna", "Energia final: 70"],
        "05": ["Luna: 60", "Sol: 70", "Energia de Luna limitada: 100"],
        "06": ["Antes: Luna - 40", "Despues: Luna - 70", "Antes: Sol - 70",
               "Despues: Sol - 100", "Letras del nombre: 4", "Letras del nombre: 3"],
    }
    with tempfile.TemporaryDirectory(prefix="java-course-") as temp:
        temp = Path(temp)
        for group in ["starter-files", "completed-examples"]:
            for source in sorted((root / group).glob("*/Main.java")):
                lesson = source.parent.name
                build = temp / group / lesson
                build.mkdir(parents=True)
                run([str(javac), "-encoding", "UTF-8", "--release", "17", "-d",
                     str(build), str(source)])
                output = run([str(java), "-cp", str(build), "Main"], input="Luna\n30\n")
                if group == "completed-examples":
                    for line in expected[lesson]:
                        assert line in output.splitlines(), (lesson, line, output)
                results.append({"file": source.relative_to(root).as_posix(),
                                "compiled_release": 17, "executed": True})

        # Check real input handling and energy limits in the demonstrated flows.
        for lesson in ["04", "06"]:
            build = temp / "completed-examples" / lesson
            for value, message in [("abc", "La cantidad debe ser un numero entero."),
                                   ("-1", "La cantidad debe estar entre 0 y 100."),
                                   ("101", "La cantidad debe estar entre 0 y 100.")]:
                output = run([str(java), "-cp", str(build), "Main"], input=f"Luna\n{value}\n")
                assert message in output, (lesson, value, output)
                results.append({"lesson": lesson, "input": value, "rejected": True})
        build = temp / "completed-examples" / "06"
        for amount, luna, sol in [("0", 40, 70), ("100", 100, 100)]:
            output = run([str(java), "-cp", str(build), "Main"], input=f"Luna\n{amount}\n")
            assert f"Despues: Luna - {luna}" in output
            assert f"Despues: Sol - {sol}" in output
            results.append({"lesson": "06", "input": amount, "energy_limits": True})

        # Exercise the final class independently of the console UI.
        probe = temp / "MascotaCheck.java"
        probe.write_text('''public class MascotaCheck {
    public static void main(String[] args) {
        Mascota luna = new Mascota("Luna", -5);
        Mascota sol = new Mascota("Sol", 70);
        if (luna.getEnergia() != 0) throw new AssertionError("lower bound");
        luna.setEnergia(150);
        if (luna.getEnergia() != 100) throw new AssertionError("upper bound");
        luna.setEnergia(40);
        luna.alimentar(20);
        if (luna.getEnergia() != 60 || sol.getEnergia() != 70)
            throw new AssertionError("independent objects");
        luna.alimentar(-1);
        luna.alimentar(Integer.MAX_VALUE);
        if (luna.getEnergia() != 60) throw new AssertionError("invalid amount");
        System.out.println("OK");
    }
}
''', encoding="utf-8")
        run([str(javac), "--release", "17", "-cp", str(build), "-d", str(build), str(probe)])
        output = run([str(java), "-cp", str(build), "MascotaCheck"])
        assert output.endswith("OK")
        results.append({"class": "Mascota", "bounds_and_independence": True})

    report = {"status": "passed", "scope": "local Java compilation and execution",
              "source_release": 17, "checks": results,
              "not_verified": ["JDoodle shared links", "ElevenLabs audio", "final video duration"]}
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "checks": len(results), "programs": 12}, ensure_ascii=False))


if __name__ == "__main__":
    main()
