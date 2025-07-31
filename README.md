# pywilbox

A Python class to control the Wilbox hardware device, including VICI valves and pump relays.

## Installation

Installation steps:

(1) Set up a virtual environment:
	
	python3 -m venv path/to/wilboxenv
	source path/to/wilboxenv/bin/activate

(2) Manually install pyusb in your Python venv first:

	pip install pyusb

(3) install pywilbox package:
	
	pip install pywilbox
	(or for source development: pip install -e pywilbox )

## Usage

```python
from pywilbox import Wilbox

box = Wilbox("/dev/ttyUSB0")
box.pump_on()
```
