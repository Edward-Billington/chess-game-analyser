#!/bin/sh
zstdcat /data/chess-games.pgn.zst | python src/main.py
