from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS
from time import sleep

class RARM:
    lastPos = [0, 0, 0, 0, 0, 0]
    def __init__(self, channel = ['9', '12', '17', '25', '26', '28'], port='/dev/ttyACM0'):
        """Initialize 6 DoF Robot arm

        Args:
            port (str, optional): Defaults to '/dev/ttyACM0' for jetson(ubuntu) or 'COMx' for windows.
            channel (list, optional): Defaults to ['9', '12', '17', '25', '26', '28'].
        """
        self.port = port
        self.channel = channel
        self.serial = Serial(port = self.port, baudrate = 115200, parity = PARITY_NONE, stopbits = STOPBITS_ONE, bytesize = EIGHTBITS, timeout = 1)
    def setPos(self, pos, time = 500, delay = 500):
        buf = ''
        for i in range(len(pos)):
            self.lastPos[i] = pos[i]
            buf += f'#{self.channel[i]}P{pos[i]}'
        buf+= f'T{time}D{delay}\r\n'
        self.serial.write(buf.encode())
        sleep(time/1000)
        sleep(1)