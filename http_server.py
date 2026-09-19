python
"""
Простейший HTTP-сервер на Python (без Flask).
Демонстрирует базовую работу с HTTP.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello, AppSec!")


if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), Handler)
    print("Сервер запущен на http://localhost:8000")
    print("Открой в браузере и увидишь 'Hello, AppSec!'")
    print("Для остановки: Ctrl+C")
    server.serve_forever()
