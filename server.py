# server.py
import http.server
import socketserver

PORT = 8081
Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving frontend on http://localhost:{PORT}/index.html")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
