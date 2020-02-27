#!/bin/bash
SERVICES=("tor" "i2pd" "docker" "syncthing" "rtorrent")

for service in "${SERVICES[@]}"; do
  systemctl is-active --quiet "$service" && echo -n "$service "
done
