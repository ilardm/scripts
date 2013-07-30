#!/bin/bash
#
# pdfs2djvu
#

if [ -z `which pdftoppm` -o -z `which cjb2` -o -z `which djvm` ]; then
echo
echo "Error: pdftoppm, cjb2 and djvm are needed"
echo
exit 1
fi

shopt -s extglob

OUTFILE="#0.djvu"
DEFMASK="*.pdf"
DPI=600

if [ -n "$1" ]; then
MASK=$1
else
MASK=$DEFMASK
fi

for PDF in $MASK; do
if [ ! -e $PDF ]; then
echo
echo "Error: current directory must contain files with the mask $MASK"
echo
exit 1
fi
echo $PDF
pdftoppm -mono -r 600 -aa yes $PDF $PDF
for PBM in $PDF*.pbm; do
echo $PBM
cjb2 -dpi $DPI $PBM $PBM.djvu
rm -f $PBM
done
done

djvm -c $OUTFILE $MASK*.pbm.djvu
