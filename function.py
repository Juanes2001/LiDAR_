import serial
import time

terminador = '10'


def main():
    try:
        ser = create_ser('COM3', 9600, timeout=1, write_timeout=1)

        while True:
            try:
                # Prepare data to send
                data = "Hello Device\n"
                # Encode and write
                ser.write(data.encode('utf-8'))

                # Optional: Wait for acknowledgment (if protocol requires it)
                # ack = ser.readline().decode().strip()
                # print("ACK:", ack)

                time.sleep(1)  # Adjust based on how frequently you send data

            except serial.SerialTimeoutException:
                print("Write timeout occurred. Retrying...")

            except serial.SerialException as e:
                print(f"Serial error: {e}")
                break

    except Exception as e:
        print(f"Failed to open serial port: {e}")


# Con esta función podemos mandar una petición de identificación para
# corroborar comunicación

def write_Serial(ser, data):
    ser.write(data.encode('utf-8'))
    time.sleep(1)


def IDNt(ser):
    global terminador

    write_Serial(ser, "*IDN?" + terminador)


def closeSer(ser):
    if ser and ser.is_open:
        ser.close()
        print("Serial port closed.")


def openSer(ser):
    if not ser.is_open:
        ser.open()
        print("Serial port opened.")


def create_ser(port, baud, timeout, write_timeout):
    # Open serial connection0

    seri = serial.Serial(
        port=port,  # Update with your correct port (e.g., '/dev/ttyUSB0' for Linux)
        baudrate=baud,
        timeout=timeout,  # Read timeout
        write_timeout=write_timeout  # Write timeout (important for robustness)
    )
    return seri











