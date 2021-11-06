# Python PySerial Setup

1. If you don't have a need for python2 but have it installed, I'd recommend
uninstalling python2 from your system completely. If you can't, you will need
to run commands with `python3` and `pip3`. If you do remove it and have only
python3, you should be able to run all python scripts with just `python`.
    1. Check your install with `python --version`. 
2. We are using Python 3, so you will need to install the latest release from
[python.org](https://www.python.org/downloads/).
3. You will then need to install the libraries via [pip](https://pip.pypa.io/en/stable/),
which comes with python. We're installing [pyserial](https://pythonhosted.org/pyserial/)
to talk to an arduino and [pygame](https://www.pygame.org/news) to receive
controller inputs. The easy way is `pip install -r requirements.txt` with the
requirements.txt in this folder. Or you can run `pip install pyserial pygame`.
For more info, see [PyPi](https://pypi.org/project/pyserial/).
    1. **DO NOT** install `serial`; this is a different package (that
    unfortunately imports with the same name). If you do, you may need to remove
    both packages with `pip uninstall`.
4. Then in a python script, start it with:
```python
import serial
import pygame
```




### Other Resources
* [Serial Communication with Python and an Arduino (better)](https://pythonforundergradengineers.com/python-arduino-LED.html)
* [Serial Communication with Python and an Arduino](https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0)
* [Finding the right serial port](https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html)
* [Possible fix for if the serial port isn't working](https://askubuntu.com/questions/1056314/uploading-code-to-arduino-gives-me-the-error-avrdude-ser-open-cant-open-d)
