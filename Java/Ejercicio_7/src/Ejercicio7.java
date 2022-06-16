
import java.util.Scanner;

/* Una compañia de venta de carros usados, paga a su personal
de ventas un salario de $1000 mensauales mas una comision de $150
por cada carro vendido, mas el 5% del valor de la venta por carro
Cada mes el capturista de la empresa ingresa en la comptadora
los datos pertinentes.
Hacer un programa que calcule e imprima el salario
mensual de un vendedor dado
El salario de 1000 lo vamos a manejar como un dato constante
pa asignarlo debemos usar la palabra reservada "final"*/


public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;
        
        System.out.println("Digite la cantidad de carros vendidos");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio de un carro");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision =venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        
        System.out.println("\nEl salario mensual es: " +  salarioMensual);
    }
}
