
package CondicionalEjercicio3;

import java.util.Scanner;


public class CondicionalEjercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero entre el 0 y el 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        if(calificacion >= 9 && calificacion <= 9){
            System.out.println("A");
    }
        else if(calificacion >= 8 && calificacion <= 8){
            System.out.println("B");
        }
        else if(calificacion >= 7 && calificacion <= 7){
            System.out.println("C");
        }
        else if(calificacion >= 6 && calificacion <= 6){
            System.out.println("D");
        }
        else
            System.out.println("Fuera de rango");
        System.out.println("calificacion = " + calificacion);
    }
}
