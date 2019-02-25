

public class Persona {
       private String nombre;
       private String apellido;
      private Direccion direccion;
       private int edad;
      private Telefono telefono;
       private String correo;
       private Bool nuevo;

    public string getNombre(){
      return this.nombre;
    }
    public string getApellido(){
      return this.apellido;
    }
    public Direccion getDireccion(){
      return this.direccion;
    }
    public integer getEdad(){
      return this.edad;
    }
    public Telefono getTelefono(){
      return this.telefono;
    }
    public string getCorreo(){
      return this.correo;
    }
    public bool getNuevo(){
      return this.nuevo;
    }

      public void setNombre(string value){
        this.nombre = value;
      }

      public void setApellido(string value){
        this.apellido = value;
      }

      public void setdireccion(Direccion value){
        this.direccion = value;
      }

      public void setEdad(integer value){
        this.edad = value;
      }

      public void settelefono(Telefono value){
        this.telefono = value;
      }

      public void setCorreo(string value){
        this.correo = value;
      }

      public void setNuevo(bool value){
        this.nuevo = value;
      }


  }

