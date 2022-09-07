/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo
*/
package Ciclos01;

public class Ejercicio01 {
    public static void main(String[] args) {
       int numero, cuadrado;
        System.out.println("Digite un número: ");
     numero = Integer.parseInt(entrada.nextLine());
     while(numero >= 0){
         cuadrado = (int)Math.pow(numero, 2);
         System.out.println("El número "+ numero+"elevado al cuadrado es: "+cuadrado);
         System.out.println("Digite otro numero: ");
         numero = Integer.parseInt(entrada.nextLine());
    }
        System.out.println("El programa ha finalizado por número negativo"); 
    }
    
}
