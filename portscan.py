import socket
import sys

def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print('[+] Host -> {} - Porta:{} -> ABERTA!'.format(host, port))

    except Exception as error:
        print(error)

if __name__ == "__main__" :

        if len(sys.argv) >= 2:
            host = sys.argv[1]

            if len(sys.argv) >= 3:
                ports = sys.argv[2].split(',')

            else:
                ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 139, 444, 445, 3306, 3389, 8080, 8443]

            scan(host, ports)