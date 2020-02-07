import http.server
import socketserver

PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)

print(f'http://localhost:{PORT}')

httpd.serve_forever()