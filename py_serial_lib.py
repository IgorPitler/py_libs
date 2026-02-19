# version 1.1
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
    err_description = ""

    def get_error_code(self):
        return self.err_code

    def get_error_description(self):
        return self.err_description

    def set_error(self, code, description = ""):
        self.err_code = code
        self.err_description = description

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
            self.set_error(1, te.strerror)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2, e.strerror)
            print("Serial exception!")

    def close(self):
        try:
            self.serial_dev.close()
        except AttributeError as ae:
            self.set_error(3, ae.name)
            print("Attribute error exception!")

    def send(self, str_data):
        command = str_data.encode(self.encoding)
        self.set_error(0)
        try:
            self.serial_dev.write(command)
        except serial.SerialTimeoutException as te:
            self.set_error(1, te.strerror)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2, e.strerror)
            print("Serial exception!")
        except AttributeError as ae:
            self.set_error(3, ae.name)
            print("Attribute error exception!")

    def get_response(self):
        response=""
        self.set_error(0)
        try:
            response=self.serial_dev.readline().decode(self.encoding).strip() #arduino finish string with \n
        except serial.SerialTimeoutException as te:
            self.set_error(1, te.strerror)
            print("Serial timeout exception!")
        except serial.SerialException as e:
            self.set_error(2, e.strerror)
            print("Serial exception!")
        except AttributeError as ae:
            self.set_error(3, ae.name)
            print("Attribute error exception!")
        return response