import tkinter as tk
from netmiko import ConnectHandler

HEIGHT = 800
WIDTH = 1000

def get_cpu(entry):
        iosv_l2 = {
            'device_type': 'cisco_ios',
            'ip': entry,
            'username': 'admin',
            'password': 'admin'
        }
        net_connect = ConnectHandler(**iosv_l2)
        output = net_connect.send_command('sh processes cpu | exclude 0.00')

        label['text'] = output


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get CPU", font=40, command=lambda:get_cpu(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)



def get_int(entry):
        iosv_l2 = {
            'device_type': 'cisco_ios',
            'ip': entry,
            'username': 'admin',
            'password': 'admin'
        }
        net_connect = ConnectHandler(**iosv_l2)
        output = net_connect.send_command('show interfaces description')

        label['text'] = output

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.13, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Int", font=40, command=lambda:get_int(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()