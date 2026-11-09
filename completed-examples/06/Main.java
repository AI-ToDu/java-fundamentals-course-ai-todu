import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escribe el nombre de tu mascota:");
        String nombre = entrada.nextLine();
        System.out.println("Escribe una cantidad de comida entera, de 0 a 100:");

        if (!entrada.hasNextInt()) {
            System.out.println("La cantidad debe ser un numero entero.");
            entrada.close();
            return;
        }

        int cantidad = entrada.nextInt();
        if (cantidad < 0 || cantidad > 100) {
            System.out.println("La cantidad debe estar entre 0 y 100.");
            entrada.close();
            return;
        }

        Mascota[] mascotas = {
            new Mascota(nombre, 40),
            new Mascota("Sol", 70)
        };

        for (int indice = 0; indice < mascotas.length; indice++) {
            Mascota mascota = mascotas[indice];
            System.out.println("Antes: " + mascota.getNombre() + " - " + mascota.getEnergia());
            mascota.alimentar(cantidad);
            System.out.println("Despues: " + mascota.getNombre() + " - " + mascota.getEnergia());
            System.out.println("Letras del nombre: " + mascota.getNombre().length());
        }

        entrada.close();
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
