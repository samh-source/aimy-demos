#!/bin/bash
cd "$(dirname "$0")"
python gen.py 2>/dev/null || py gen.py
git add -A && git -c user.email=samh@betteraccountingsolutions.com -c user.name="Sam" commit -qm "update gallery" && git push -q origin master
echo "done: https://samh-source.github.io/aimy-demos/"
