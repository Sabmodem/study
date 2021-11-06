from PIL import Image

# img = Image.new('RGB',(300,300))
# for i in range(300):
#     for k in range(300):
#         img.putpixel((i,k),(i,255-i,255-k))

# img.save('1.jpeg')

img = Image.new('RGB',(300,300))
for i in range(300):
    for k in range(300):
        img.putpixel((i,k),(k,255-i,255-i))

img.save('2.jpeg')

img = Image.new('RGB',(300,300))
for i in range(300):
    for k in range(300):
        img.putpixel((i,k),(k,k-i,k-i))

img.save('3.jpeg')

img = Image.new('RGB',(300,300))
for i in range(300):
    for k in range(300):
        img.putpixel((i,k),((i+k)%255,255,255-k))

img.save('4.jpeg')

img = Image.new('RGB',(300,300))
for i in range(300):
    for k in range(300):
        img.putpixel((i,k),(i,255-i,(i+k)%255))

img.save('5.jpeg')

img = Image.new('RGB',(300,300))
for i in range(300):
    for k in range(300):
        img.putpixel((i,k),((k-i)%255,k,(i+k)%255))

img.save('8.jpeg')
