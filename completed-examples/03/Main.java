public class Main {
    public static void main(String[] args) {
        int energia = 40;

        if (energia < 50) {
            System.out.println("La mascota necesita comer.");
        } else {
            System.out.println("La mascota puede jugar.");
        }

        for (int paso = 1; paso <= 3; paso++) {
            System.out.println("Paso " + paso);
        }

        while (energia < 60) {
            energia = energia + 10;
            System.out.println("Energia al comer: " + energia);
        }

        System.out.println("Energia final: " + energia);
    }
}
