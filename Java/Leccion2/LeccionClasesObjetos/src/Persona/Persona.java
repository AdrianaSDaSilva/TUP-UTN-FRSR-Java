
package Persona;

public class Java {
    //Atributos de la clase( Características)
    String nombre;
    String apellido;

//Métodos de la clase(Acciones)
    // un metodo puede recibir valores = argumentos
    // puede regresar un valor = valor de retorno
    // para definir un petodo comenzamos con public void el void es que no regresa ninguna informacion
    public void obtenerInformacion(){//los parentesis indican que pueden recibir informacion 
        System.out.println("Nombre: "+ nombre);
        // dentro de la clase podemos definir los atributos
        System.out.println("Apellido: "+apellido); // ctrl 7 nos muestra lo que tiene nuestra clase
      
        // como crear un objeto a partir de la clase PERSONA
        // Una clase es nuestra plantilla
        // el metodo main es para ejecutar, se recomienda hacerlo por fuera
    }

  }
