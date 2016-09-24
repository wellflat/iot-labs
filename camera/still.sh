#!/bin/sh

WIDTH=1600
HEIGHT=1200
TIME_DELAY=1
QUORITY=100
DST_DIR=/var/www/html
IMAGE_NAME=image.jpg

sudo raspistill -v -w $WIDTH -h $HEIGHT -t $TIME_DELAY -q $QUORITY -o $DST_DIR/$IMAGE_NAME
