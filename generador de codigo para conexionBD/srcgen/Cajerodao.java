

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Cajerodao {

  private Connection con;
    private Statement st;
    private ResultSet rs;

    public Cajerodao() {
        con = null;
        st = null;
        rs=null;
    }


    public string consultar(int id){
      String retorno;
        String consulta = "SELECT * FROM public.\"/*nombreTabla*/ \n" +
"WHERE \"/* idnombreTabla */\" = "+id;
        try {
            con = Conexion.getConexion();
            st = con.createStatement();
            rs = st.executeQuery(consulta);
            if(rs.next()){

                retorno = rs.getString("nombreAtributo");

            }
            st.close();
            Conexion.cerrarConexion();
        } catch (Exception e) {
            System.err.println("No se pudo realizar la consulta");
            return null;
        }
        return retorno;
    }



    public boolean eliminar(String id) {

      String eliminar = "DELETE FROM public."/*nombreTabla*/"
	WHERE \"/*idnombreTabla*/\" = "+id;
      try {
          con = Conexion.getConexion();
          st = con.createStatement();
          st.executeUpdate(eliminar);
          st.close();
          Conexion.cerrarConexion();
          return true;
      } catch (SQLException e) {
          System.out.println("No se puedo realizar la modificacion");
      }
      return false;
  }



