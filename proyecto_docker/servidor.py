import http.server
import socketserver

PORT = 7529

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor web corriendo en el puerto {PORT}")
    httpd.serve_forever()
