
package ClasesObjetos;


public class Persona {
    // Atributos de la clase(caracteristicas)
    String nombre;
    String apellido;
    
    //Métodos de la clase (acciones)
    // los metodos se pueden reutilizar y llamar las veces que sean necesarias
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
}
