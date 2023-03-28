#!/usr/bin/env python
# coding: utf-8

# Thư viện dùng

# In[6]:


from PIL import Image, ImageDraw, ImageFilter
import string
import random
import math
import os
import pandas as pd
import imageio.v2 as imageio
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Biến toàn cục

# In[7]:


def genLogo(background : Image, logo : Image , traindir : string, x : int, y : int, name_file : int) :
    '''
    Gen ảnh:
    ---------
    Param:
    - background, logo: ảnh để Ren
    - traindir: folder để save ảnh Ren
    - x, y: tọa độ đặt ảnh logo ngẫu nhiên trên background
    - name_file: tên ảnh (đánh số từ 0 đến n)
    '''
    gen_logo = background.copy()
    gen_logo.paste(logo, (x,y))
    gen_logo.save(traindir + "/" + str(name_file) +  ".jpg", quality = 95) #Lưu vào ảnh có path: 'traindir/{name_file}.jpg'


# In[8]:


def new_label(x : int, y: int, logo_height : int, logo_width : int, newlabel: string, name_file : string, brand : string):
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
    picture_name = brand + "_" + str(name_file) + ".jpg"
    picture_brand = brand
    x_min = x
    y_min = y
    x_max = logo_height + x
    y_max = logo_width + y
    
    with open(newlabel,'a') as file_w:   
        l = picture_name + " " + picture_brand  + " " + str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) + "\n"
        '''
        Ex: 0.png    Highland    x_min   y_min   x_max   y_max 
        '''
        file_w.write(l)           
        file_w.close()


# In[9]:


def create_train_example(background : Image, logo : Image , traindir : string, newlabel : string, brand : string, name_file : int):
    """
    Chèn logo vào ảnh
    Params
    ----------------
    - traindir: đường dẫn đến folder để tạo ảnh 
    - background: ảnh background
    - logo: ảnh logo cần chèn
    - newlable: đường dẫn đến folder để tạo label
    - name_file: ten ảnh
    - brand: tên brand
    """
    
    bg_height,bg_width = background.size
    logo_height,logo_width = logo.size
    #Only paste when Logo smaller than background
    if (logo_height < bg_height) and (logo_width < bg_width):
        y = random.randint(0, bg_width - logo_width)
        x = random.randint(0, bg_height - logo_height)
        
        genLogo(background, logo, traindir, x, y, name_file)
        new_label(x, y, logo_height, logo_width, newlabel, name_file, brand)
    else:
        print("Logo bigger than background")


# In[10]:


def readBackGround(DIRECTORY : string): #, CATEGORIES : list):
    
    list_path_background = []
    #for category in CATEGORIES: #Xét từng folder
    path = os.path.join(DIRECTORY, category) #Get path from folder
    for img in os.listdir(path): #Get each of img from folder
        path_background = os.path.join(path, img) #Get img path
        list_path_background.append(path_background)
    return list_path_background


# In[11]:


def main():
    DIRECTORY = r'<background_path_file>' #Get the path
    #CATEGORIES = ['cats','dogs'] #Name the folder 
    list_path_background = readBackGround(DIRECTORY ) #, CATEGORIES)
    path_logo = r'<logo_path>'
    brand = "HighLand"
    traindir = '<where you want to save GenLogo>'
    newlabel = "<Label.txt>"
    name_file = 0
    
    for path_background in list_path_background:
        background = Image.open(path_background, 'r')
        logo = Image.open(path_logo, 'r')
        create_train_example(background, logo, traindir, newlabel, brand, name_file)
        name_file += 1


# In[12]:


main()


# In[ ]:





# In[13]:


logo.size


# In[14]:


background.size


# In[ ]:




