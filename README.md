# Basic port scanner

A simple command line Python script which allows TCP ports to be scanned on a specified host

## Features:
- Scans ports 1 to 65535 using TCP
- Resolves domain names to DNS addresses
- Displays scan start time and target information
- Handles exceptions like keyboard interrupts (Ctrl + C) and DNS errors

## Future improvements:
- Add multithreading for faster scans
- Add banner grabbing to detect services
- Filter for common ports only
- Save output to a file

## How to use:
- python port_scanner.py <target>
- e.g. python port_scanner.py 127.0.0.1

## What I learned:
- Python scripting fundamentals
- Port scanning logic
- How tedious script building can be
