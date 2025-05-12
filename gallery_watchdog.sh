#!/bin/bash

WATCH_DIR="./gallery_images"

echo "👁️ Watching $WATCH_DIR for changes..."

inotifywait -m -r -e create -e modify -e delete --format '%w%f' "$WATCH_DIR" | while read file
do
    echo "🔄 Detected change: $file"
    ./../_support/autopush.sh
done
