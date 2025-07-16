import function as fn
import numpy as np

data = []



if __name__ == '__main__':


    arr = np.array([[1,2], [3,4]])
    print(arr[:][0])


    # serial_ = fn.create_ser('COM9', 9600, timeout=1, write_timeout=1)
    # fn.openSer(ser = serial_)
    # try:
    #     while True:
    #         command = input("Ingrese comando: ")
    #         result = fn.process_command(serial_,command)
    #         if result is not None:
    #             data.append(result)
    #         print(data)
    #
    #
    # except KeyboardInterrupt:
    #     # fn.close_ser(serial_)
    #     print("\nFin de la ejecución\n")


