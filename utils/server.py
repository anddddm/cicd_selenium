import http.server
import socketserver
import threading
import time
import os

class LocalServer:
    def __init__(self, port=8080, directory="."):
        self.port = port
        self.directory = os.path.abspath(directory)
        self.server = None
        self.thread = None
    
    def start(self):
        """Запуск сервера в отдельном потоке"""
        os.chdir(self.directory)
        
        handler = http.server.SimpleHTTPRequestHandler
        
        self.server = socketserver.TCPServer(
            ("", self.port), 
            handler,
            bind_and_activate=False
        )
        
        self.server.allow_reuse_address = True
        self.server.server_bind()
        self.server.server_activate()
        
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()
        
        time.sleep(2)
        print(f"Сервер запущен на http://localhost:{self.port}")
    
    def stop(self):
        """Остановка сервера"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            if self.thread:
                self.thread.join(timeout=5)
            print("Сервер остановлен")