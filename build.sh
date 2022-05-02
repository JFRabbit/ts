#!/usr/bin/env bash
# rm dist
rm -rf dist
# package
./venv/bin/pyinstaller -F ts.py --clean
