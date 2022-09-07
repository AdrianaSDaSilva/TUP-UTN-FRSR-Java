package CicloWhile;

/* ciclos son condiciones que se repiten, en caso de que se cumpla cierta condicion se repite el ciclo*/
/* El ciclo While viene del ciclo MIENTRAS de PseInt*/
public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; // Inferencia de tipos
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; // Vamos aumentando en uno la variable
        }
        var conteo2 = 0; // Inferencia de tipos
        while (conteo2 <= 7) { // aqui cuenta has el 7 inclusive
            System.out.println("conteo2 = " + conteo2);
            conteo2++;
        }

        // CICLO DO WHILE
        // equivale con el REPETIR HASTA QUE de pSeint
        // Diferencia con el anterior es la forma en que se ejecuta
        // Cambia el orden en que se ejecutan las lineas de codigo
        // en while primero ven la condicion y despues entraban a las lineas de codigo
        // en este caso es diferente, lo primero que lleva es el DO
        // y luego las lineas de codigo, al final está la condicion que hara que se
        // repita o salga del ciclo
        // primero ejecuta el codigo y luego hace la comprobación
        // en este por lo menos una vez se ejecuta el código

        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++; // para que no se vuelva infinito
        } while (contador < 7); // es necesario poner el punto y coma para que funcione

        // CICLO FOR
        // maneja un numero determinado de iteraciones a diferencia
        // del while y do while
        for (var contador1 = 0; contador1 < 7; contador1++) {
            // el primer lugar es para declarar una variable de tipo contador o iterador
            // el segundo lugar es para poner la condicion a cumplir
            // el tercer lugar es para poner el incremento o decremento del contador
            System.out.println("contador1 = " + contador1);
        }

        // palabras break y continue
        // Break: nos permite romper un ciclo
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break; // asi solo se muestra el 0, si lo sacamos imprime todos los pares
            }
        }

        // Continue
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 != 0) {
                continue; // vamos a la siguiente iteracion
            }
            System.out.println("contando = " + contando);
        }

        // Uso de Etiquetas (Labels)
        // es otro ciclo for bucle
        inicio: // Etiqueta
        for (var contando1 = 0; contando1 < 7; contando1++) {
            if (contando1 % 2 != 0) {
                continue inicio;

            }
            System.out.println("contando1 = " + contando1);
        }

    }
}
