public class Main {
    public static void main(String[] args) {
        String nombre = "Luna";
        int energia = 40;
        int comida = 20;
        int costoDeJugar = 15;
        double peso = 3.5;
        boolean tieneHambre = energia < 50;

        int energiaDespuesDeComer = energia + comida;
        int energiaFinal = energiaDespuesDeComer - costoDeJugar;

        System.out.println("Nombre: " + nombre);
        System.out.println("Peso: " + peso + " kg");
        System.out.println("Tiene hambre: " + tieneHambre);
        System.out.println("Energia despues de comer: " + energiaDespuesDeComer);
        System.out.println("Energia final: " + energiaFinal);
        System.out.println("Doble de comida: " + (comida * 2));
        System.out.println("Division entera 5 / 2: " + (5 / 2));
        System.out.println("Division decimal 5.0 / 2: " + (5.0 / 2));
    }
}
