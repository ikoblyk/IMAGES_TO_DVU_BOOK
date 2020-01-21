#!/bin/bash

namee="$1"

echo "creating djvu files..."
for name in $(ls | grep 'jpg') ; do c44 $name -slice 100 $(echo $name | sed -r 's/(.*)\.[^\.]+/\1/').djvu; done

echo "Creating final file..."
djvm -c $namee.djvu *.djvu
echo "Deleting unnecessary crap"
rm -f [^$namee]*.djvu
rm -f *.jpg
echo "All Done!"
