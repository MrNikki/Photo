from PIL import Image, ImageFilter

class ImageEgitor():
    def __init__(self, name):
        self.name = name
        self.file = ""
        self.change_list = list()
    def info(self):
        print(f"Розмір: {self.file.size}")
        print(f"Колір: {self.file.mode}")
        print(f"Формат: {self.file.format}")

    def do_left(self):
        left = self.file.transpose(Image.ROTATE_90)
        self.change_list.append(left)

    def do_cropped(self):
        box = (250, 100, 600, 400)
        new = self.file.crop(box)
        self.change_list.append(new)

    def open(self):
        try:
            self.file = Image.open(self.name)
        except:
            print("Немає такого файлу, кабачку")
        
    def flipped(self):
        mirror = self.file.transpose(Image.FLIP_LEFT_RIGHT)
        self.change_list.append(mirror)
image = ImageEgitor("koala.jpeg")
image.open()
image.file.show()
image.do_cropped()
image.do_left()
image.flipped()

for p in image.change_list:
    p.show()

        