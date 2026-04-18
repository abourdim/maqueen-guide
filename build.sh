#!/usr/bin/env bash
# Build the Maqueen guide from Python sources into index.html.
# Requires only Python 3.8+ (no external packages).

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🛠️  Building Maqueen guide..."
echo ""

cd src
python3 assembler.py

# Move the built file to repo root as index.html (for GitHub Pages)
if [ -f maqueen-guide.html ]; then
    mv maqueen-guide.html ../index.html
    SIZE=$(du -h ../index.html | cut -f1)
    echo ""
    echo "✅ Built ../index.html ($SIZE)"
    echo ""
    echo "Open index.html in your browser, or deploy to GitHub Pages:"
    echo "  Settings → Pages → Source: main branch / root"
else
    echo "❌ Build failed — no output file"
    exit 1
fi
