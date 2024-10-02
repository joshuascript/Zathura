#https://stackoverflow.com/questions/75883715/tkinter-how-can-i-detect-when-the-main-window-is-resizing
import tkinter as tk

class MainWindow:
    def __init__(self):

        self.parent=tk.Tk()
        self.parent.title("TEST")
        self.parent.minsize(350, 300)

        self.label=tk.Label(self.parent, text="Ready")
        self.label.pack()

        self.parent.bind("<Configure>", self.resizing)

        self.parent.mainloop()

    def resizing(self, event):
        if event.widget == self.parent:
            if getattr(self, "_after_id", None):
                self.parent.after_cancel(self._after_id)
            self.label.configure(text="window resizing...")
            self._after_id = self.parent.after(
                100, lambda: self.label.configure(text="ready")
            )

app=MainWindow()
