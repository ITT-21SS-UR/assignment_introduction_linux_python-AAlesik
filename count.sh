#!/bin/bash
URL="ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README"    # ⎫
FILENAME=${URL##*/}                                                              # ⎜
SPLITFILE=$FILENAME"_Split.txt"                                                  # ⎬ Setting path-variables up
SORTFILE=$FILENAME"_Sort.txt"                                                    # ⎭

rm -f $FILENAME       # ⎫
rm -f $SPLITFILE      # ⎬ Removing all files -- ...just in case...
rm -f $SORTFILE       # ⎭

wget $URL             # 〉Downloading File

cat $FILENAME | tr [:upper:] [:lower:] | tr [:blank:] '\n' | tr -d [:punct:] | sed -r '/^\s*$/d' > $SPLITFILE  # 〉Writing File with lower-case + split individual words per line
cat $SPLITFILE | sort | uniq -c  > $SORTFILE                                                                   # 〉Writing File with alphabetical sorted & counted words
cat $SORTFILE | sort -r | head -10 |tr -d [:blank:] | tr -d [:digit:]                                          # 〉Print top ten used words
