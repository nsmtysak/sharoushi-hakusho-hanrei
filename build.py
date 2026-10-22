"""sharoushi-hanrei-hakusho.html（アーティファクト用の本文）を、GitHub Pages で開ける index.html に包む。

使い方: python build.py
"""
import io
import pathlib

here = pathlib.Path(__file__).parent
body = io.open(here / "sharoushi-hanrei-hakusho.html", encoding="utf-8").read()

head = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2B3F8F">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font-size:14px}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

io.open(here / "index.html", "w", encoding="utf-8", newline="\n").write(
    head + body + "\n</html>\n"
)
print("index.html を作成しました")
