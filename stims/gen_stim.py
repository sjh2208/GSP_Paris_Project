#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
import numpy as np

coords = [(40, 30), (125, 30), (210, 30), (295, 30),
          (40, 115), (125, 115), (210, 115), (295, 115),
          (40, 200), (125, 200), (210, 200), (295, 200)]

boxes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def make_transparent(img):
    new_image = []
    for item in img.getdata():
        if item[:3] == (255, 255, 255):
            new_image.append((255, 255, 255, 0))
        else:
            new_image.append(item)
    img.putdata(new_image)
    return img

def box_resize(img):
    size = (421, 312)
    new = img.resize((int(size[0]/4) - 20, int(size[1]/3) - 20))
    return new

def fix_elem(img):
    step1 = make_transparent(img)
    step2 = box_resize(step1)
    return step2

#set up template files for combination later
grid = Image.open('./templates/grid.jpeg').convert('RGBA')
a = Image.open('./templates/a.jpeg').convert('RGBA')
a = fix_elem(a)
b = Image.open('./templates/b.jpeg').convert('RGBA')
b = fix_elem(b)
c = Image.open('./templates/c.jpeg').convert('RGBA')
c = fix_elem(c)
d = Image.open('./templates/d.jpeg').convert('RGBA')
d = fix_elem(d)
e = Image.open('./templates/e.jpeg').convert('RGBA')
e = fix_elem(e)
f = Image.open('./templates/f.jpeg').convert('RGBA')
f = fix_elem(f)
g = Image.open('./templates/g.jpeg').convert('RGBA')
g = fix_elem(g)
h = Image.open('./templates/h.jpeg').convert('RGBA')
h = fix_elem(h)
one = Image.open('./templates/1.jpeg').convert('RGBA')
one = fix_elem(one)
two = Image.open('./templates/2.jpeg').convert('RGBA')
two = fix_elem(two)
three = Image.open('./templates/3.jpeg').convert('RGBA')
three = fix_elem(three)
four = Image.open('./templates/4.jpeg').convert('RGBA')
four = fix_elem(four)
five = Image.open('./templates/five.jpeg').convert('RGBA')
five = fix_elem(d)
six = Image.open('./templates/six.jpeg').convert('RGBA')
six = fix_elem(six)
seven = Image.open('./templates/seven.jpeg').convert('RGBA')
seven = fix_elem(seven)
eight = Image.open('./templates/eight.jpeg').convert('RGBA')
eight = fix_elem(eight)

#create new stims
path_name = './outputs/stim_{f}_{n}.png'
max = 100

#which-figure loop
for i in range(2):
    
    #how-many-grids-of-each loop
    for j in range(0, max):
        
        new_grid = grid.copy()
        new_boxes = boxes.copy()
        
            
        if i == 0: #figure=letter
            
            #fill-in-boxes loops
            for s1 in range(8):
                box = new_boxes[np.random.randint(0, len(new_boxes))]
                new_boxes.remove(box)
                letter = np.random.randint(0, 8)
                if letter == 0:
                    new_grid.paste(a, coords[box], a)
                elif letter == 1:
                    new_grid.paste(b, coords[box], b)
                elif letter == 2:
                    new_grid.paste(c, coords[box], c)
                elif letter == 3:
                    new_grid.paste(d, coords[box], d)
                elif letter == 4:
                    new_grid.paste(e, coords[box], e)
                elif letter == 5:
                    new_grid.paste(f, coords[box], f)
                elif letter == 6:
                    new_grid.paste(g, coords[box], g)
                elif letter == 7:
                    new_grid.paste(h, coords[box], h)
            for s2 in range(4):
                box = new_boxes[np.random.randint(0, len(new_boxes))]
                new_boxes.remove(box)
                fig = np.random.randint(0, 8)
                if fig == 0:
                    new_grid.paste(one, coords[box], one)
                elif fig == 1:
                    new_grid.paste(two, coords[box], two)
                elif fig == 2:
                    new_grid.paste(three, coords[box], three)
                elif fig == 3:
                    new_grid.paste(four, coords[box], four)
                elif fig == 4:
                    new_grid.paste(five, coords[box], five)
                elif fig == 5:
                    new_grid.paste(six, coords[box], six)
                elif fig == 6:
                    new_grid.paste(seven, coords[box], seven)
                elif fig == 7:
                    new_grid.paste(eight, coords[box], eight)
            
        elif i == 1: #figure=number
            
            #fill-in-boxes loops
            for s1 in range(8):
                box = new_boxes[np.random.randint(0, len(new_boxes))]
                new_boxes.remove(box)
                number = np.random.randint(0, 8)
                if number == 0:
                    new_grid.paste(one, coords[box], one)
                elif number == 1:
                    new_grid.paste(two, coords[box], two)
                elif number == 2:
                    new_grid.paste(three, coords[box], three)
                elif number == 3:
                    new_grid.paste(four, coords[box], four)
                elif number == 4:
                    new_grid.paste(five, coords[box], five)
                elif number == 5:
                    new_grid.paste(six, coords[box], six)
                elif number == 6:
                    new_grid.paste(seven, coords[box], seven)
                elif number == 7:
                    new_grid.paste(eight, coords[box], eight)
            for s2 in range(4):
                box = new_boxes[np.random.randint(0, len(new_boxes))]
                new_boxes.remove(box)
                fig = np.random.randint(0, 8)
                if fig == 0:
                    new_grid.paste(a, coords[box], a)
                elif fig == 1:
                    new_grid.paste(b, coords[box], b)
                elif fig == 2:
                    new_grid.paste(c, coords[box], c)
                elif fig == 3:
                    new_grid.paste(d, coords[box], d)
                elif fig == 4:
                    new_grid.paste(e, coords[box], e)
                elif fig == 5:
                    new_grid.paste(f, coords[box], f)
                elif fig == 6:
                    new_grid.paste(g, coords[box], g)
                elif fig == 7:
                    new_grid.paste(h, coords[box], h)

        #crop and save the final stim
        new_grid = new_grid.crop((41, 29, 382, 285))
        new_grid.save(path_name.format(f=i, n=j), 'PNG')
        
print('Done generating stimuli!')

