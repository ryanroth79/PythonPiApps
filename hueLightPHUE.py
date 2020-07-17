from phue import Bridge
import tkinter

class Light:
  def __init__(self, name, light, brightness):
    self.name = name
    self.l = light
    self.bs = brightness

  def myfunc(self):
    print("Hello my name is " + self.name)

  def toggle(self):
    print("Toggling " + self.l.name)
    print(int(self.bs.get()))
    if(self.l.on):
      self.l.on = False
    else:
      self.l.on = True

  def setBrightness(self):
    self.l.brightness = int(self.bs.get())
      

window = tkinter.Tk()
window.geometry("800x480")
window.wm_title("Let It GLOW")


bVar = tkinter.DoubleVar()
brightnessSlider = tkinter.Scale(window, from_=0, to_=255, variable = bVar, orient=tkinter.HORIZONTAL, resolution = 1, width=45, length=200).grid(row=0, column=0, columnspan=2)


b = Bridge('192.168.1.177')

l = b.lights
Lights = ['']


for r, li in enumerate(l):
    lo = Light(li.name, li, bVar)
    button = tkinter.Button(text = li.name, command = lo.toggle).grid(row = r+1, column=0)
    bbutton = tkinter.Button(text = li.name + "B", command = lo.setBrightness).grid(row = r+1, column=1)
    Lights.append(lo)
    print(li.name)

window.mainloop()
