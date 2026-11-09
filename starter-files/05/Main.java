public class Main {
    public static void main(String[] args) {
        Mascota luna = new Mascota("Luna", 40);
        System.out.println(luna.getNombre() + ": " + luna.getEnergia());
        // TODO: crea otra mascota llamada Sol con energia 70.
        // TODO: agrega setEnergia con limites de 0 y 100.
        // TODO: agrega alimentar y alimenta solamente a Luna.
    }
}

class Mascota {
    private String nombre;
    private int energia;

    Mascota(String nombre, int energia) {
        this.nombre = nombre;
        // Etapa inicial: el reto agrega validacion antes de publicar la solucion.
        this.energia = energia;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEnergia() {
        return energia;
    }
}
