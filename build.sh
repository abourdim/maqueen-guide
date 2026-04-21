#!/usr/bin/env bash
# Build the Maqueen guide from Python sources into index.html.
# Requires only Python 3.8+ (no external packages).

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🛠️  Building Maqueen guide..."
echo ""

python3 src/assembler.py

if [ -f index.html ]; then
    SIZE=$(du -h index.html | cut -f1)
    echo ""
    echo "✅ Built index.html ($SIZE)"
    echo ""
    echo "Open index.html in your browser, or deploy to GitHub Pages:"
    echo "  Settings → Pages → Source: GitHub Actions"
else
    echo "❌ Build failed — no output file"
    exit 1
fi
