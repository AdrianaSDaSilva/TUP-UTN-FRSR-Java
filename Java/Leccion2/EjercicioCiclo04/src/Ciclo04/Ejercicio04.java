/*
Ejercicio 4: PEdir número hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclo04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0; //inicializamos variables
      
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){ // Bucle while, mientras el numero sea mayor o igual a cero
           JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            conteo++;// va contando los numeros ingresados
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
                
    }
        JOptionPane.showMessageDialog(null, "Ha ingresado " + conteo + " números que no son negativos");
    }
}
