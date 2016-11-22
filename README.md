# ChipWhisperer API Example #1

The following is an example of usage of the ChipWhisperer API to perform the following functions:

## Programming ##

Objective: Command-line programmer that writes a .hex file. Optional GUI can be used too, but by default provides a simple command-line interface.

Status: TODO

## Send measurement queries from Matlab ##

Objective: Send simple encryption queries from Matlab, of the form measure_AES(plaintext,key), which would return a ciphertext and the leakage trace.

Status: TODO

## Send fault queries from Matlab ##

Send simple encryption + glitch queries, of the form glitch_AES(plaintext,key,cycle), which would return a faulty ciphertext (with some probability) and a leakage trace, and where the cycle parameter would refer to the cycle where we glitch the AES.

Status: TODO

