
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
        // var entrada = new Scanner(System.in);
        /*System.out.println("Digite su edad: ");
        edad = Integer.parseInt ( entrada.nextLine());
        System.out.println("edad = " + edad);*/
        //conversion de tipos primitivos parte2
        /* var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
        int num1 = 5, num2 = 4;
        /* var solucion = num1 + num2;
        System.out.println("solucion de la suma  = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        
        solucion = num1 % num2; //Guarda el residuo de la division
        System.out.println("Solucion = " + solucion);
        
        if (num1 % 2 == 0);
          System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero Impar");*/

 /*int varNum1 = 1, varNum2 = 4;
      int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        //Operador de composicion
        varNum1 += 1; // varNum1 = varNum1 + 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 2;
        System.out.println("varNum3 = " + varNum1);
        
        varNum1 *= 5;
        System.out.println("varNum2 = " + varNum1);
        
        varNum1 /= 6;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 %= 6;
        System.out.println("varNum3 = " + varNum3);*/
        //Operadores Unarios
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); // el resultado sera negativo
        
        //Operador de negacion
        var varC = true; //Esta literal por defoult en java es de tipo boolean
        var varD  = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);

        var varE = 9;
        var varF = ++varE;
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
        
        
        //Postincremento (el simbolo va a depender de la variable)
        var varG = 3;
        var varH = varG++; //primero el valor de la variable luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores unarios de decremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); //La variable ya esta en decremento
        System.out.println("varJ = " + varJ);
        
        //Posdecremento
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);*/
        //Operadores de igualdad y relaciones
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum > bNum;
        System.out.println("gVar = " + gVar);
        
        if(aNum % 2 == 0)
            System.out.println("El numero es Par");
        else 
            System.out.println("El numero es Impar");
        
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto)
            System.out.println("Es mayor de edad");
        else
            System.out.println("Es menor de edad");*/
        /*var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre)
            System.out.println("Papá puede asistir al juego de su hijo");
        else
            System.out.println("Papá no puede asistir al juego de su hijo");*/
        
        
        //Operador ternario
       /* var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("Resultado = " + resultadoT);
        
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
       
       //Prioridad de los operadores
       var x = 5;
       var y = 10;
       var z = ++x + y--;
       System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4 + ((5*6) / 3) 
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        
        
    }
}
