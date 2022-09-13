/*
Ejercicio 4: PEdir número hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclo04;

import java.util.Scanner;

public class Ciclo04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0; //inicializamos variables
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ // Bucle while, mientras el numero sea mayor o igual a cero
            System.out.println("El número " + numero + " es POSITIVO");
            conteo++;// va contando los numeros ingresados
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
            
    }
        System.out.println("Ha ingresado  " + conteo + " números no negativos" );
         }
}
