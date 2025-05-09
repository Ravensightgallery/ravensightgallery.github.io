#!/bin/bash

cd "$(dirname "$0")"

inotifywait -m -r -e modify,create,delete --format '%w%f' gallery_images | while read change; do
    echo "[🖼️ Watchdog] Detected change in: $change"
    
    python3 generate_gallery_pages.py && \
    git add *.html && \
    git commit -m "🔄 Auto-update triggered by change in $change" && \
    git push origin main

    notify-send "🦅 Raven Gallery Update" "Gallery updated due to change in:\n$change"
done
