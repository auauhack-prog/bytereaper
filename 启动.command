#!/bin/bash
cd "$(dirname "$0")"
echo "ByteReaper v1.0.0 — Binary Reverse Engineering Platform"
echo "========================================================"
[ -d "venv" ] || python3 -m venv venv
source venv/bin/activate
pip install -q -r requirements.txt 2>/dev/null
python3 graph.py
