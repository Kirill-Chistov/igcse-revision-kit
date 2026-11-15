#!/usr/bin/env python3
"""Run the revision tracker on your computer.

    python3 tools/tracker/serve.py            # then open http://localhost:8765
    python3 tools/tracker/serve.py --port 9000
    python3 tools/tracker/serve.py --check    # start, self-test, stop

Your data stays in me/progress.json and me/flashcards.json. Only this computer can reach the page
(it listens on 127.0.0.1). Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import common as c  # noqa: E402

LOCK = threading.Lock()
NAME = re.compile(r"^[A-Za-z0-9_.\-]+(/[0-9A-Za-z_\-]+)?$")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            return self._send(200, c.render_page("local").encode(), "text/html; charset=utf-8")
        if path == "/api/state":
            with LOCK:
                state = {"progress": c.load_progress(), "flashcards": c.load_cards()}
            return self._send(200, json.dumps(state, ensure_ascii=False).encode())
        self._send(404, b'{"error":"not found"}')

    def do_PUT(self):
        path = urllib.request.unquote(self.path.split("?")[0])
        try:
            if path.startswith("/api/progress/"):
                subj = path[len("/api/progress/"):]
                if not NAME.match(subj) or "/" in subj:
                    return self._send(400, b'{"error":"bad subject"}')
                points = self._body().get("points", {})
                with LOCK:  # re-read, so edits an agent made meanwhile to other subjects survive
                    d = c.load_progress()
                    if points:
                        d["points"][subj] = points
                    else:
                        d["points"].pop(subj, None)
                    c.save_json(c.PROGRESS, d)
                return self._send(200, b'{"ok":true}')
            if path.startswith("/api/decks/"):
                deck = path[len("/api/decks/"):]
                if not NAME.match(deck):
                    return self._send(400, b'{"error":"bad deck"}')
                body = self._body()
                with LOCK:
                    d = c.load_cards()
                    d["decks"][deck] = body
                    c.save_json(c.FLASHCARDS, d)
                return self._send(200, b'{"ok":true}')
        except (ValueError, json.JSONDecodeError) as e:
            return self._send(400, json.dumps({"error": str(e)}).encode())
        self._send(404, b'{"error":"not found"}')

    def do_DELETE(self):
        path = urllib.request.unquote(self.path.split("?")[0])
        if path.startswith("/api/decks/"):
            with LOCK:
                d = c.load_cards()
                d["decks"].pop(path[len("/api/decks/"):], None)
                c.save_json(c.FLASHCARDS, d)
            return self._send(200, b'{"ok":true}')
        self._send(404, b'{"error":"not found"}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--check", action="store_true", help="start, fetch the page and the data once, then stop")
    a = ap.parse_args()
    if not c.ME.exists():
        print("No me/ folder yet — run /setup with your AI agent first (showing every subject meanwhile).")
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    url = f"http://localhost:{a.port}"
    if a.check:
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        page = urllib.request.urlopen(url).read()
        state = json.loads(urllib.request.urlopen(url + "/api/state").read())
        srv.shutdown()
        n = len(c.spec_data()["subjects"])
        print(f"ok: page {len(page)//1024} KB, {n} subject(s), "
              f"{sum(len(v) for v in state['progress']['points'].values())} rated point(s), "
              f"{len(state['flashcards']['decks'])} deck(s)")
        return
    print(f"Revision tracker running at {url}  (Ctrl+C to stop)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
