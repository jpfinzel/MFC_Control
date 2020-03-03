from tkinter import *
import serial
import struct

class MFC_set:
    def __init__(self, master):
        self.master = master
        master.title("MFC Set Points")
        self.zero = 0.00
        self.set_ser = serial.Serial('COM5')
        self.set_ser.baudrate = 9600
        self.read_ser = serial.Serial('COM4')
        self.read_ser.baudrate = 9600
        self.TimeInterval = 500

        self.entries = [DoubleVar(), DoubleVar(), DoubleVar(), DoubleVar()]
        self.readouts = [StringVar(), StringVar(), StringVar(), StringVar()]
        self.labels = ['Channel 1: CO or H2', 'Channel 2: CH4 or C2H2', 'Channel 3: O2', 'Channel 4: He']
        self.characters = ['A', 'B', 'C', 'D', 'E', 'F']

        for i in range(len(self.entries)):
            self.entries[i].set(self.zero)
            self.readouts[i].set(self.zero)

        self.label_1 = Label(master, text=self.labels[0])
        self.label_2 = Label(master, text=self.labels[1])
        self.label_3 = Label(master, text=self.labels[2])
        self.label_4 = Label(master, text=self.labels[3])

        self.flow_1 = Message(master, textvariable=self.readouts[0])
        self.flow_2 = Message(master, textvariable=self.readouts[1])
        self.flow_3 = Message(master, textvariable=self.readouts[2])
        self.flow_4 = Message(master, textvariable=self.readouts[3])

        vcmd = master.register(self.validate)
        self.entry_1 = Entry(master, textvariable=self.entries[0], validate="key", validatecommand=(vcmd, '%P'))
        self.entry_2 = Entry(master, textvariable=self.entries[1], validate="key", validatecommand=(vcmd, '%P'))
        self.entry_3 = Entry(master, textvariable=self.entries[2], validate="key", validatecommand=(vcmd, '%P'))
        self.entry_4 = Entry(master, textvariable=self.entries[3], validate="key", validatecommand=(vcmd, '%P'))

        #
        self.send_button = Button(master, text="Send Setpoints", command=self.send_setpoints)
        self.reset_button = Button(master, text="Clear Setpoints", command=self.reset)

        self.label_1.grid(row=0, column=0, columnspan=3, sticky=W+E)
        self.entry_1.grid(row=1, column=0, columnspan=3, sticky=W+E, padx=10, pady=5, ipadx=5, ipady=5)
        self.flow_1.grid(row=2, column=0, columnspan=3, sticky=W + E)

        self.label_2.grid(row=0, column=4, columnspan=3, sticky=W + E)
        self.entry_2.grid(row=1, column=4, columnspan=3, sticky=W + E, padx=10, pady=5, ipadx=5, ipady=5)
        self.flow_2.grid(row=2, column=4, columnspan=3, sticky=W + E)

        self.label_3.grid(row=6, column=0, columnspan=3, sticky=W + E)
        self.entry_3.grid(row=7, column=0, columnspan=3, sticky=W + E, padx=10, pady=5, ipadx=5, ipady=5)
        self.flow_3.grid(row=8, column=0, columnspan=3, sticky=W + E)

        self.label_4.grid(row=6, column=4, columnspan=3, sticky=W + E)
        self.entry_4.grid(row=7, column=4, columnspan=3, sticky=W + E, padx=10, pady=10, ipadx=5, ipady=5)
        self.flow_4.grid(row=8, column=4, columnspan=3, sticky=W + E)

        self.send_button.grid(row=10, column=1, columnspan=3, sticky=W + E, padx=10, pady=10, ipadx=5, ipady=5)
        self.reset_button.grid(row=10, column=3, columnspan=3, sticky=W + E, padx=10, pady=10, ipadx=5, ipady=5)

        self.read_ser.reset_input_buffer()
        # self.set_ser.reset_input_buffer()
        self.get_flows()

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            # self.channel_1 = None
            return True

        try:
            set_point = float(new_text)
            if 0 <= set_point <= 50:
                # self.channel_1 = set_point
                return True
            else:
                return False
        except ValueError:
            return False

    def send_setpoints(self):
        for i in range(len(self.entries)):
            signal = int(round((float(self.entries[i].get()) / 50.0) * 255))
            send_signal = b''
            send_signal += struct.pack('!B', signal)
            letter_code = self.characters[i].encode('utf-8')
            self.set_ser.write(letter_code)
            self.set_ser.write(send_signal)

    def reset(self):
        for i in range(len(self.entries)):
            self.entries[i].set(self.zero)
        self.send_setpoints()

    def get_flows(self):
        incoming = self.read_ser.readline().decode('utf-8')
        data_array = incoming.split(",")
        processed = [x.replace("\r\n", "") for x in data_array]

        for i in range(len(self.entries)):
            self.readouts[i].set(processed[i])

        self.master.after(self.TimeInterval, self.get_flows)


root = Tk()
my_gui = MFC_set(root)
root.mainloop()