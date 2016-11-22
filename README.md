# ChipWhisperer API Example #1

The following is an example of usage of the ChipWhisperer API to perform the following functions:

## Programming ##

Objective: Command-line programmer that writes a .hex file. Optional GUI can be used too, but by default provides a simple command-line interface.

Status: Done

Running `cwlite_program.py simeplserial-aes-xmega.hex` should program the file into the XMEGA device, with the following output:

```
<BUNCH OF MESSAGES>
['OpenADC', 'Clock Setup', 'CLKGEN Settings', 'Multiply', 2],
['OpenADC', 'Clock Setup', 'CLKGEN Settings', 'Divide', 26],
['OpenADC', 'Clock Setup', 'ADC Clock', 'Reset ADC DCM', None],
['OpenADC', 'Clock Setup', 'ADC Clock', 'Phase Adjust', 0],
Detected XMEGA128D4
Attempting to program simeplserial-aes-xmega.hex to XMEGA
XMEGA Programming flash...
XMEGA Reading flash...
Verified flash OK, 3067 bytes
```

Note running the file on it's own will connect & open the GUI programmer.

## Send measurement queries from Matlab ##

Objective: Send simple encryption queries from Matlab, of the form measure_AES(plaintext,key), which would return a ciphertext and the leakage trace.

Status: TODO

## Send fault queries from Matlab ##

Send simple encryption + glitch queries, of the form glitch_AES(plaintext,key,cycle), which would return a faulty ciphertext (with some probability) and a leakage trace, and where the cycle parameter would refer to the cycle where we glitch the AES.

Status: TODO

