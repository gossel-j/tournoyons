#!/bin/sh

cd src
zip -r ../tournoyons.zip *.py
cd ..
echo '#!/usr/bin/env python2.7' | cat - tournoyons.zip > tournoyons
chmod +x tournoyons
rm tournoyons.zip
