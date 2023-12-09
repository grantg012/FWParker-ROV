import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7654  # Port to listen on (non-privileged ports are > 1023)


g_socket = None

def writeToSerial(msg: str) -> None:
    """msg will be something like '1600b'."""
    global g_socket
    if g_socket is None:
        # Open a client
        g_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        g_socket.connect((HOST, PORT))
    g_socket.sendall(msg.encode())

