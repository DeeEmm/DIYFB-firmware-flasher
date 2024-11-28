#!/usr/bin/env bash
# rm -fr build dist
VERSION=0.0.1
NAME="DIYFB-Firmware-Flasher"
DIST_NAME="DIYFB-Firmware-Flasher"

pyinstaller --log-level=DEBUG \
            --noconfirm \
            build-on-mac.spec

# https://github.com/sindresorhus/create-dmg
create-dmg "dist/$NAME.app"
mv "$NAME $VERSION.dmg" "dist/$DIST_NAME.dmg"
