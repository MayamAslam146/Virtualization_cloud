from http.server import HTTPServer, BaseHTTPRequestHandler

class AzureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <body style="font-family:Arial; text-align:center; padding:50px; background:#0078d4; color:white">
            <h1>☁️ Microsoft Azure Virtual Machine</h1>
            <h2>Lab 9 - Task 2 Azure VM Simulation</h2>
            <hr style="border:1px solid white">
            <p><b>Student Name:</b> Mayam Aslam</p>
            <p><b>Reg No:</b> Inft232101024</p>
            <p><b>University:</b> KFUEIT - Faculty of CS & IT</p>
            <hr style="border:1px solid white">
            <h3>✅ Nginx Web Server is Running!</h3>
            <p>VM Size: Standard B1s</p>
            <p>OS: Ubuntu Server 22.04 LTS</p>
            <p>Port 3000 - Active</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

print("Azure VM Server starting on port 3000...")
server = HTTPServer(('0.0.0.0', 3000), AzureHandler)
print("Server running!")
server.serve_forever()
