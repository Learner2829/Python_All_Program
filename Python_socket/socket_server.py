import socket
import sys


host = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# def create_socket():
#     global host
#     global port
#     global s


def bind_socket():
    global host
    global port
    global s

    print("Binding the port " + str(port))
    try:
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error" + str(msg) + "\n" + "Retring")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established " + "IP" + address[0] + " : port" + str(address[1]))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    # create_socket()
    bind_socket()
    socket_accept()


main()
