from PIL import Image, ImageDraw, ImageFilter
import string
import random
import math
import os
import pandas as pd

background = Image.open("C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/background/6921201_9c482d378a_c.jpg")
logo = Image.open("C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/logo/highlandcoffee.jpg")
labeldir = "<Where you store new label file txt>" 
train_file = "C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/train_generated"
original_label = "<Where you store old label file txt>"

def get_size(background: Image, logo: Image):
    """
    Lấy chiều cao và chiều rộng ảnh 
    Param
    ----------------
    background
    logo

    Return
    ----------------
    - Chiều cao và chiều rộng lần lượt của background và logo nếu ảnh background lớn hơn ảnh logo
    """
    if background.size <= logo.size:
        return 0,0,0,0
    background_height,background_width = background.size
    logo_height,logo_width = logo.size
    return background_height,background_width,logo_height,logo_width 

def draw_box(img,x_min,y_min,x_max,y_max):
    draw = ImageDraw.Draw(img)
    # Draw the bounding box on the image
    draw.rectangle(((x_min, y_max), (x_max, y_min)), outline="green", width=2)
    # Display image with bounding boxes and class labels
    img.show()

def create_train_example(traindir:string ,background:Image,logo:Image , labeldir: string):
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
    bg_height,bg_width,logo_height,logo_width = get_size(background,logo)
    
    #Only paste when Logo smaller than background
    if (logo_height < bg_height) and (logo_width < bg_width):
        x = random.randint(0, logo_width)
        y = random.randint(0, logo_height)
        background.paste(logo,(y,x))
    else:
        return "Errol"
    #Paste logo above background 
    
    '''
    Save new picture LogoReg:
    ----------------
    Param:
    - name_new_picture : ten anh moi
    '''
    name_file = os.path.basename(logo)
    name_new_picture = traindir + str(name_file) +  ".png"
    background.save(name_new_picture)
    new_label(x, y, labeldir, 0 )
    
    

def new_label(x : int, y: int, original_label : string,  labeldir: string, name_file : string):
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

    #Read original babel txt to extract 
    with open(original_label, 'r') as f:
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
        f.close()
    #Thay doi toa do cua Logo sau khi paste
        x_min += x
        y_min += y
        x_max += x
        y_max += y
    #Write to labeldir 
    with open(labeldir,'w') as file_w:   
        l = name_picture + " " + brand_picture + " " + label_number + " " + str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) + "\n"
        '''
        Ex: Highland.png    Highland    label_number    x_min   y_min   x_max   y_max 
        '''
        L = [l]
        file_w.writelines(L)
        file_w.close() 


create_train_example(train_file,background,logo)
            