import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)
        
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying")
        bind_socket()

# Establish connection with a client
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established. IP: " + address[0] + " Port: " + str(address[1]))
    send_command(conn)
    conn.close()

# Send the command
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
    create_socket()
    bind_socket()
    socket_accept()

main()