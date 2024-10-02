import software_install_object
import tkinter as tk

software_install_object.ObjectLoader.load()

print(software_install_object._list[0])

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.geometry("1920x1080")

scr_width = 1920 #14 is size of scrollbar
scr_height = 1080


canvas = tk.Canvas(root, width=scr_width-400, height=scr_height, bg="lightgrey", scrollregion=(0, 0, scr_width, scr_height+10000))

canvas.place(relx=1, rely=0, anchor="ne")

y_scroll = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
y_scroll.pack(side=tk.RIGHT, fill='y')

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def design_button():
    idx=0
    for _ in software_install_object._list:
        print(_.name)
        round_rectangle(50, 50+(idx*200), 1470, 200+(idx*200), radius=45, fill="grey")
        canvas.create_text(85, 65+(idx*200), text=_.name, anchor="nw", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(85, 125+(idx*200), text="Version: " + _.version, anchor="nw", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(scr_width-485, 125+(idx*200), text=_.install_type, anchor="ne", fill="black", font=('Helvetica 15 bold'))
        idx+=1

design_button()




canvas1 = tk.Canvas(root, width=400, height=scr_height, bg="darkgrey")
canvas1.place(anchor="nw")

canvas1.create_rectangle(0, 0, 400, 100, fill="blue")
canvas1.create_rectangle(0, 100, 400, 200, fill="green")
canvas1.create_rectangle(0, 200, 400, 300, fill="red")
canvas1.create_rectangle(0, 300, 400, 400, fill="yellow")


print(root.winfo_screenwidth())
canvas.config(yscrollcommand=y_scroll.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
#canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---
#frame = tk.Frame(canvas)
#canvas.create_window((800,9), window=frame)

# --- add widgets in frame ---

#for _ in range(len(software_install_object._list)):
#    l = tk.Label(frame, text=software_install_object._list[_], font="-size 16")
#    l.pack()

# --- start program ---

root.mainloop()
