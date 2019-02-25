

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Personadao {

  private Connection con;
    private Statement st;
    private ResultSet rs;

    public Personadao() {
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
                
            }
            st.close();
            Conexion.cerrarConexion();
        } catch (Exception e) {
            System.err.println("No se pudo realizar la consulta");
            return null;
        }
        return Persona;
    }

    public boolean eliminar(int id) {

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


