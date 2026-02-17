# version 1.01
# uses pyserial
# install command: sudo apt install python3-serial
import serial

class SerialDevice :
    port =""
    baudrate = 9600
    timeout = 1
    encoding = "utf-8"
    # serial_dev

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600, timeout=3) :
        self.port = port
        self.baudrate = baudrate
        self.timeout=timeout
        try:
            self.serial_dev = serial.Serial(port=self.port,
                                        baudrate=self.baudrate,
                                        bytesize=serial.EIGHTBITS,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        timeout=self.timeout)
        except serial.SerialException as e:
            print("Serial exception!")

    def close(self):
        self.serial_dev.close()

    def send(self, str_data):
        command = str_data.encode(self.encoding)

        try:
            self.serial_dev.write(command)
        except serial.SerialException as e:
            print("Serial exception!")
        except serial.SerialTimeoutException as et:
            print("Serial timeout exception!")

    def get_response(self):
        response=""
        try:
            response=self.serial_dev.readline().decode(self.encoding).strip() #arduino finish string with \n
        except serial.SerialException as e:
            # tmp
            print("Serial exception!")
        return response