# version 1.06
# by Igor Pitler
# uses pyserial
# install command: sudo apt install python3-serial
import serial

class SerialDevice :
    port =""
    baudrate = 9600
    timeout = 1
    encoding = "utf-8"
    # serial_dev

    # 0 no error, 1 timeout, 2 common serial error
    err_code = 0

    def get_error(self):
        return self.err_code

    def set_error(self, code):
        self.err_code = code

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
        except serial.SerialTimeoutException as te:
            self.set_error(1)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2)
            print("Serial exception!")

    def close(self):
        self.serial_dev.close()

    def send(self, str_data):
        command = str_data.encode(self.encoding)
        self.set_error(0)
        try:
            self.serial_dev.write(command)
        except serial.SerialTimeoutException as et:
            self.set_error(1)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2)
            print("Serial exception!")

    def get_response(self):
        response=""
        self.set_error(0)
        try:
            response=self.serial_dev.readline().decode(self.encoding).strip() #arduino finish string with \n
        except serial.SerialTimeoutException as te:
            self.set_error(1)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2)
            print("Serial exception!")
        return response