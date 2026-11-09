public class Main {
    public static void main(String[] args) {
        Mascota luna = new Mascota("Luna", 40);
        Mascota sol = new Mascota("Sol", 70);

        luna.alimentar(20);
        System.out.println(luna.getNombre() + ": " + luna.getEnergia());
        System.out.println(sol.getNombre() + ": " + sol.getEnergia());

        luna.setEnergia(150);
        System.out.println("Energia de Luna limitada: " + luna.getEnergia());
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
