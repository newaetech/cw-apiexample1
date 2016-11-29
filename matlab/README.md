# ChipWhisperer MATLAB API Example

## Setup - ChipWhisperer

You will need to first install Python 2.7 + ChipWhisperer. Note you'll need match the type of Python to your MATLAB install (i.e., 64-bt Python if using 64-bit MATLAB).

The easiest method is to install WinPython - be sure to select the 2.7 version, you CANNOT USE Python 3.x with ChipWhisperer.

See https://wiki.newae.com/MATLAB_Control_of_CW-Lite for full details. Note you MUST INSTALL the ChipWhisperer Python package, and ensure it works stand-alone before attempting the MATLAB interface. The MATLAB interface provides little error reporting, so you'll have difficulty using it without first getting the system working stand-alone.

Again see https://wiki.newae.com/MATLAB_Control_of_CW-Lite for full details.

## Setup - MATLAB

If Python isn't in your system path, you'll need to set the value of ```pyversion```. You can easily check if it's in your path by simply seeing the current value of it:

```
>> pyversion

       version: ''
    executable: ''
       library: ''
          home: ''
      isloaded: 0
```

If it's not set, you can specify it:

```
pyversion 'C:\WinPython-64bit-2.7.9.5\python-2.7.9.amd64\python.exe'
```

Which you should then be able to confirm gives you sane values:

```

>> pyversion

       version: '2.7'
    executable: 'C:\WinPython-64bit-2.7.9.5\python-2.7.9.amd64\python.exe'
       library: 'C:\WinPython-64bit-2.7.9.5\python-2.7.9.amd64\python27.dll'
          home: 'C:\WinPython-64bit-2.7.9.5\python-2.7.9.amd64'
      isloaded: 0
```

This will let you import Python packages (including ChipWhisperer).

## Running Examples

Again see https://wiki.newae.com/MATLAB_Control_of_CW-Lite for full details, the following is a brief summary:

To run the examples, first set your MATLAB folder to the cw-apiexample\matlab folder. You should then be able to run the following from your MATLAB prompt:

```
cw = cwconnect()
[cipher, trace] = measure_AES(cw, [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15],[0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);
plot(trace)
```

Note you only have to run cwconnect() once, and then simply reuse the cw object. Trying to connect again may fail if the cw object still exists. If you get this error, you can run cw.disconnect() to close the existing object and reconnect.

