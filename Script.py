import function as fn
import numpy as np

data = []



if __name__ == '__main__':


    # arr = np.array([[1,2], [3,4]])
    # print(arr[:][0])


    serial_1 = fn.create_ser('COM9', 9600, timeout=1, write_timeout=1)
    serial_2 = fn.create_ser('COM12', 9600, timeout=1, write_timeout=1)

    ser_Array = [serial_1,serial_2]

    fn.openSer(ser = ser_Array)

    try:
        while True:
            command = input("Ingrese comando: ")

            result= fn.process_command(ser_Array,command)
            if result is not None:
                data.append(result)
            print(data)


    except KeyboardInterrupt:
        fn.close_ser(serial_1)
        fn.close_ser(serial_2)
        print("\nFin de la ejecución\n")


