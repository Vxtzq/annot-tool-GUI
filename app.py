import webbrowser
import os
import tkinter
from tkinter import filedialog
import pygame
import time
import gc
import sys

from settings import *
from managecfg import *

from screeninfo import get_monitors

for m in get_monitors():
    
    HEIGHT = m.height-50
    

from glob import glob
from PIL import Image

import random
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.slider import Slider
from pygame_widgets.toggle import Toggle

from replaceformat import *
tkinter.Tk().withdraw()

gc.enable()

finish = 0

resized = 0
pygame.init()

boxid = [[]]

imgsize = 416

coef = HEIGHT/900


font = pygame.font.Font('freesansbold.ttf', int(coef*24))
bigfont = pygame.font.Font('freesansbold.ttf', int(coef*30))


screen = pygame.display.set_mode([int(coef*900), int(coef*900)])
pygame.display.set_caption('Annot tool GUI v1.8')
visualiz = 0
previousImg = pygame.image.load("ressources/previous.png")
previousImg = pygame.transform.scale(previousImg,((int(120*coef),int(150*coef))))
nextImg = pygame.image.load("ressources/next.png")
nextImg = pygame.transform.scale(nextImg,((int(120*coef),int(150*coef))))
discardImg = pygame.image.load("ressources/discard.png")
discardImg = pygame.transform.scale(discardImg,((int(155*coef),int(150*coef))))
endImg = pygame.image.load("ressources/end.png")
endImg = pygame.transform.scale(endImg,((int(150*coef),int(150*coef))))
visualizImg = pygame.image.load("ressources/visualize.png")
visualizImg = pygame.transform.scale(visualizImg,((int(150*coef),int(150*coef))))
okImg = pygame.image.load("ressources/ok.png")
okImg = pygame.transform.scale(okImg,((int(150*coef),int(150*coef))))
plusImg = pygame.image.load("ressources/+.png")
plusImg = pygame.transform.scale(plusImg,((int(70*coef),int(70*coef))))
blank2 = pygame.image.load("ressources/bg.jpg")
blank2 = pygame.transform.scale(blank2,((int(1200*coef),int(900*coef))))
blank2Rect = blank2.get_rect()

browseImg = pygame.image.load("ressources/browse.png")
browseImg = pygame.transform.scale(browseImg,((int(110*coef),int(60*coef))))

plusImg = pygame.transform.scale(plusImg,((int(70*coef),int(70*coef))))
minusImg = pygame.image.load("ressources/-.png")
minusImg = pygame.transform.scale(minusImg,((int(70*coef),int(70*coef))))
pointImg = pygame.image.load("ressources/point.png")
pointImg = pygame.transform.scale(pointImg,((int(40*coef),int(40*coef))))
borderImg = pygame.image.load("ressources/border.png")
borderImg = pygame.transform.scale(borderImg,((int(600*coef),int(600*coef))))

specific = None

icon = pygame.image.load('ressources/icon.png')

bg = pygame.image.load("ressources/bg.jpg")
bg = pygame.transform.scale(bg,((int(1200*coef),int(900*coef))))
bgRect = bg.get_rect()
pygame.display.set_icon(icon)

try:
    ids = [[]]

    imglist = []
    def fast_scandir(dirname):
        subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
        for dirnames in list(subfolders):
            subfolders.extend(fast_scandir(dirnames))
        return subfolders
    names = fast_scandir("images/")


    namesid = []
    for element in names:
        
        element = element.replace(os.path.abspath("images/"),"")
        
        element = element.replace("images/","")
        element = element.replace("/*","")
        element = element.replace("/","")
        namesid.append((element,0))




    class_num = 0
    counterlocal = 0


    if names == []:
        
        for i in range(len(names)):
            
            
            class_num += 1
            for file in glob(names[i] + "/*"):
                if not "txt" in file:
                    
                    namesid[counterlocal] = [namesid[counterlocal][0],namesid[counterlocal][1]]
                    namesid[counterlocal][1] = counterlocal
                    
                    namesid[counterlocal] = (namesid[counterlocal][0],namesid[counterlocal][1])
                    imglist.append((file,counterlocal))
            counterlocal += 1
    else:
        counterlocal = 0
        for i in range(len(names)):
            
            
            class_num += 1
            for file in glob(names[i] + "/*"):
                if not "txt" in file:
                    namesid[counterlocal] = [namesid[counterlocal][0],namesid[counterlocal][1]]
                    namesid[counterlocal][1] = counterlocal
                    
                    namesid[counterlocal] = (namesid[counterlocal][0],namesid[counterlocal][1])
                    imglist.append((file,counterlocal))
            counterlocal += 1
    counterlocal = 0

                



    mousex = 0
    mousey = 0
    imgnum = 0

    firstcoords = [[]]
    secondcoords = [[]]

    nametext = []
    def func():
        global textboxlist,nametext
        text = textboxlist.getText()
        textboxlist.setText("")
        nametext.append(text)
        

    output = ""
    textbox = TextBox(screen, int(50*coef), int(150*coef), int(700*coef), int(40*coef), fontSize=int(coef*30),
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=output, radius=10, borderThickness=5, placeholderText="Your path here")
    textboxlist = TextBox(screen, int(100*coef), int(650*coef), int(700*coef), int(40*coef), fontSize=int(coef*30),
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=func, radius=10, borderThickness=5, placeholderText="Your path here")
    sizebox = TextBox(screen, int(100*coef), int(420*coef), int(700*coef), int(40*coef), fontSize=int(coef*30),
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=func, radius=10, borderThickness=5, placeholderText="size")
    if namesid[0][0] == '@':
        toggle = Toggle(screen, int(350*coef), int(450*coef), int(100*coef), int(25*coef),startOn=False)

    else:
        toggle = Toggle(screen, int(350*coef), int(550*coef), int(100*coef), int(25*coef),startOn=True)

    slider = Slider(screen, int(100*coef), int(300*coef), int(700*coef), int(40*coef), min=1, max=99, step=1, handleRadius=20,handleColour=(0,150,0))
    slider.setValue(20)
    val = TextBox(screen, int(830*coef), int(300*coef), int(50*coef), int(50*coef), fontSize=int(coef*30))
    toggleval = TextBox(screen, int(500*coef), int(540*coef), int(80*coef), int(50*coef), fontSize=int(coef*30))

    testpercent = 5
    on = True
    text = ""
    okclick = 0

    def okmenu():
        global on, text,okclick,namesid,toggle,imglist,sizebox,imgsize
        
        file = open("result/obj.names","w")
            
        for classes in namesid:
            file.write(str(classes[0]) +"\n")
        file.close()
        file = open("result/obj.data","w")
        
        
        file.write("classes = "+str(len(namesid)) +"\n")
        file.write("train = "+str(TRAIN_LOC) +"\n")
        file.write("test = "+str(TEST_LOC) +"\n")
        file.write("names = "+str(NAMES) +"\n")
        file.write("backup = "+str(BACKUP_LOC) +"\n")
        file.write("weights = "+str(WEIGHTS_LOC) +"\n")
        
        file.close()
        if YOLO_TINY == False:
            process_file(len(namesid),int(imgsize), int(imgsize),"result/yolo-obj.cfg",0.001)
        else:
            process_file(len(namesid),int(imgsize), int(imgsize),"result/yolo-tiny-obj.cfg",0.001)
        
        if sizebox.getText() != "":
            
            imgsize = int(sizebox.getText())           
        
        if text != "":
            imglist = []
            
            text = text
            
            names = fast_scandir(text)
            
            namesid = []
            
            for element in names:
                
                
                namesid.append((element,0))
                
                
            
            if names == []:
                
                for file in glob(text + "/*"):
                    if not ".txt" in file:
                        namesid.append((file,0))
                        imglist.append((file,0))
            else:
                class_num = 0
                counterlocal = 0
                for i in range(len(names)):
                    
                    
                    class_num += 1
                    
                    for files in glob(names[i] + "/*"):
                        if not "txt" in files:
                            
                            namesid[counterlocal] = [namesid[counterlocal][0].split('/')[-1],namesid[counterlocal][1]]
                            namesid[counterlocal][1] = counterlocal
                            
                            namesid[counterlocal] = (namesid[counterlocal][0],namesid[counterlocal][1])
                            imglist.append((files,counterlocal))
                    
                        
                    
                    counterlocal += 1
                        
            
            
            
            on = False
        else:
            on = False
        
        okclick = 1


    countervis = 0
    firstpos = True
    firstcoord = (0,0)
    firstcoordnew = (0,0)
    secondpos = False
    secondcoord = (0,0)
    secondcoordnew = (0,0)
    nullclick = 0
    namelocal = 0


    def discard():
        global imgcounter,visualiz,nextclick,firstcoords,secondcoords,boxid
        if visualiz == 0:
            firstcoords[imgcounter] = []
            secondcoords[imgcounter] = []
            boxid[imgcounter] = []
        nextclick = 1
        
        
    def browse():
        global text
        
        folder_path = filedialog.askdirectory()
        if "()" in str(folder_path):
            pass
        else:
            
            text = folder_path
            textbox.setText(text)    

    previousclick = 0
    def previous():
        
        global previousclick,imgnum,firstpoms,secondpos,firstcoords,secondcoords,imgcounter,countervis,firstcoord,secondcoord,firstcoordnew,secondcoordnew
        if visualiz == 0:
            if annotfinish == 0:
                if imgcounter > 0:
                    previousclick = 1
                    firstpos = True
                    secondpos = False
                    imgcounter-= 1
                    imgnum -=1
                    
                    
                    
                    try:
                        os.remove(replacetxt(imglist[imgnum-1][0]))
                    except:
                        pass
                else:
                    previousclick = 1
        if visualiz == 1:
            if countervis > 0:
                countervis -= 1
                previousclick = 1
                
            else:
                previousclick = 1
                
                
    try:
        currentid = imglist[0][1]
    except:
        if on == False:
             
             currentid = imglist[0][1]


        
    nextclick = 0
    def nextimg():
        global nextclick,resized,imgnum,imgcounter,firstpos,secondpos,box,imglist,firstcoordnew,secondcoordnew,visualiz,firstcoords,secondcoords,countervis
        if visualiz == 0:
            if annotfinish == 0:
                resized = 0
                currentid = imglist[imgcounter][1]
                boxname.clear()
                if imgcounter < len(imglist):
                    nextclick = 1
                    firstcoords.append([])
                    secondcoords.append([])
                    boxid.append([])
                    ids.append([])
                    if visualiz == 0:
                        filetxt = replacetxt(imglist[imgnum][0])
                        if box == None:
                            filetxt = open(filetxt,"a")
                            filetxt.close()
                            
                            filetxt = replacetxt(imglist[imgnum][0])
                            filetxt = open(filetxt, 'r+')
                            filetxt.truncate(0) 
                            filetxt.close()
                            filetxt = replacetxt(imglist[imgnum][0])
                            filetxt = open(filetxt,"a")
                            filetxt.close()
                            
                        else:
                            filetxt = open(filetxt,"a")
                            filetxt.close()
                            filetxt = replacetxt(imglist[imgnum][0])
                            
                            filetxt = open(filetxt, 'r+')
                            filetxt.truncate(0)
                            filetxt.close()
                            
                            filetxt = replacetxt(imglist[imgnum][0])
                            filetxt = open(filetxt,"a")
                            
                            
                            counter = 0
                            for firstposlist,secondposlist in zip(firstcoords[imgcounter],secondcoords[imgcounter]):
                                
                                centerx = (firstposlist[0]+secondposlist[0])/2-40
                                centery = (firstposlist[1]+secondposlist[1])/2-40
                                centerx = centerx /600*coef
                                centery = centery / 600*coef
                                
                                width = secondposlist[0]-firstposlist[0]
                                height=secondposlist[1]-firstposlist[1]
                                width = round(width,5)/600*coef
                                height = round(height,5)/600*coef
                                
                                centerx = round(centerx,5)
                                centery = round(centery,5)
                                width = round(width,5)
                                height = round(height,5)
                                
                                width = abs(width)
                                height = abs(height)
                                ID = imglist[imgnum][1]
                                text = str(ids[imgnum][counter])+ " "+str(centerx)+" "+str(centery)+" "+str(width)+" "+str(height)+"\n"
                                filetxt.write(text)
                                counter += 1
                            filetxt.close()
                                
                        firstpos = True
                        secondpos = False
                        imgcounter += 1
                        
                    else:
                        nextclick = 1
        imgnum +=1
        if visualiz == 1:
            if countervis < len(imglist):
                countervis += 1
                firstpos = False
                secondpos = True
                
                firstcoord = firstcoords[countervis]
                secondcoord = secondcoords[countervis]
                nextclick =1
            else:
                nextclick = 1
            
        
    def colorize(image, new_color):
        """
        Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
        original).
        :param image: Surface to create a colorized copy of
        :param new_color: RGB color to use (original alpha values are preserved)
        :return: New colorized Surface instance
        """
        image = image.copy()

        
        image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        
        image.fill(new_color[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

        return image
    def visualize():
        global visualiz,countervis,firstcoords,secondcoords
        visualiz = 1
        
        try:
            img = pygame.image.load(imglist[countervis][0])
            img = pygame.transform.scale(img,((int(600*coef),int(600*coef))))
            
        except:
            pass
    imgcounter = 0 
    def traintestsplit():
        
        global testpercent,imglist,finish
        counter = 0
        alltxt = []
        random.shuffle(imglist)
        percent = len(imglist)*testpercent//100
        
        for i in range(len(names)):
            
            for file in glob(names[i]):
                
                if not "txt" in file:
                    alltxt.append(file)
            counter += 1
        random.shuffle(alltxt)
        file = open("result/test.txt","w")
        counter = 0
        for i in range(percent):
            name = imglist[counter][0]
            file.write(os.path.abspath(name)+"\n")
            counter +=1
        
        file = open("result/train.txt","w")  
        for i in range(len(imglist)-percent):
            name = imglist[counter][0]
            file.write(os.path.abspath(name)+"\n")
            counter +=1
        finish = 1
    def imgDraw(x,y):
        global coef
        screen.blit(img, (x,y))
        screen.blit(borderImg, (x,y))
    def button(buttonimg,x,y,function):
        global mousex,mousey,imgnum,screen,okclick,coef
        
        buttonRect = buttonimg.get_rect()
        screen.blit(buttonimg, (int(x*coef),int(y*coef)))
        buttonRect[0] = int(coef*x)
        buttonRect[1] = int(coef*y)
        
        if buttonRect.collidepoint (mousex, mousey) :
            
            if pygame.mouse.get_pressed()[0]:
                
                okclick = 1
                time.sleep(0.2)
                
                function()

                
                    
                
                
            
            buttonimg = colorize(buttonimg,(125,125,125))
            screen.blit(buttonimg, (int(coef*x),int(coef*y)))
    def discardlist():
        global nametext
        if len(nametext) > 0:
            nametext.pop()
    def finishall():
        onfinish = True
        while onfinish:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            
            greet = font.render("Data is ready, you can now close this window", True, (0,0,0))
            greetRect = greet.get_rect()
            greetRect.center = (int(coef*450),int(coef*450))
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    onfinish = False
                    quit()
            
            
            screen.blit(greet, greetRect)
            
            pygame.display.flip()
            pygame.display.update()
    first = 1
    def menu():
        global textbox,first,output,on,text,okImg,mousex,mousey,testpercent,toggle,nametext,namesid,blank2,blank2Rect
        
        
        while on:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            mousex,mousey = pygame.mouse.get_pos()
            testpercent = slider.getValue()
            togglevalue = toggle.getValue()
            
            val.setText(testpercent)
            toggleval.setText(str(toggle.getValue()))
            greet = font.render("Welcome to Annot Tool GUI v1.8 !", True, (0,0,0))
            greetRect = greet.get_rect()
            greetRect.center = (int(coef*450),int(coef*20))
            size = font.render("Enter image size (default : 416)", True, (0,0,0))
            sizeRect = greet.get_rect()
            sizeRect.center = (int(coef*300),int(coef*380))
            sub = font.render("Are the images into subfolders ? (e. g images/class1/img.png)", True, (0,0,0))
            subRect = sub.get_rect()
            subRect.center = (int(coef*450),int(coef*500))
            classes = font.render("Choose classes name (one class at a time)", True, (0,0,0))
            classesRect = classes.get_rect()
            classesRect.center = (int(coef*410),int(coef*620))
            percent = font.render("Percentage of images in test.txt (by default : 20%)", True, (0,0,0))
            percentRect = greet.get_rect()
            percentRect.center = (int(coef*300),int(coef*255))
            classeslist = font.render("classes : "+str(nametext), True, (0,0,255))
            
            classeslistRect = classeslist.get_rect()
            classeslistRect.center = (int(coef*450),int(coef*750))
            events = pygame.event.get()
            text = textbox.getText()
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    on = False
                    quit()
            
            path = font.render("Path to custom dataset (by default : images/'): ", True, (0,0,0))
            pathRect = greet.get_rect()
            pathRect.center = (int(coef*300),int(coef*100))
            button(browseImg,760,140,browse)
            button(pygame.transform.scale(discardImg,(60,60)),815,635,discardlist)
            pygame_widgets.update(events)
            screen.blit(path, pathRect)
            screen.blit(size, sizeRect)
            screen.blit(classeslist, classeslistRect)
            screen.blit(classes, classesRect)
            screen.blit(sub, subRect)
            screen.blit(percent, percentRect)
            screen.blit(greet, greetRect)
            if toggle.getValue() == True:
                blank2Rect.center = (int(coef*465),int(coef*1050))
                screen.blit(blank2,blank2Rect)
            button(okImg,700,700,okmenu)
            pygame.display.flip()
            pygame.display.update()
        if first == 1:
            
            counterloc = 0
            
            if toggle.getValue() == False:
                namesid.clear()
                for element in nametext:
                    
                    namesid.append((element, counterloc))
                    counterloc += 1
                    
            
            first = 0
        
            
    VISUALIZEFINISH = 0

    def plus():
        global nextclick,currentid,okclick
        nextclick = 1
        currentid += 1
        okclick = 1
        
    def minus():
        global nextclick,currentid,okclick
        nextclick = 1
        currentid -= 1
        okclick = 1
    def finishvisualize():
        global VIZUALIZEFINISH
        VISUALIZEFINISH = 1
    def noUse():
        global nextclick
        nextclick = 1

    box = None
    annotfinish = 0
    running = True
    info = None
    clickcooldown = 0
    nextboxid = None
    nextboxidRect = None

    boxname = []

    while running:

        screen.fill((255, 255, 255))
        screen.blit(bg, bgRect)
        menu()
        if finish == 1:
            finishall()
        try:
            pass
        except:
            pass
        try:
            img = pygame.image.load(imglist[imgnum][0])
            img = pygame.transform.scale(img,((int(coef*600),int(coef*600))))
            if resized == 0:
                
                PILimg = Image.open(imglist[imgnum][0])
                PILimg = PILimg.resize((imgsize,imgsize))
                
                PILimg = PILimg.save(imglist[imgnum][0])
                resized = 1
            text = font.render(imglist[imgnum][0], True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (int(coef*450),int(coef*20))
            info = font.render("Space bar to delete image", True, (0,0,0))
            infoRect = info.get_rect()
            infoRect.center = (int(coef*450),int(coef*700))
            num = font.render("Image "+str(imgcounter+1)+" of "+str(len(imglist)), True, (0,0,0))
            numRect = num.get_rect()
            numRect.center = (int(coef*100),int(coef*850))
            idtext = font.render("Change next box ID", True, (0,0,0))
            idtextRect = idtext.get_rect()
            idtextRect.center = (int(coef*770),int(coef*200))
            
            nextboxid = font.render(str(currentid), True, (0,0,0))
            nextboxidRect = nextboxid.get_rect()
            nextboxidRect.center = (int(coef*760),int(coef*290))
            
            
        except Exception as e:            
            specific = e
            if visualiz == 0:
                text = font.render("Annotation finished", True, (0,0,0))
                annotfinish = 1
                info = font.render("", True, (0,0,0))
                img = pygame.image.load("ressources/blank.png")
                img = pygame.transform.scale(img,((600*coef,600*coef)))
                num = font.render("", True, (0,0,0))
                numRect = num.get_rect()
                numRect.center = (100,850)
                firstpos = True
                secondpos = False
                firstcoordnew = []
                secondcoordnew = []
                firstcoord = []
                secondcoord = []
                textRect = text.get_rect()
                textRect.center = (int(coef*300),int(coef*300))
                button(endImg,340,700,traintestsplit)
                button(visualizImg,60,700,visualize)
            if visualiz == 1:
                if VISUALIZEFINISH == 0:
                    text = font.render("", True, (0,0,0))
                    secondpos = False
                    fisrtpos = True
                    firstcoordnew = []
                    num = font.render("", True, (0,0,0))
                    numRect = num.get_rect()
                    numRect.center = (100,850)
                    secondcoordnew = []
                    firstcoord = []
                    secondcoord = []
                    button(endImg,340,700,traintestsplit)
                    info = font.render("", True, (0,0,0))
                    infoRect = info.get_rect()
                    infoRect.center = (450,700)
                    try:
                        name = imglist[countervis]
                    except:
                        finishvisualize()
                    
                    img = pygame.image.load(name[0])
                    img = pygame.transform.scale(img,((600,600)))
                    
                else:
                    
                    info = font.render("", True, (0,0,0))
                    infoRect = info.get_rect()
                    infoRect.center = (450,700)
                    
                    
                    if countervis == len(imglist):
                        text = font.render('Finished, click on "prepare data for training"', True, (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (330,300)
                        text2 = font.render('if you are satisfied', True, (0,0,0))
                        text2Rect = text2.get_rect()
                        text2Rect.center = (300,325)
                        img = pygame.image.load("ressources/blank.png")
                        img = pygame.transform.scale(img,((600,600)))
                    else:
                        text2 = font.render('', True, (0,0,0))
                        text2Rect = text2.get_rect()
                        text2Rect.center = (300,325)
                        text = font.render('', True, (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (330,300)
                        img = pygame.image.load(imglist[countervis][0])
                        img = pygame.transform.scale(img,((600,600)))
                    
                    
                    
                    
                    button(endImg,340,700,traintestsplit)
                    
        
        
        
        mousex,mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                
                if previousclick == 0 and nextclick ==0 and okclick == 0:
                    clickcooldown = 0
                    
                    if visualiz==0:
                        if firstpos == True:
                            secondpos  = True
                            firstpos = False
                            
                            firstcoord=(mousex,mousey)
                        else:
                            secondpos = False
                            firstpos = True
                            secondcoord=(mousex,mousey)
                        if firstpos == True:
                            if secondpos == False:
                                
                                firstcoordnew = [firstcoord[0],firstcoord[1]]
                                secondcoordnew = [secondcoord[0],secondcoord[1]]
                                
                                if secondcoordnew[0] > int(640*coef):
                                    secondcoordnew[0] = int(640*coef)
                                if secondcoordnew[1] > int(640*coef):
                                    secondcoordnew[1] = int(640*coef)
                                if firstcoordnew[0] < int(40*coef):
                                    firstcoordnew[0] = int(40*coef)
                                if firstcoordnew[1] < int(40*coef):
                                    firstcoordnew[1] = int(40*coef)
                                if secondcoordnew[0] < int(40*coef):
                                    secondcoordnew[0] = int(40*coef)
                                if secondcoordnew[1] < int(40*coef):
                                    secondcoordnew[1] = int(40*coef)
                                if firstcoordnew[0] > int(640*coef):
                                    firstcoordnew[0] = int(640*coef)
                                if firstcoordnew[1] > int(640*coef):
                                    firstcoordnew[1] = int(640*coef)
                                firstcoordnew = tuple(firstcoordnew)
                                secondcoordnew = tuple(secondcoordnew)
                                firstcoords[imgcounter].append(firstcoordnew)
                                secondcoords[imgcounter].append(secondcoordnew)
                                
                                boxid[imgcounter].append(currentid)
                                ids[imgcounter].append(currentid)
                                boxname.append(None)
                else:
                    
                    previousclick = 0
                    nextclick = 0
                    
                
                    okclick = 0
                            
            if event.type == pygame.KEYDOWN:
                if visualiz == 0:
                    if annotfinish == 0:
                        
                        if event.key == pygame.K_SPACE:
                            if visualiz == 0:
                                if annotfinish == 0:
                                    firstcoords[imgcounter] = []
                                    os.remove(imglist[imgcounter][0])
                                    del imglist[imgcounter]
                                    
                                    imgnum +=1
                                    secondcoords[imgcounter] = []
                                    nullclick = 1
                            
                            
                            
                            
                        
         

        
        
        
       
        
        
            
        button(previousImg,645,10,previous)
        button(nextImg,770,10,nextimg)
        button(discardImg,700,700,discard)
        button(minusImg,650,250,minus)
        button(plusImg,800,250,plus)
        
        for name in namesid:
            if name[1] == currentid:
                namelocal = name[0]
                try:
                    
                    pass
                except:
                    pass
        if currentid > len(namesid)-1:
            namelocal = "None"
        if currentid < 0:
            namelocal = "None"
        local = font.render(namelocal, True, (0,0,255))
        localRect = local.get_rect()
        localRect.center = (int(coef*765),int(coef*355))
        screen.blit(local, localRect)
                        
        
        imgDraw(int(coef*40),int(coef*40))
        screen.blit(text, textRect)
        screen.blit(num, numRect)
        screen.blit(info,infoRect)
        screen.blit(nextboxid,nextboxidRect)
        screen.blit(idtext, idtextRect)
        
        try:
            screen.blit(text2, text2Rect)
        except:
            pass

        
        discardrect = discardImg.get_rect()
        if visualiz == 0:
            if annotfinish == 0:
                if firstpos == False:
                    rect = (
                        min(firstcoord[0], mousex),min(firstcoord[1], mousey),
                        abs(mousex-firstcoord[0]), abs(mousey-firstcoord[1]))
                    pygame.draw.rect(screen, (0,0,255), rect,5)
                    pygame.draw.circle(screen, (255,0,0), firstcoord, 10)
                    
                    pygame.draw.circle(screen, (255,0,0), (mousex,mousey), 10)
                
                if firstpos == True:
                    if secondpos == False:
                        if nullclick == 0:
                            secondcoord = [secondcoord[0],secondcoord[1]]
                            firstcoord = [firstcoord[0],firstcoord[1]]
                        if nullclick == 1:
                            nullclick = 0
                
                
        if visualiz==1:
            
            for firstposlist, secondposlist in zip(firstcoords[countervis],secondcoords[countervis]):
                
                
                rect = (
                    min(secondposlist[0], firstposlist[0]), min(secondposlist[1], firstposlist[1]),
                    abs(secondposlist[0]-firstposlist[0]), abs(secondposlist[1]-firstposlist[1]))
                
                visbox = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                pygame.draw.rect(screen, (0,255,255), rect,5)
                
                pygame.draw.circle(screen, (255,0,0), firstposlist, 10)
                
                pygame.draw.circle(screen, (255,0,0), secondposlist, 10)
            
        else:
            counterlocal = 0
            for firstposlist, secondposlist in zip(firstcoords[imgcounter],secondcoords[imgcounter]):
                
                box = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                
                rect = (
                    min(secondposlist[0], firstposlist[0]), min(secondposlist[1], firstposlist[1]),
                    abs(secondposlist[0]-firstposlist[0]), abs(secondposlist[1]-firstposlist[1]))
                for val in rect:
                    val = int(coef*val)
                    
                
                pygame.draw.rect(screen, (0,0,255), rect,5)
                
                #button(pointImg,firstposlist[0]-20,firstposlist[1]-20,noUse)
                
                
                
                #button(pointImg,secondposlist[0]-20,secondposlist[1]-20,noUse)
                for name in namesid:
                    if name[1] == boxid[imgcounter][counterlocal]:
                        namelocal = name[0]
                        
                boxtext = font.render(namelocal, True, (0,0,255))
                boxtextRect = boxtext.get_rect()
                if secondposlist[0] - firstposlist[0] < 0:
                    
                    boxtextRect.center = (secondposlist[0]+int(coef*80),secondposlist[1]-int(coef*20))
                    #boxtextRect.center = (int(coef*boxtextRect.center[0]),int(coef*boxtextRect.center[1]))
                else:
                    
                    
                    boxtextRect.center = (firstposlist[0]+int(coef*80),firstposlist[1]-int(coef*20))
                    #boxtextRect.center = (int(coef*boxtextRect.center[0]),int(coef*boxtextRect.center[1]))
                    
                screen.blit(boxtext,boxtextRect)
                counterlocal  +=1
                
            
        
                
            
        
        
        
        pygame.display.flip()
        pygame.display.update()



    pygame.quit()
except Exception as e:
    
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 24)
    bigfont = pygame.font.Font('freesansbold.ttf', 30)
    boxid = [[]]

    screen = pygame.display.set_mode([900, 900])
    pygame.display.set_caption('Annot tool GUI v1.8')
    def error(error, specific):
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        run = True
        link_color = (100,100,255)
        while run:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            
            
            
            greet = font.render("ERROR", True, (0,0,0))
            greetRect = greet.get_rect()
            greetRect.center = (450,20)
            sub = bigfont.render("Error", True, (200,0,0))
            
            subRect = sub.get_rect()
            subRect.center = (450,400)
            if specific == None:
                cause1 = font.render(error + " at line "+str(exc_tb.tb_lineno), True, (200,0,0))
            else:
                cause1 = font.render(str(specific) + " at line "+str(exc_tb.tb_lineno), True, (200,0,0))
            
            cause1Rect = cause1.get_rect()
            cause1Rect.center = (450,450)
            solution = font.render("Click here to report errors", True, link_color)
            solutionRect = solution.get_rect()
            solutionRect.center = (450,500)
            
            
            screen.blit(sub, subRect)
            screen.blit(cause1, cause1Rect)
            rect = screen.blit(solution, solutionRect)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if rect.collidepoint(pos):
                        webbrowser.open(r"https://github.com/proplayer2020/annot-data-GUI/issues/new")
            if rect.collidepoint(pygame.mouse.get_pos()):
                link_color = (70, 29, 150)

            else:
                link_color = (100, 100, 255)
            screen.blit(greet, greetRect)
            
            pygame.display.flip()
            pygame.display.update()
        pygame.quit()
    error(str(e),specific)


