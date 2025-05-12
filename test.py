#!/usr/bin/env python3
"""
Simple HTTP Server for serving the China Bushcraft Community PDF viewer.
This script starts a web server on port 8088 with the current directory as the root.
No administrator/root privileges required for port 8088.

Usage:
    python3 test.py
"""

import http.server
import socketserver
import os
import sys

PORT = 8088
DIRECTORY = os.getcwd()  # Use current directory as web root

class Handler(http.server.SimpleHTTPRequestHandler):
    # Set default directory to serve
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    # Override log messages to show server activity
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}")

def main():
    # Check if running with proper permissions for port 80
    if os.name != 'nt' and os.geteuid() != 0 and PORT < 1024:
        print("Error: You need root privileges to use port 80.")
        print("Try: sudo python3 test.py")
        print("Alternative: Change PORT to a value above 1024 (e.g., 8080) to run without root.")
        sys.exit(1)
    
    try:
        # Create the server
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Server started at http://localhost:{PORT}")
            print(f"Serving files from: {DIRECTORY}")
            print("Press Ctrl+C to stop the server")
            
            # Serve until interrupted
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except PermissionError:
        print(f"Error: Permission denied for port {PORT}")
        print("On Windows, try running as Administrator")
        print("On Unix/Linux, try: sudo python3 test.py")
        print("Alternative: Change PORT to a value above 1024 (e.g., 8080) to run without admin rights")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
