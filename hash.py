#!/usr/bin/env python3
"""Regenerate the CSP hashes in vercel.json from the inline <style> and <script> in index.html.
Run after any edit to index.html:  python3 hash.py
"""
import base64, hashlib, io, json, re, sys, pathlib

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")

def block(tag):
    m = re.search(r"<%s[^>]*>(.*?)</%s>" % (tag, tag), html, re.S)
    if not m:
        sys.exit("no inline <%s> found in index.html" % tag)
    return "'sha256-%s'" % base64.b64encode(
        hashlib.sha256(m.group(1).encode("utf-8")).digest()).decode()

style, script = block("style"), block("script")

cfg_path = root / "vercel.json"
cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
for rule in cfg.get("headers", []):
    for h in rule.get("headers", []):
        if h["key"].lower() == "content-security-policy":
            h["value"] = re.sub(r"style-src [^;]*", "style-src " + style, h["value"])
            h["value"] = re.sub(r"script-src [^;]*", "script-src " + script, h["value"])
cfg_path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
print("style-src ", style)
print("script-src", script)
