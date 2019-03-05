

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class Daopersona {

  private Connection con;
    private Statement st;
    private ResultSet rs;

    public Daopersona() {
        con = null;
        st = null;
        rs=null;
    }



    public Persona consultar(int id){
        Persona = null;
        String consulta = "SELECT * FROM public.\"Persona \n" +
"WHERE \"idPersona\" = "+id;
        try {
            con = Conexion.getConexion();
            st = con.createStatement();
            rs = st.executeQuery(consulta);
            if(rs.next()){
                Persona = new Persona();
                //recorrer las entidades que hay para sacar las variables y consultarlas
            }
            st.close();
            Conexion.cerrarConexion();
        } catch (Exception e) {
            System.err.println("No se pudo realizar la consulta");
            return null;
        }
        return Persona;
    }

    public boolean eliminarPersona(int id) {

      String eliminar = "DELETE FROM public.Persona WHERE idPersona = "+id;
      try {
          con = Conexion.getConexion();
          st = con.createStatement();
          st.executeUpdate(eliminar);
          st.close();
          Conexion.cerrarConexion();
          return true;
      } catch (SQLException e) {
          System.out.println("No se puedo realizar la eliminacion");
      }
      return false;
  }

    public boolean agregarPersona(Persona value) throws ClassNotFoundException{
        String insertar = "INSERT INTO public.\"Persona\"(\n" +
"	?,?)\n" +
"	VALUES (?,?)";
        try {
            con = Conexion.getConexion();
            st = con.createStatement();
            st.executeUpdate(insertar);
            st.close();
            Conexion.cerrarConexion();
            return true;
        } catch (SQLException e) {
            System.out.println("no se pudo realizar el agregado");
        }
        return false;
}
  public boolean modificarPersona(/*tipoAtributoCambiar*/ value,int id) throws ClassNotFoundException {
          String script = "update \"Persona\" set \"/*nombreAtributoCambiar*/\"= "+value+"  \n" +
  "WHERE \"idPersona\"="+id;
          try {
              con = Conexion.getConexion();
              st = con.createStatement();
              st.executeUpdate(script);
              st.close();
              Conexion.cerrarConexion();
              return true;
          } catch (SQLException e) {
              System.out.println("No se puedo realizar la modificacion");
          }
          return false;
      }



