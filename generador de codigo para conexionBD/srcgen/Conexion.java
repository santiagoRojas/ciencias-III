

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Conexion {
  static Connection conn;
      public static Connection getConexion() throws ClassNotFoundException {

          String driver = "org.postgresql.Driver";
          String nameBD = "jdbc:postgresql://localhost:5432/baseDeDatos";
          String user = "usuario";
          String password = "contaseña";

          try {
                  Class.forName(driver);
                  conn = DriverManager.getConnection(nameBD, user, password);
                  //Si la conexion fue realizada con exito, muestra el sgte mensaje.

                  return conn;
                  }
                  //Si se produce una Excepcion y no nos podemos conectar, muestra el sgte. mensaje.
          catch(SQLException e) {
                  System.out.println("Se ha producido un error en la conexion a la base de datos Ejemplo! ");
                  return null;
              }
          }
  public static void cerrarConexion() {
      try {
          conn.close();
      } catch (SQLException e) {
          System.out.println("No se pudo cerrar la conexion");
      }
  }}

