import tkinter
root = tkinter.Tk()
root.title("マンデルブロー 複素数／カラー")
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()

def _color(n):
    c = (int(255*n/loops)<<8) + int(192*(loops-n)/loops)
    return "#{:06x}".format(c)

loops = 100
xs = -2.5
xe = 1.5
ys = -1.5

#xs = 0.32
#xe = 0.38
#ys = 0.48

steps = (xe-xs)/800

for x in range(800): # 実部
    cvs.update()
    a = xs+steps*x
    for y in range(600): # 虚部
        b = ys+steps*y
        c = a + b*1j
        z = 0
        for n in range(loops):
            z = z*z + c
            if abs(z) > 2:
                cvs.create_rectangle(x, y, x, y, fill=_color(n), width=0)
                break

root.mainloop()
