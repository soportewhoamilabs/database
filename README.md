# database
Repositorio Base de datos Whoami-labs
<?php
// Ejemplo de conexión a MySQL con credenciales incrustadas en el código
$servername = "localhost";
$username   = "admin_user";   // Usuario seteado directamente
$password   = "SuperSecret123"; // Contraseña seteada directamente
$dbname     = "mi_base_de_datos";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

echo "Conexión exitosa a la base de datos.";
?>
