import serial
import time

terminador = '10'


# Con esta función podemos mandar una petición de identificación para
# corroborar comunicación

def IDNt(ser):
    global terminador

    write_Serial(ser, "*IDN?" + terminador)


def write_Serial(ser, data):
    ser.write(data.encode('utf-8'))
    time.sleep(1)

def read_one_Serial(ser):
    if ser.in_waiting > 0:  # Check if there is data waiting
        line = ser.readline().decode('utf-8').strip()  # Read and decode
        return line

def read_Serial(ser):
    data_array = []
    try:
        print("Starting to read data...")
        while True:
            if ser.in_waiting > 0:  # Check if there is data waiting
                line = ser.readline().decode('utf-8').strip()  # Read and decode
                try:
                    number = float(line)  # Convert to number (int/float)
                    data_array.append(number)
                    print(f"Received: {number}")
                except ValueError:
                    print(f"Ignored non-numeric data: {line}")
            time.sleep(0.01)  # Prevent CPU overload

    except KeyboardInterrupt:
        print("\nStopped by user.")


def IDNt(ser):
    global terminador
    write_Serial(ser, "*IDN?" + terminador)


def OUTp_i(ser,i):
    global terminador
    write_Serial(ser, f"OUTP? {i}" + terminador)


def closeSer(ser):
    if ser and ser.is_open:
        ser.close()
        print("Serial port closed.")


def openSer(ser):
    if not ser.is_open:
        ser.open()
        print("Serial port opened.")
    else:
        print("Serial port has already been opened.")

def create_ser(port, baud, timeout, write_timeout):
    # Open serial connection0

    seri = serial.Serial(
        port=port,  # Update with your correct port (e.g., '/dev/ttyUSB0' for Linux)
        baudrate=baud,
        timeout=timeout,  # Read timeout
        write_timeout=write_timeout  # Write timeout (important for robustness)
    )
    return seri











