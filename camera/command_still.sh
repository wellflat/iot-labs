#!/bin/sh

WIDTH=1600
HEIGHT=1200
TIME_DELAY=1000
#TIME_DELAY=3600000  ## 1 hour
QUORITY=95
DST_DIR=/var/www/html
IMAGE_NAME=image.jpg
#IMAGE_NAME=timelapse_%04d.jpg
TIME_LAPSE=60000  ## ms

echo 'capture image'
sudo raspistill -v -w $WIDTH -h $HEIGHT -t $TIME_DELAY -q $QUORITY -o $DST_DIR/$IMAGE_NAME
echo 'end.'

# timelapse mode
# echo 'timelapse mode'
# sudo raspistill -v -w $WIDTH -h $HEIGHT -t $TIME_DELAY -q $QUORITY -tl $TIME_LAPSE -o $DST_DIR/$IMAGE_NAME
# echo 'end.'
