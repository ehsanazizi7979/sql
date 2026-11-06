#!/usr/bin/env python3
"""Tiny static server for the Chapter 1 summary page.

Serves the directory, mapping "/" to chapter-01-summary.html so the
live preview opens straight onto the chapter summary.
"""
import http.server
import os
import socketserver

PORT = int(os.environ.get("PORT", "8000"))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DEFAULT = "chapter-01-summary.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/" + DEFAULT
        return super().do_GET()

    def end_headers(self):
        # Allow the page to be embedded in the Arena preview iframe.
        self.send_header("X-Frame-Options", "ALLOWALL")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Server(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving {DIRECTORY} on http://0.0.0.0:{PORT}/ -> {DEFAULT}", flush=True)
        httpd.serve_forever()
