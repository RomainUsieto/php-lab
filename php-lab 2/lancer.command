#!/bin/sh
cd -- "$(dirname -- "$0")" || exit 1
PORT_PHP_LAB="${1:-8080}"
printf '\nPHP Lab : http://localhost:%s\nGarde ce terminal ouvert. Ctrl+C pour arrêter.\n\n' "$PORT_PHP_LAB"
exec python3 -m http.server "$PORT_PHP_LAB" --bind 127.0.0.1
