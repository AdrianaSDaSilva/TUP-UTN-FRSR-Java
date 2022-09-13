// Ejercicio 3: Leer números hasta que se introduzca un cero
// Para cada uno indicar si es par o impar
//Primero lo haremos con la clase Scanner
// Luego con la clase JOptionPane

package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // Importamos la clase Scanner
        int numero; // creamos un variable de tipo entera vacía
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){ //Ciclo While, mientras
            if(numero % 2 == 0){ // Condicion para encontrar números pares
                System.out.println("El número ingresado " +numero + " es PAR" );
                
            }
            else {
                System.out.println("El número ingresado  " + numero + " es IMPAR");
            }
            System.out.println("Digite otro número");
            numero = Integer.parseInt(entrada.nextLine());
      }
        System.out.println("El número ingresado es " + numero + " finaliza el programa");
    }
}
