import sqlite3
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

# Conectar a la base de datos SQLite
conn = sqlite3.connect('usuarios.db', check_same_thread=False)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (nombre TEXT, apellido TEXT, registro TEXT, hash_contrasena TEXT)''')
conn.commit()

# Función para registrar usuarios
def registrar_usuario(nombre, apellido, registro, contrasena):
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
    cursor.execute("INSERT INTO usuarios (nombre, apellido, registro, hash_contrasena) VALUES (?, ?, ?, ?)",
                   (nombre, apellido, registro, hash_contrasena))
    conn.commit()
    return f"Usuario {nombre} registrado exitosamente."

# Función para validar usuarios
def validar_usuario(nombre, apellido, contrasena):
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND apellido=? AND hash_contrasena=?",
                   (nombre, apellido, hash_contrasena))
    resultado = cursor.fetchone()
    if resultado:
        return "Usuario validado correctamente."
    else:
        return "Nombre o contraseña incorrectos."

# Clase personalizada para manejar las solicitudes HTTP
class ManejadorHTTP(BaseHTTPRequestHandler):

    # Manejo de solicitudes GET
    def do_GET(self):
        if self.path == "/":
            self.mostrar_formulario()
        else:
            self.send_error(404, "Página no encontrada")

    # Manejo de solicitudes POST
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        datos = urlparse.parse_qs(post_data.decode('utf-8'))

        if self.path == "/registrar":
            nombre = datos['nombre'][0]
            apellido = datos['apellido'][0]
            registro = datos['registro'][0]
            contrasena = datos['contrasena'][0]
            respuesta = registrar_usuario(nombre, apellido, registro, contrasena)
            self.responder_html(respuesta)

        elif self.path == "/validar":
            nombre = datos['nombre'][0]
            apellido = datos['apellido'][0]
            contrasena = datos['contrasena'][0]
            respuesta = validar_usuario(nombre, apellido, contrasena)
            self.responder_html(respuesta)
        else:
            self.send_error(404, "Ruta no encontrada")

    # Responder con una página HTML
    def responder_html(self, contenido):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(contenido.encode('utf-8'))

    # Mostrar el formulario HTML
    def mostrar_formulario(self):
        formulario_html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Registro y Validación de Usuario</title>
        </head>
        <body>
            <h2>Registrar Usuario</h2>
            <form method="POST" action="/registrar">
                Nombre: <input type="text" name="nombre"><br>
                Apellido: <input type="text" name="apellido"><br>
                Registro: <input type="text" name="registro"><br>
                Contraseña: <input type="password" name="contrasena"><br>
                <input type="submit" value="Registrar">
            </form>

            <h2>Validar Usuario</h2>
            <form method="POST" action="/validar">
                Nombre: <input type="text" name="nombre"><br>
                Apellido: <input type="text" name="apellido"><br>
                Contraseña: <input type="password" name="contrasena"><br>
                <input type="submit" value="Validar">
            </form>
        </body>
        </html>
        '''
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(formulario_html.encode('utf-8'))

# Configuración del servidor HTTP
def run(server_class=HTTPServer, handler_class=ManejadorHTTP, port=7890):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor en ejecución en el puerto {port}")
    try:
        httpd.serve_forever()  # Mantener el servidor corriendo indefinidamente
    except KeyboardInterrupt:
        print("Servidor detenido manualmente.")
    finally:
        conn.close()  # Cerrar la conexión a la base de datos cuando el servidor se detiene

# Ejecutar el servidor
if __name__ == '__main__':
    run()