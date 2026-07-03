#!/usr/bin/env python3
"""Serve the repo on localhost so the print sheets render in Chrome."""
import http.server
import socketserver
import webbrowser

PORT = 8788
URL = f"http://localhost:{PORT}/sheets/"


def main():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving print sheets at {URL}\n(Ctrl-C to stop)")
        try:
            webbrowser.open(URL)
        except Exception:
            pass
        httpd.serve_forever()


if __name__ == "__main__":
    main()
