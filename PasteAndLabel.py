#!/usr/bin/env python
# coding: utf-8

# In[86]:


from PIL import Image, ImageDraw, ImageFilter
import string
import random
import math
import os
import pandas as pd
import imageio.v2 as imageio
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[87]:


path_background = "D:/Cuong/download/pasteImg/rocket.jpg"
path_logo = "D:/Cuong/download/pasteImg/lena.jpg"
background = Image.open(path_background, 'r')
logo = Image.open(path_logo, 'r')
labeldir = 'label.txt'
newlabeldir = 'newlabel.txt'


# In[88]:


def create_train_example(background : Image, logo : Image , labeldir : string, newlabeldir : string, path_logo : string):
    """
    Chèn logo vào ảnh
    Param
    ----------------
    - traindir: đường dẫn đến folder để tạo ảnh 
    - background: ảnh background
    - logo: ảnh logo cần chèn
    - labeldir: đường dẫn đến folder để tạo label
    Return
    ----------------
    - Tọa độ của logo
    """
    temp_background = background.copy()
    
    bg_height,bg_width = temp_background.size
    logo_height,logo_width = logo.size
    
    print(str(bg_height) + " " + str(bg_width) + " " + str(logo_height) + " " + str(logo_width))
    
    #Only paste when Logo smaller than background
    if (logo_height < bg_height) and (logo_width < bg_width):
        x = random.randint(0, logo_width)
        y = random.randint(0, logo_height)
        temp_background.paste(logo, (x,y))
        temp_background.save("geeks.jpg", quality=95)
    else:
        return "Errol"
    #Paste logo above background 
    
    '''
    Save new picture LogoReg:
    ----------------
    Param:
    - name_new_picture : ten anh moi
    '''
    name_file = os.path.basename(path_logo)
    name_new_picture =  str(name_file)
    temp_background.save(name_new_picture)
    new_label(x, y, labeldir, newlabeldir, name_file)
    
    


# In[89]:


def new_label(x : int, y: int, labeldir : string,  newlabeldir: string, name_file : string):
    '''
    Gan label + ghi vao tep txt
    -------------------------
    Input:
    - original_label: path file txt where you store label
    - labeldir: path file txt where you want to store label for LogoRen (should create a txt file to store)
    - x, y: distant of place where logo paste to background
    - name_file: name Logo paste above background
    Output:
    - write (name_picture, brand_picture, label_number, x_min, y_min, x_max, y_max) to laberdir 
    '''
    name_picture = ""
    brand_picture = ""
    label_number = 0
    x_min = 0
    y_min = 0
    x_max = 0
    y_max = 0
    #Read original babel txt to extract 
    with open(labeldir, 'r') as f:
        lines = f.readlines()
    
        for line in lines:
            #Doc du lieu tu original_label trung ten anh Logo
            if line.split(' ')[0] == name_file: 
                name_picture = line.split(' ')[0]
                brand_picture = line.split(' ')[1]
                label_number = line.split(' ')[2]
                x_min = int(line.split(' ')[3])
                y_min = int(line.split(' ')[4])
                x_max = int(line.split(' ')[5])
                y_max = int(line.split(' ')[6])
                
                x_min += x
                y_min += y
                x_max += x
                y_max += y
                
        f.close()
    #Thay doi toa do cua Logo sau khi paste
    with open(newlabeldir,'w') as file_w:   
        l = name_picture + " " + brand_picture + " " + str(label_number) + " " + str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) + "\n"
        '''
        Ex: Highland.png    Highland    label_number    x_min   y_min   x_max   y_max 
        '''
        file_w.writelines([l])           
        file_w.close()
    #Write to labeldir 
     


# In[90]:


create_train_example(background, logo, labeldir, newlabeldir, path_logo)


# In[68]:


logo.size


# In[ ]:




