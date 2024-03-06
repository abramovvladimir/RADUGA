from tkinter import*

bot = Tk()

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Жёлтый',
    '#00ff00': 'Зелёный',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}

class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(bot, bg = hex_color, command = self.get_color)
        self.b.pack(fill = X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

l = Label(bot)
e = Entry(bot, width = 25, justify = 'center')
l.pack()
e.pack()

for g, o in colors.items():
    MyButtons(bot, o, g)

bot.mainloop()
