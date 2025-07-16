import serial
import time
import numpy as np
import matplotlib as plt

terminador = "\x0A"

# Con esta función podemos mandar una petición de identificación para
# corroborar comunicación

def IDNt(ser):
    global terminador
    write_Serial(ser, "*IDN?" + terminador)
    time.sleep(0.5)
    data = read_one_Serial(ser)
    return data


def process_command(ser,command):

    command_splitted = command.split(" ")

    match command_splitted[0]:
        case "Identificar":
            data = IDNt(ser=ser)
            return data
        case "Obtener":
            data = []
            for i in command_splitted[1:]:
                if i == "x":
                    data.append(float(OUTp_i(ser=ser, i=1)))
                elif i == "y":
                    data.append(float(OUTp_i(ser=ser, i=2)))
                elif i == "r":
                    data.append(float(OUTp_i(ser=ser, i=3)))
                elif i == "arc":
                    data.append(float(OUTp_i(ser=ser, i=4)))
            return data


def write_Serial(ser, data):
    ser.write(data.encode('utf-8'))
    time.sleep(1)

def read_one_Serial(ser):
    line = ""
    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting
            line += ser.read(ser.in_waiting).decode('utf-8').strip()  # Read and decode
        else:
            break
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


def OUTp_i(ser,i):
    global terminador
    write_Serial(ser, f"OUTP? {i}" + terminador)
    time.sleep(0.5)
    data = read_one_Serial(ser)
    return data

def close_ser(ser):
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











