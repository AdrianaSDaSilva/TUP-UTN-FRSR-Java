/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y 
luego ir pidiendo número indicando "es mayor" o 
" es menor" según corresponda
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos
 */
package Ciclos05;

import java.util.Scanner;


public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //metodo random es tipo double, esto va a generar un número aleatorio
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un número mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un número menor");
            }
            else{
                System.out.println("\tFELICIDADES!!! Has adivinado el número");
                
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("\tAdivinaste el número en: " + conteo + " intentos");
    }
}
