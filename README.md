## TraceRoute Script

A secure and cross-platform Python script for performing traceroute operations to given domains. This script is designed with safety and robust error handling in mind.
Features

Cross-platform support (Windows and Unix-like systems).
Enhanced security against command injection.
Comprehensive error handling.
Clean, formatted output for easy reading.

## Prerequisites

Python 3.x
traceroute tool installed (for Unix-like systems)
tracert tool (default on Windows systems)

## Usage

Clone the repository:

bash

    git clone https://github.com/ishaiva/HopsTraceRoute.git
    cd HopsTraceRoute

Run the script with the desired domain:

bash

    python3 TraceRoute.py example.com

Example

Command:

bash

    python3 TraceRoute.py example.com

Output:

Traceroute to example.com
========================================
Hop 1: _gateway (192.168.1.1) 5.403 ms 5.384 ms 5.424 ms
----------------------------------------
Hop 2: isp-router1.example.net (203.0.113.1) 10.123 ms 10.124 ms 10.125 ms
----------------------------------------
Hop 3: 203.0.113.50 (203.0.113.50) 15.000 ms 15.001 ms 15.002 ms
----------------------------------------
...
Hop 14: cdn-edge.example-cdn.com (198.51.100.10) 50.123 ms 50.124 ms 50.125 ms
----------------------------------------
Hop 15: example.com (203.0.113.100) 55.123 ms 55.124 ms 55.125 ms
----------------------------------------

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
License

## MIT License

Copyright (c) [2023] [ishaiva]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
