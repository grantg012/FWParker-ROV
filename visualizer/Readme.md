# Thruster Visualizer

### Running

1. Shift + Right click in windows explorer and choose "Open Powershell here"
2. In powershell, run `python visualizer.py`
3. THEN, start the ROV python code


### Setup

1. Install python (64bit)  
    a. Be sure to check tk and tcl when installing
2. Install `matplotlib`, `tk`, and `msvc-runtime` with pip. `pip install matplotlib`, etc...
3. Download `visualizer.py` and `fakeSerial.py` to the same folder as the other ROV code
4. In the ROV python code, add `import fakeSerial` to the top of the file
5. In the `writeToSerial()` function, add a call to the end `fakeSerial.writeToSerial(msg)`
