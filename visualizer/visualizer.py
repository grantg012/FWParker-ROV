import atexit
import re
import socket
import sys
import tk
import tkinter
from tkinter import Image
import threading
from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7654  # Port to listen on (non-privileged ports are > 1023)

g_last_command = {c: 1500 for c in "abcd"}
LETTER_TO_X = dict(zip("abcdxy", range(1, 7)))

LETTER_PATTERN = re.compile(r"[A-z]")

g_socket = None

@atexit.register
def close_socket():
    global g_socket
    if g_socket is not None:
        g_socket.close()


def ui_process_data(plot: Axes, canvas: FigureCanvasTkAgg, data: bytes) -> None:
    """"""
    # Parse everything that's sent and our knowledge of the command
    global g_last_command
    while data:
        dataStr = data.decode()
        try:
            letterIndex = LETTER_PATTERN.search(dataStr).start()
            value, letter = int(dataStr[:letterIndex]), chr(data[letterIndex])
            g_last_command[letter] = value
            data = data[letterIndex + 1:]
        except Exception as e:
            print(e)
            data = data[1:]

    plot.cla() # Clear the plot
    series = {}
    for letter, command in g_last_command.items():
        x = LETTER_TO_X[letter]
        serie = plot.plot([x, x], [1499, command])[0]
        series[letter] = serie

    # Legend
    plot.legend(tuple(series.values()), tuple(series.keys()))

    plot.set_xlim([0, 7])
    plot.set_ylim([1380, 1620])

    canvas.draw()

def socketProcess(plot1, canvas: FigureCanvasTkAgg):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        global g_socket
        g_socket = s
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                ui_process_data(plot1, canvas, data)


def main(args: list) -> int:
    """"""

    # Thanks https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
    window = tkinter.Tk()
    window.title("ROV Visualization")
    window.geometry()
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    socketThread = threading.Thread(target=socketProcess, args = (plot1, canvas), daemon=True)
    socketThread.start()

    window.mainloop()



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))