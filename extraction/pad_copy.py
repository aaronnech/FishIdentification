import Image

old_im = Image.open('someimage.jpg')
old_size = old_im.size

new_size = (800, 800)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

new_im.show()
# new_im.save('someimage.jpg')