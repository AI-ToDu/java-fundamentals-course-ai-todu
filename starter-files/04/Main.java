import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escribe el nombre de tu mascota:");
        String nombre = entrada.nextLine();
        saludar(nombre);
        // TODO: lee y valida una cantidad entera de comida entre 0 y 100.
        // TODO: crea calcularEnergia y muestra su valor de retorno.
        entrada.close();
    }

    static void saludar(String nombre) {
        System.out.println("Hola, " + nombre);
    }
}
