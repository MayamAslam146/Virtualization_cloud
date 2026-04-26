from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = b"""
        <!DOCTYPE html>
        <html>
        <body style="font-family:Arial; text-align:center; padding:50px; background:#4285f4; color:white">
            <h1>Google Kubernetes Engine (GKE)</h1>
            <h2>Lab 9 - Task 3 GKE Simulation</h2>
            <hr style="border:1px solid white">
            <p><b>Student Name:</b> Mayam Aslam</p>
            <p><b>Reg No:</b> Inft232101024</p>
            <p><b>University:</b> KFUEIT - Faculty of CS & IT</p>
            <hr style="border:1px solid white">
            <h3>Containerized App Running on GKE!</h3>
            <p>Cluster: my-lab-cluster</p>
            <p>Region: us-central1</p>
            <p>Port: 8090 - Active</p>
        </body>
        </html>
        """
        self.wfile.write(html)

print("GKE App starting on port 8090...")
server = HTTPServer(('0.0.0.0', 8090), Handler)
print("Container Running!")
server.serve_forever()
