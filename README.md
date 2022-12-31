# Simple port scanner for MicroPython

A simple socket port scanner for embeded microcontrollers with micropython, ESP32, ST32


### Usage 


### Upload to your board

Plug your board in your serial port 

```

mpremote cp portscan.py :


```


### Scan


```

>>> import portscan

>>> portscan("192.168.1.1","192.168.1.100")


```

