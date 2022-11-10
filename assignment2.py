import tkinter as tk

class PaintTool(object):

    def __init__(self,bgcolour):
        self._root = tk.Tk()
        self._root.geometry('750x500')
        self._root.iconbitmap('favicon.ico') # I just wanted a favicon ¯\_(ツ)_/¯
        self._root.title('Paint Tool (⌐■_■)')

        self._coords = []

        self._L1 = tk.Label(self._root, text="Colour", font="Verdana 10 underline").place(x=20,y=20)
        self._L2 = tk.Label(self._root, text="Shape", font="Verdana 10 underline").place(x=20,y=250)

        self._redbtn = tk.Button(self._root, text="Red",command=self.red,bg="red", padx=20,pady=5).place(x=10,y=50)
        self._bluebtn = tk.Button(self._root, text="Blue",command=self.blue,bg="blue",fg="white", padx=19,pady=5).place(x=10,y=100)
        self._yellowbtn = tk.Button(self._root, text="Yellow",command=self.yellow,bg="yellow", padx=13,pady=5).place(x=10,y=150)

        self._linebtn = tk.Button(self._root, text="Line",bg="grey",command=self.line, padx=20,pady=5).place(x=10,y=280)
        self._rectbtn = tk.Button(self._root, text="Rectangle",bg="grey",command=self.rect,padx=5,pady=5).place(x=10,y=330)
        self._ovalbtn = tk.Button(self._root, text="Oval",bg="grey",command=self.oval, padx=20,pady=5).place(x=10,y=380)

        self._reset = tk.Button(self._root, text="Clear Canvas",bg="black",fg="red",command=self.reset,padx=20,pady=5).place(x=10,y=450)

        try:
            self._myCanvas = tk.Canvas(self._root, bg=bgcolour, height=500, width=500)
        except TypeError() or ValueError():
            print("Error for background colour. Setting default to white.")
            self._myCanvas = tk.Canvas(self._root, bg="white", height=500, width=500)
        
        self._myCanvas.bind("<Button-1>", self.mouse_function)
        self._myCanvas.pack()
        self._root.mainloop()
    
    def reset(self):
        self._myCanvas.delete("all")

    def red(self):
        self.colour="red"
    def blue(self):
        self.colour="blue"
    def yellow(self):
        self.colour="yellow"

    def line(self):
        self.shape="line"
    def rect(self):
        self.shape="rect"
    def oval(self):
        self.shape="oval"
    
    def mouse_function(self,event):
        global x,y
        self._x = event.x
        self._y = event.y
        self._coords.append(self._x)
        self._coords.append(self._y)
        if len(self._coords) == 4:
            try:
                if self.shape=="line":
                    self._myCanvas.create_line(self._coords[0],self._coords[1],self._coords[2],self._coords[3],fill=self.colour)
                elif self.shape=="rect":
                    self._myCanvas.create_rectangle(self._coords[0],self._coords[1],self._coords[2],self._coords[3],fill=self.colour)
                elif self.shape=="oval":
                    self._myCanvas.create_oval(self._coords[0],self._coords[1],self._coords[2],self._coords[3],fill=self.colour)
                self._coords.clear()
            except TypeError() or ValueError():
                raise Exception("Error!!! No shape and/or colour chosen.")
                pass
    

    

if __name__ == "__main__":
    white = "white"
    grey = "grey"
    purple = "purple"

    paint1 = PaintTool(white)
