# version 1.0
# uses pyserial
import serial

class SerialDevice :
    port =""
    baudrate = 9600
    timeout = 2
    encoding = "utf-8"
    # serial_dev

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600, timeout=2) :
        self.port = port
        self.baudrate = baudrate
        self.timeout=timeout
        self.serial_dev = serial.Serial(port=self.port,
                                        baudrate=self.baudrate,
                                        bytesize=serial.EIGHTBITS,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        timeout=self.timeout)

    def close(self):
        self.serial_dev.close()

    def send(self, str_data):
        command = str_data.encode(self.encoding)

        try:
            self.serial_dev.write(command)
        except serial.SerialException as e:
            # tmp
            print("Serial exception!")

    def get_response(self):
        response=""
        try:
            response=self.serial_dev.readline().decode(self.encoding).strip() #arduino finish string with \n
        except serial.SerialException as e:
            # tmp
            print("Serial exception!")
        return response