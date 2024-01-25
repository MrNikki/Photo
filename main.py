from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("original.jpg") as file:
    print(f"Розмір: {file.size}")
    print(f"Колір: {file.mode}")
    print(f"Формат: {file.format}")
    
    file = ImageEnhance.Contrast(file)
    file = file.enhance (1.5)
    file.save("contr.jpg")
    file.show()


    file = file.transpose(Image.FLIP_LEFT_RIGHT)
    file.save("mirrow.jpg")
    
    
    file = file.convert("L")
    file.save("original1.jpg")

    file = file.filter(ImageFilter.BLUR)
    file.save("blured.jpg")

    file = file.transpose(Image.ROTATE_180)
    file.save("up.jpg")

    

    