# Links to arduino library source code

[Radio Head](https://github.com/adafruit/RadioHead/blob/46ac392cc1a0e0d81ba3c4e4489e7d6b13795065/RH_ASK.h)

[Adafruit RTCLib for DS1307](https://github.com/adafruit/RTClib/blob/master/examples/ds1307/ds1307.ino)


## Cameras
https://krystof.io/mjpg-streamer-on-a-raspberry-pi-zero-w-with-a-usb-webcam-streaming-setup/
https://github.com/jacksonliam/mjpg-streamer/blob/master/mjpg-streamer-experimental/plugins/input_uvc/README.md
https://askubuntu.com/questions/214977/how-can-i-find-out-the-supported-webcam-resolutions

```bash
/usr/local/bin/mjpg_streamer -i "input_uvc.so -d /dev/video0 -f 30 -r 640x480" -o "output_http.so -p 8080 -w usr/local/bin/share.mjpg-streamer/www"

v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats
v4l2-ctl -d /dev/video0 --list-formats-ext

192.168.2.2:8080/stream_simple.html
192.168.2.10:8080/?action=stream

```
