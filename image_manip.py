# import Image # not working
from PIL import Image

old_im = Image.open('Incubation_time_to_Reolsution.png')
old_size = old_im.size

new_size = (800, 800)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
new_im.paste(old_im, box)

new_im.show()
# new_im.save('someimage.jpg')