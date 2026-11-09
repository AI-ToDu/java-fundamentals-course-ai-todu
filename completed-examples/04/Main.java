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

        saludar(nombre);
        int energiaFinal = calcularEnergia(40, cantidad);
        System.out.println("Energia final: " + energiaFinal);
        entrada.close();
    }

    static void saludar(String nombre) {
        System.out.println("Hola, " + nombre);
    }

    static int calcularEnergia(int energiaActual, int cantidad) {
        int resultado = energiaActual + cantidad;
        if (resultado > 100) {
            return 100;
        }
        return resultado;
    }
}
