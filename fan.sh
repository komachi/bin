#!/bin/bash
CURRENT_LEVEL="$(grep 'level:' /proc/acpi/ibm/fan | cut -d':' -f2 | tr -d '\t')"

if [ "$CURRENT_LEVEL" = 'disengaged' ]; then
  NEW_LEVEL='auto'
else
  NEW_LEVEL='disengaged'
fi

echo "Changing from $CURRENT_LEVEL to $NEW_LEVEL"
echo "level $NEW_LEVEL" | sudo tee /proc/acpi/ibm/fan > /dev/null 2>&1