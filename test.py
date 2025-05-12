#!/usr/bin/env python3
"""
Simple HTTP Server for serving the China Bushcraft Community PDF viewer.
This script starts a web server on port 8088 that can be accessed from any IP address.
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
HOST = "0.0.0.0"  # 使用0.0.0.0表示监听所有可用的网络接口

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
        print("错误：使用低于1024的端口需要root权限。")
        print("尝试：sudo python3 test.py")
        print("替代方案：将PORT更改为1024以上的值（例如8080）以无需root权限运行。")
        sys.exit(1)
    
    try:
        # Create the server
        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            print(f"服务器已启动，可通过以下地址访问：")
            print(f"http://{HOST}:{PORT} (任何IP)")
            print(f"http://localhost:{PORT} (本地)")
            print(f"服务文件目录：{DIRECTORY}")
            print("按Ctrl+C停止服务器")
            
            # Serve until interrupted
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已被用户停止")
    except PermissionError:
        print(f"错误：没有端口{PORT}的权限")
        print("在Windows上，尝试以管理员身份运行")
        print("在Unix/Linux上，尝试：sudo python3 test.py")
        print("替代方案：将PORT更改为1024以上的值（例如8080）以无需管理员权限运行")
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    main()
