

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class Daocajero {

  private Connection con;
    private Statement st;
    private ResultSet rs;

    public Daocajero() {
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

                retorno = rs.getString("/*nombreAtributo*/");

            }
            st.close();
            Conexion.cerrarConexion();
        } catch (Exception e) {
            System.err.println("No se pudo realizar la consulta");
            return null;
        }
        return retorno;
    }



    public boolean eliminar(String value) {

      String eliminar = "DELETE FROM public."/*nombreTabla*/"
	WHERE \"/*idNombreAtributo*/\" = "+value;
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

    public boolean agregar(String value) throws ClassNotFoundException{
        String insertar = "INSERT INTO public."/*nombreTabla*/"(\n" +
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

public boolean modificar(String value,int id) throws ClassNotFoundException {
        String script = "update \"/*nombreTabla*/\" set \"/*nombreAtributoCambiar*/\"= "+value+"  \n" +
"WHERE \"/*idNombreAtributo*/\"="+id;
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



