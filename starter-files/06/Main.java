public class Main {
    public static void main(String[] args) {
        Mascota[] mascotas = {
            new Mascota("Luna", 40),
            new Mascota("Sol", 70)
        };
        System.out.println("Cantidad de mascotas: " + mascotas.length);
        // TODO: recorre el array con un for.
        // TODO: alimenta a cada mascota y muestra su energia.
        // TODO: agrega una tercera mascota.
        // TODO: integra Scanner como en la leccion 4.
    }
}

class Mascota {
    private String nombre;
    private int energia;

    Mascota(String nombre, int energia) {
        this.nombre = nombre;
        setEnergia(energia);
    }

    public String getNombre() {
        return nombre;
    }

    public int getEnergia() {
        return energia;
    }

    public void setEnergia(int nuevaEnergia) {
        if (nuevaEnergia < 0) {
            energia = 0;
        } else if (nuevaEnergia > 100) {
            energia = 100;
        } else {
            energia = nuevaEnergia;
        }
    }

    public void alimentar(int cantidad) {
        if (cantidad < 0 || cantidad > 100) {
            System.out.println("La cantidad debe estar entre 0 y 100.");
            return;
        }
        setEnergia(energia + cantidad);
    }
}
