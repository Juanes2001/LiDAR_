import function as fn


if __name__ == '__main__':

    serial_ = fn.create_ser('COM3', 9600, timeout=1,write_timeout=1)
    fn.openSer(ser=serial_)
    while True :
        try:

            command = input("Ingrese comando: ")
            data = fn.process_command(serial_,command)



        except KeyboardInterrupt:


