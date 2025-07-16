import function as fn

data = []



if __name__ == '__main__':

    serial_ = fn.create_ser('COM9', 9600, timeout=1, write_timeout=1)
    fn.openSer(ser = serial_)
    try:
        while True:
            command = input("Ingrese comando: ")
            data.append(fn.process_command(serial_,command))
            print(data)

            array_only = [item for item in data if not isinstance(item, str)]

    except KeyboardInterrupt:
        # fn.close_ser(serial_)
        print("\nFin de la ejecución\n")


