
import java.util.Scanner;


public class HolaMundo {
    public static void main(String arg[]) {
/*        
//Escribo el codigo aqui
        System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienveniidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
        */
        
//Var = inferencia de tipos en Java
        /*var miVariableEntera2 =10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + Tab
        //Para ejecutar shift + F6
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        
        //Reglas para definir una variable en Java
        //Se recomiendo camel case, empieza con minuscula y luego cada palabra con mayuscula
        //no se pueden utilizar numeros como primer caracter
        //no se pueden utilizar caracteres especiales
        //si puede tener guion bajo
        //se puede usar el signo dolar
        //acentos no se recomiendan para evitar olvidos 
        
        // Concatenacion
        var usuario = "Osvaldo";
        var profesion = "Ingeniero";
        var union = profesion + " " + usuario;
        System.out.println("union = "  + union);
        */
        //Click derecho - format = ordena el código
        
        /*var a = 8;
        var b = 4;
        System.out.println(a + b);
        
        // Ejercicio: Caracteres Especiales en Java
        var nombre = "Natalia";
        System.out.println("Nueva Linea: \n" + nombre); //salto de linea
        System.out.println("Tabulador: \t" + nombre); // tabulador para centrar
        System.out.println("\t\t.:MENU:."); //doble tabulador
        System.out.println("Retroceso: \b\b" + nombre); //Retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas simples: \"" + nombre + "\"");*/
        
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Sigite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el Título: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2 + " " + usuario2);*/
        
        /*byte numEnteroByte = 10;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: " + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        
        int numEnteroInt = 10;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: " + Long.MAX_VALUE);*/
        
        /*float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor mínimo de float: " + Float.MIN_VALUE);
        System.out.println("El Valor maximo de float es: " + Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de double es: "+ Double.MIN_VALUE);
        System.out.println("El valor maximo de Double es: " + Double.MAX_VALUE);*/
        
        //Inferencias de tipos Var y tipos primitivos
        /*var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        
        
        //Tipos primitivos Char
        //Este tipo puede almacenar solo 1 caracter
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres Unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copiar y pegar de unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var miVariableChar1 = 'a';
        System.out.println("miVariableChar1 = " + miVariableChar1);
        
        var varCaracter1 = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        
        var varCaracterDecimal1 = (char)36; //Valor entero y le asigna un tipo int y se le agrega (char) para que lo reconozca como tal
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        
        var varCaracterSimbolo1 = '$'; //Un caracter especial, podemos copiar y pegar de unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);

        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        
        
        //Tipos primitivos Tipos Booleanos
       /* boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool) {//Variable booleana no es necesario poner == true
        System.out.println("La bandera es verde");
        }
        else{
                System.out.println("La bandera es roja");
        }
    
        //Con inferencias de tipos
         var varBool1 = false;
        System.out.println("varBool1 = " + varBool1);
        
        if(varBool1) {//Variable booleana no es necesario poner == true
        System.out.println("La bandera es verde");
        }
        else{
                System.out.println("La bandera es roja");
        }
        */
        //Algoritmo: ¿Es mayor de edad?
        /*var edad = 3;
        //var adulto = edad >= 18;
        if(edad >= 18) {
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }*/
        
        
        //Conversion de tipos primitivos
       /* var edad = Integer.parseInt("20"); //convertimos tipo string a entero
        System.out.println("edad = " + (edad + 1)); //concatenamos el entero + 1
        var valorPI = Double.parseDouble("3.1416"); //Convertimos de string a double
        System.out.println("valorPI = " + valorPI);*/
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        /*System.out.println("Digite su edad: ");
        edad = Integer.parseInt ( entrada.nextLine());
        System.out.println("edad = " + edad);*/

        
        //conversion de tipos primitivos parte2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
    }
}    
