import serial
import time

# Open serial port
ser = serial.Serial(
	port='/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_DT044WO4-if00-port0',
	baudrate=9600,
	timeout=1,
	parity    = serial.PARITY_NONE,
	stopbits  = serial.STOPBITS_ONE,
	bytesize  = serial.EIGHTBITS,
)

# Send command
# ser.write(b'NP\r')
ser.write(b'GO 3\r')  # Move to position 3
ser.flush()

# Read response
time.sleep(0.1)
while ser.in_waiting:
    print(repr(ser.readline().decode(errors='ignore').strip()))


# Clean up
ser.close()
