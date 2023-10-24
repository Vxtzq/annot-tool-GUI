import webbrowser
import os
import tkinter
from tkinter import filedialog
import pygame
import time
import gc
import sys
import cv2

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
buttonrects = []
proceed = 0
zoomming = 0
zoomready = 0
numberframes = 0
infos = []
backup = ""
word = ""

imgsfromvid = []

firstframeinit = 1
buffercounter = 0

img = None
resized = 0

pygame.init()
backupnum = 0
boxid = [[]]

imgsize = 416

hover = 0
index = 0

coef = HEIGHT/900

backups = []
buttonids = []
lastclick = 0

font = pygame.font.Font('freesansbold.ttf', int(coef*24))
bigfont = pygame.font.Font('freesansbold.ttf', int(coef*30))
backupvid = None

screen = pygame.display.set_mode([int(coef*900), int(coef*900)])
pygame.display.set_caption('Annot tool GUI v1.9')
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
nextframeImg = pygame.image.load("ressources/nextframe.png")
nextframeImg = pygame.transform.scale(nextframeImg,((int(150*coef),int(150*coef))))
previousframeImg = pygame.image.load("ressources/previousframe.png")
previousframeImg = pygame.transform.scale(previousframeImg,((int(150*coef),int(150*coef))))
previousframefastImg = pygame.image.load("ressources/previousframefast.png")
previousframefastImg = pygame.transform.scale(previousframefastImg,((int(150*coef),int(150*coef))))
nextframefastImg = pygame.image.load("ressources/nextframefast.png")
nextframefastImg = pygame.transform.scale(nextframefastImg,((int(150*coef),int(150*coef))))
plusImg = pygame.image.load("ressources/+.png")
plusImg = pygame.transform.scale(plusImg,((int(70*coef),int(70*coef))))
blank2 = pygame.image.load("ressources/bg.jpg")
blank2 = pygame.transform.scale(blank2,((int(1200*coef),int(190*coef))))
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
zoomImg = pygame.image.load("ressources/zoom.png")
zoomImg = pygame.transform.scale(zoomImg,((int(150*coef),int(125*coef))))

specific = None
lastctrlz = 0
lastbuttonup = 0

icon = pygame.image.load('ressources/icon.png')

bg = pygame.image.load("ressources/bg.jpg")
bg = pygame.transform.scale(bg,((int(1200*coef),int(900*coef))))
bgRect = bg.get_rect()
pygame.display.set_icon(icon)
def pathnotfound():
    global bg, bgRect #YOLO_TINY,modeltoggle,modeltoggleval,textbox,first,output,on,text,okImg,mousex,mousey,testpercent,toggle,nametext,namesid,blank2,blank2Rect
    
    on = True
    while on:
        
        screen.fill((255,255,255))
        screen.blit(bg, bgRect)
        
        events = pygame.event.get()
        
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                on = False
                
                
        greet = font.render("ERROR", True, (255,0,0))
        greetRect = greet.get_rect()
        greetRect.center = (450*coef,200*coef)
        path = font.render("Path to darknet directory not found, change it in settings.py", True, (0,0,0))
        pathRect = path.get_rect()
        pathRect.center = (int(coef*450),int(coef*450))
        
        screen.blit(path, pathRect)
        screen.blit(greet, greetRect)
        
        pygame.display.flip()
        pygame.display.update()
darknet = 0
if DARKNET_LOC != "":
    darknet = 1
    if os.path.isdir(DARKNET_LOC):
        pass
    else:
        pathnotfound()
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
    firstcoordsnocoef = [[]]
    secondcoordsnocoef = [[]]

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
    textboxlist = TextBox(screen, int(50*coef), int(650*coef), int(700*coef), int(40*coef), fontSize=int(coef*30),
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=func, radius=10, borderThickness=5, placeholderText="Your path here")
    sizebox = TextBox(screen, int(50*coef), int(420*coef), int(700*coef), int(40*coef), fontSize=int(coef*30),
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=func, radius=10, borderThickness=5, placeholderText="size")
    if namesid[0][0] == '@':
        toggle = Toggle(screen, int(350*coef), int(450*coef), int(100*coef), int(25*coef),startOn=False)

    else:
        toggle = Toggle(screen, int(350*coef), int(550*coef), int(100*coef), int(25*coef),startOn=True)
    modeltoggle = Toggle(screen, int(270*coef), int(840*coef), int(40*coef), int(25*coef),startOn=False)
    
    slider = Slider(screen, int(70*coef), int(300*coef), int(700*coef), int(40*coef), min=1, max=99, step=1, handleRadius=20,handleColour=(0,150,0))
    slider.setValue(20)
    val = TextBox(screen, int(800*coef), int(300*coef), int(50*coef), int(50*coef), fontSize=int(coef*30))
    toggleval = TextBox(screen, int(500*coef), int(540*coef), int(80*coef), int(50*coef), fontSize=int(coef*30))
    modeltoggleval = TextBox(screen, int(350*coef), int(825*coef), int(150*coef), int(50*coef), fontSize=int(coef*40))

    testpercent = 5
    on = True
    text = ""
    okclick = 0

    def okmenu():
        global on, text,okclick,namesid,toggle,imglist,sizebox,imgsize
        
        
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

    first = 1
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
        global imgcounter,visualiz,nextclick,firstcoords,secondcoords,firstcoordsnocoef,secondcoordsnocoef,boxid,currentid
        if visualiz == 0:
            firstcoords[imgcounter] = []
            secondcoords[imgcounter] = []
            firstcoordsnocoef[imgcounter] = []
            secondcoordsnocoef[imgcounter] = []
            boxid[imgcounter] = []
        if currentid == None:
            currentid = 0
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
        
        global buffercounter, numberframes,firstframeinit,buffercounter, countervis,imglist,backupnum,backups,previousclick,imgnum,firstpoms,secondpos,firstcoords,secondcoords,imgcounter,countervis,firstcoord,secondcoord,firstcoordnew,secondcoordnew
        buffercounter = 0
        numberframes = 0
        firstframeinit = 1
        if visualiz == 0:
            for file in glob("buffer/*"):
                    os.remove(file)
            if "mp4" in imglist[imgcounter][0]:
                buffercounter -= 1
            if annotfinish == 0:
                backupnum = 0
                
                if len(backups) > 0:
                    os.remove(backups[0])
                else:
                    pass
                backups.clear()
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
        if countervis < len(imglist):
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
        global buffercounter,numberframes, firstcoordsnocoef,secondcoordsnocoef,firstframeinit, buffercounter,countervis,imglist,backupnum,backups, zoomming,nextclick,resized,imgnum,imgcounter,firstpos,secondpos,box,imglist,firstcoordsnocoef,secondcoordsnocoef,firstcoordnew,secondcoordnew,visualiz,firstcoords,secondcoords,countervis
        firstframeinit = 1
        buffercounter = 0
        numberframes = 0
        
        if visualiz == 0:
            
            if annotfinish == 0:
                if "mp4" in imglist[imgcounter][0]:
                    buffercounter += 1
                backupnum = 0
                if len(backups) > 0:
                    os.remove(backups[0])
                else:
                    pass
                for file in glob("buffer/*"):
                    os.remove(file)
                backups.clear()
                resized = 0
                currentid = imglist[imgcounter][1]
                boxname.clear()
                if imgcounter < len(imglist):
                    nextclick = 1
                    firstcoords.append([])
                    secondcoords.append([])
                    firstcoordsnocoef.append([])
                    secondcoordsnocoef.append([])
                    boxid.append([])
                    ids.append([])
                    if visualiz == 0:
                        if zoomming == 0:
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
                                for firstposlist,secondposlist in zip(firstcoordsnocoef[imgcounter],secondcoordsnocoef[imgcounter]):
                                    
                                    centerx = (firstposlist[0]+secondposlist[0])/2-40
                                    
                                    centery = (firstposlist[1]+secondposlist[1])/2-40
                                    centerx = centerx /600
                                    centery = centery / 600
                                    
                                    width = secondposlist[0]-firstposlist[0]
                                    height=secondposlist[1]-firstposlist[1]
                                    width = round(width,5)/600
                                    height = round(height,5)/600
                                    
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
        if countervis < len(imglist):
            if visualiz == 1:
                if zoomming == 0:
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
        global visualiz,countervis,firstcoords,secondcoords,img
        visualiz = 1
        
        try:
            img = pygame.image.load(imglist[countervis][0])
            img = pygame.transform.scale(img,((int(600*coef),int(600*coef))))
            
        except:
            pass
    imgcounter = 0 
    def traintestsplit():
        global testpercent,imglist
        counter = 0
        alltxt = []
        random.shuffle(imglist)
        
        for i in range(len(names)):
            
            for file in glob(names[i]+"/*"):
                
                if not "txt" in file and not "mp4" in file:
                    
                    alltxt.append(file)
            counter += 1
        
        percentval = int(len(alltxt)*testpercent/100)
        
        random.shuffle(alltxt)
        file = open("result/test.txt","w")
        counter = 0
        
        for i in range(percentval):
            name = imglist[counter][0]
            
            file.write(os.path.abspath(name)+"\n")
            counter +=1
        file.close()
        file2 = open("result/train.txt","w")  
        for i in range(len(imglist)-percentval):
            name = imglist[counter][0]
            
            file2.write(os.path.abspath(name)+"\n")
            counter +=1
        file2.close()
        finishprepare()
    def imgDraw(x,y):
        global coef
        screen.blit(img, (x,y))
        screen.blit(borderImg, (x,y))
    def button(buttonimg,x,y,function,ID):
        global buttonids,buttonrects,mousex,mousey,imgnum,screen,okclick,coef,hover,lastclick
        
        buttonRect = buttonimg.get_rect()
        screen.blit(buttonimg, (int(x*coef),int(y*coef)))
        buttonRect[0] = int(coef*x)
        buttonRect[1] = int(coef*y)
        if ID in buttonids:
            pass
        else:
            buttonids.append(ID)
            buttonrects.append(buttonRect)
        
        if buttonRect.collidepoint (mousex, mousey) :
            hover = 1
            okclick = 1
            if pygame.mouse.get_pressed()[0]:
                now = pygame.time.get_ticks()
                if now - lastclick > 250:
                    okclick = 1
                    
                    
                    function()
                    lastclick = now

                
                    
                
                
            
            buttonimg = colorize(buttonimg,(125,125,125))
            screen.blit(buttonimg, (int(coef*x),int(coef*y)))
    def discardlist():
        global nametext
        if len(nametext) > 0:
            nametext.pop()
        time.sleep(0.1)
      
    def finishprepare():
        global bg, bgRect #YOLO_TINY,modeltoggle,modeltoggleval,textbox,first,output,on,text,okImg,mousex,mousey,testpercent,toggle,nametext,namesid,blank2,blank2Rect
        
        on = True
        while on:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            
            events = pygame.event.get()
            
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    on = False
                    
                    
            
            path = font.render("Data is ready, you can now close this window", True, (0,0,0))
            pathRect = path.get_rect()
            pathRect.center = (int(coef*450),int(coef*450))
            
            screen.blit(path, pathRect)
            
            pygame.display.flip()
            pygame.display.update() 
    
    
    def menu():
        global test,folder_path, YOLO_TINY,modeltoggle,modeltoggleval,textbox,first,output,on,text,okImg,mousex,mousey,testpercent,toggle,nametext,namesid,blank2,blank2Rect
        
        model = ""
        
        while on:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            mousex,mousey = pygame.mouse.get_pos()
            testpercent = slider.getValue()
            togglevalue = toggle.getValue()
            modeltogglevalue = modeltoggle.getValue()
            
            
            val.setText(testpercent)
            if str(toggle.getValue()) == "True":
                toggleval.setText("yes")
            if str(toggle.getValue()) == "False":
                toggleval.setText("no")
            if modeltoggle.getValue() == False:
                model = "regular"
                YOLO_TINY = False
            else:
                model = "tiny"
                YOLO_TINY = True
            modeltoggleval.setText(model)
            greet = font.render("Welcome to Annot Tool GUI v1.9 !", True, (0,0,0))
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
            
            yolomodel = font.render("yolo model type : ", True, (0,0,0))
            
            yolomodelRect = yolomodel.get_rect()
            yolomodelRect.center = (int(coef*130),int(coef*855))
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
            button(browseImg,760,140,browse,0)
            button(pygame.transform.scale(discardImg,(60,60)),765,645,discardlist,1)
            
            screen.blit(path, pathRect)
            screen.blit(size, sizeRect)
            screen.blit(classeslist, classeslistRect)
            screen.blit(classes, classesRect)
            screen.blit(sub, subRect)
            screen.blit(percent, percentRect)
            screen.blit(greet, greetRect)
            pygame_widgets.update(events)
            
            if toggle.getValue() == True:
                blank2Rect.center = (int(coef*465),int(coef*690))
                screen.blit(blank2,blank2Rect)
            
            screen.blit(yolomodel, yolomodelRect)
            button(okImg,730,750,okmenu,2)
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
        
        file = open("result/obj.names","w")
        
        for classes in namesid:
            file.write(str(classes[0]) +"\n")
        file.close()
        if darknet == 0:
            file = open("result/obj.data","w")
        if darknet == 1:
            file = open(DARKNET_LOC+"/data/obj.data","w")
        
        
        file.write("classes = "+str(len(namesid)) +"\n")
        file.write("train = "+str(TRAIN_LOC) +"\n")
        file.write("test = "+str(TEST_LOC) +"\n")
        file.write("names = "+str(NAMES) +"\n")
        file.write("backup = "+str(BACKUP_LOC) +"\n")
        if YOLO_TINY == True:
            file.write("weights = "+str(TINY_WEIGHTS_LOC) +"\n")
        else:
            file.write("weights = "+str(WEIGHTS_LOC) +"\n")
        
        file.close()
        if YOLO_TINY == False:
            if darknet == 0:
                process_file(len(namesid),int(imgsize), int(imgsize),"result/yolo-obj.cfg",0.001)
            else:
                process_file(len(namesid),int(imgsize), int(imgsize),DARKNET_LOC+"/data/yolo-obj.cfg",0.001)
        else:
            if darknet == 0:
                process_file(len(namesid),int(imgsize), int(imgsize),"result/yolo-tiny-obj.cfg",0.001)
            else:
                process_file(len(namesid),int(imgsize), int(imgsize),DARKNET_LOC+"/data/yolo-tiny-obj.cfg",0.001)
    VISUALIZEFINISH = 0
    def zoom():
        global zoomming,okclick
        okclick = 1
        zoomming = 1
    def nextframe():
        global box,firstframeinit,imgnum,buffercounter,numberframes,imglist,imgnum,backupvid,okclick,nextclick,firstcoords,secondcoords
        
        
        
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
            for firstposlist,secondposlist in zip(firstcoordsnocoef[imgcounter],secondcoordsnocoef[imgcounter]):
                
                centerx = (firstposlist[0]+secondposlist[0])/2-40
                
                centery = (firstposlist[1]+secondposlist[1])/2-40
                centerx = centerx /600
                centery = centery / 600
                
                width = secondposlist[0]-firstposlist[0]
                height=secondposlist[1]-firstposlist[1]
                width = round(width,5)/600
                height = round(height,5)/600
                
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
        firstframeinit = 1
        box = None
        numberframes +=5
        if len(firstcoords) > 0:
            firstcoords[-1] = []
        if len(secondcoords) > 0:
            secondcoords[-1] = []
        okclick = 1
        imglist[imgnum][0]
        imglist[imgnum] = (backupvid,imglist[imgnum][1])
        nextclick = 1
    def previousframe():
        global firstframeinit,numberframes,imglist,imgnum,backupvid,okclick,nextclick, box,firstcoords,secondcoords
        if len(firstcoords) > 0:
            firstcoords[-1] = []
        if len(secondcoords) > 0:
            secondcoords[-1] = []
        firstframeinit = 1
        
        numberframes -=5
        okclick = 1
        imglist[imgnum] = (backupvid,imglist[imgnum][1])
        nextclick = 1
    def nextframefast():
        global box,firstframeinit,buffercounter,numberframes,imglist,imgnum,backupvid,okclick,nextclick,firstcoords,secondcoords
        
        
        filetxt = replacetxt(str(imglist[imgnum][0]).replace(".mp4",""))
        
        if box == None:
            filetxt = open(filetxt,"a")
            filetxt.close()
            filetxt = replacetxt(str(imglist[imgnum][0]).replace(".mp4",""))

            
            filetxt = open(filetxt, 'r+')
            filetxt.truncate(0) 
            filetxt.close()
            filetxt = replacetxt(str(imglist[imgnum][0]).replace(".mp4",""))

            filetxt = open(filetxt,"a")
            filetxt.close()
            
        else:
            
            filetxt = open(filetxt,"a")
            filetxt.close()
            
            filetxt = replacetxt(str(imglist[imgnum][0]).replace(".mp4",""))

            filetxt = open(filetxt, 'r+')
            filetxt.truncate(0)
            filetxt.close()
            
            filetxt = replacetxt(str(imglist[imgnum][0]).replace(".mp4",""))

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
        firstframeinit = 1
        box = None
        numberframes +=100
        if len(firstcoords) > 0:
            firstcoords[-1] = []
        if len(secondcoords) > 0:
            secondcoords[-1] = []
        okclick = 1
        imglist[imgnum][0]
        imglist[imgnum] = (backupvid,imglist[imgnum][1])
        nextclick = 1
    def previousframefast():
        global firstframeinit,numberframes,imglist,imgnum,backupvid,okclick,nextclick, box,firstcoords,secondcoords
        if len(firstcoords) > 0:
            firstcoords[-1] = []
        if len(secondcoords) > 0:
            secondcoords[-1] = []
        firstframeinit = 1
        
        numberframes -=100
        okclick = 1
        imglist[imgnum] = (backupvid,imglist[imgnum][1])
        nextclick = 1
        
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
        global VISUALIZEFINISH
        VISUALIZEFINISH = 1
    def noUse():
        global nextclick
        nextclick = 1

    
    annotfinish = False
    running = True
    info = 0
    clickcooldown = 0
    nextboxid = 0
    nextboxidRect = 0
    box = None
    boxname = []
    menu()
    
    while running:
        
        
        screen.fill((255, 255, 255))
        
        screen.blit(bg, bgRect)
        
        try:
            if not  "mp4" in imglist[imgnum][0]:
                img = pygame.image.load(imglist[imgnum][0])
                img = pygame.transform.scale(img,((int(coef*600),int(coef*600))))
                if resized == 0:
                
                    PILimg = Image.open(imglist[imgnum][0])
                    PILimg = PILimg.resize((imgsize,imgsize))
                    
                    PILimg = PILimg.save(imglist[imgnum][0])
                    resized = 1
            else:
                cap = cv2.VideoCapture(imglist[imgnum][0])
                backupvid = imglist[imgnum][0]
                totalframes = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                
                
                # set frame position
                
                cap.set(cv2.CAP_PROP_POS_FRAMES,numberframes)
                ret, frame = cap.read()
                img = pygame.image.frombuffer(
                    frame.tobytes(), frame.shape[1::-1], "BGR")
                img = pygame.transform.scale(img,(600*coef,600*coef))
                pygame.image.save(img, "buffer/buffer"+str(buffercounter)+".png")
                imglist[imgnum] = ["buffer/buffer"+str(buffercounter)+".png",imglist[imgnum][1]]
                imglist[imgnum] = ("buffer/buffer"+str(buffercounter)+".png",imglist[imgnum][1])
            if "buffer" in imglist[imgnum][0]:
                button(previousframeImg,200,700,previousframe,13)
                button(nextframeImg,350,700,nextframe,14)
                button(previousframefastImg,45,700,previousframefast,15)
                button(nextframefastImg,505,700,nextframefast,16)
            if "imagefromvideo" in imglist[imgnum][0]:
                button(previousframeImg,200,700,previousframe,13)
                button(nextframeImg,350,700,nextframe,14)
                button(previousframefastImg,45,700,previousframefast,15)
                button(nextframefastImg,505,700,nextframefast,16)
            text = font.render(imglist[imgnum][0], True, (0,0,0))
            textRect = text.get_rect()
            textRect.left = int(coef*10)
            textRect.centery = int(coef*20)
            #textRect.center = (int(coef*450),int(coef*20))
            info = font.render("Space bar to delete", True, (0,0,0))
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
                button(endImg,340,700,traintestsplit,3)
                button(visualizImg,60,700,visualize,4)
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
                    button(endImg,340,700,traintestsplit,5)
                    info = font.render("", True, (0,0,0))
                    infoRect = info.get_rect()
                    infoRect.center = (450,700)
                    try:
                        name = imglist[countervis]
                        img = pygame.image.load(name[0])
                        img = pygame.transform.scale(img,((600*coef,600*coef)))
                    except Exception as e:
                        
                        finishvisualize()
                    
                    
                    
                else:
                    
                    info = font.render("", True, (0,0,0))
                    infoRect = info.get_rect()
                    infoRect.center = (450,700)
                    
                    
                    if countervis >= len(imglist):
                        text = font.render('Finished, click on "prepare data for training"', True, (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (330*coef,300*coef)
                        text2 = font.render('if you are satisfied', True, (0,0,0))
                        text2Rect = text2.get_rect()
                        text2Rect.center = (300*coef,325*coef)
                        img = pygame.image.load("ressources/blank.png")
                        img = pygame.transform.scale(img,((600*coef,600*coef)))
                    else:
                        text2 = font.render('', True, (0,0,0))
                        text2Rect = text2.get_rect()
                        text2Rect.center = (300,325)
                        text = font.render('', True, (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (330,300)
                        index= 0
                        for element in imglist:
                            if "buffer" in element[0]:
                                del imglist[index]
                                index += 1
                            
                        img = pygame.image.load(imglist[countervis][0])
                        img = pygame.transform.scale(img,((600*coef,600*coef)))
                    
                    
                    
                    
                    button(endImg,340,700,traintestsplit,6)
                    
        
        
        
        mousex,mousey = pygame.mouse.get_pos()
        
        events = pygame.event.get()
        
        for event in events:
            
            if event.type == pygame.QUIT:

                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                proceed = 1
                for rect in buttonrects:
                    if rect.collidepoint (mousex, mousey):
                        proceed = 0
                    else:
                        pass
                if proceed == 1:    
                    if previousclick == 0 and nextclick ==0 and okclick == 0 and hover == 0:
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
                                    if zoomming == 0:
                                        firstcoordnew = [firstcoord[0],firstcoord[1]]
                                        firstcoordnocoef = [firstcoord[0],firstcoord[1]]
                                        secondcoordnew = [secondcoord[0],secondcoord[1]]
                                        secondcoordnocoef = [secondcoord[0],secondcoord[1]]
                                        if secondcoordnew[0] > int(640*coef):
                                            secondcoordnew[0] = int(640*coef)
                                            secondcoordnocoef[0] = int(640)
                                        if secondcoordnew[1] > int(640*coef):
                                            secondcoordnew[1] = int(640*coef)
                                            secondcoordnocoef[1] = int(640)
                                        if firstcoordnew[0] < int(40*coef):
                                            firstcoordnew[0] = int(40*coef)
                                            firstcoordnocoef[0] = int(40)
                                        if firstcoordnew[1] < int(40*coef):
                                            firstcoordnew[1] = int(40*coef)
                                            firstcoordnocoef[1] = int(40)
                                        if secondcoordnew[0] < int(40*coef):
                                            secondcoordnew[0] = int(40*coef)
                                            secondcoordnocoef[0] = int(640)
                                        if secondcoordnew[1] < int(40*coef):
                                            secondcoordnew[1] = int(40*coef)
                                            secondcoordnocoef[1] = int(40)
                                        if firstcoordnew[0] > int(640*coef):
                                            firstcoordnew[0] = int(640*coef)
                                            firstcoordnocoef[0] = int(640)
                                        if firstcoordnew[1] > int(640*coef):
                                            firstcoordnew[1] = int(640*coef)
                                            firstcoordnocoef[1] = int(640)
                                        firstcoordnew = tuple(firstcoordnew)
                                        secondcoordnew = tuple(secondcoordnew)
                                        firstcoords[imgcounter].append(firstcoordnew)
                                        secondcoords[imgcounter].append(secondcoordnew)
                                        firstcoordsnocoef[imgcounter].append(firstcoordnocoef)
                                        secondcoordsnocoef[imgcounter].append(secondcoordnocoef)
                                        boxid[imgcounter].append(currentid)
                                        ids[imgcounter].append(currentid)
                                        boxname.append(None)
                
            
            if hover == 0:
                if okclick == 1:
                    okclick = 0
                if nextclick == 1:
                    nextclick = 0
                if previousclick == 1:
                    previousclick = 0
            else:
                hover = 0
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LCTRL] and keys[pygame.K_z]:
                if len(backups) > 0:
                    now = pygame.time.get_ticks()
                    if now- lastctrlz > 200:
                        
                        #imglist[imgcounter] = [imglist[imgcounter][0],imglist[imgcounter][1]]
                        #imglist[imgcounter][0] = backups[len(backups)-1]
                        #imglist[imgcounter] = (imglist[imgcounter][0],imglist[imgcounter][1])
                        pygame.image.save(pygame.image.load(backups[0]), replace(str(imglist[imgnum][0])).replace("backup","")+".png")
                                    
                        
                        
                        #backups.pop()
                        
                        lastctrlz = now
            if event.type == pygame.KEYDOWN:
                if visualiz == 0:
                    if annotfinish == 0:
                        
                        if event.key == pygame.K_SPACE:
                            if visualiz == 0:
                                if annotfinish == 0:
                                    firstcoords[imgcounter] = []
                                    firstcoordsnocoef[imgcounter] = []
                                    os.remove(imglist[imgcounter][0])
                                    del imglist[imgcounter]
                                    
                                    imgnum +=1
                                    secondcoords[imgcounter] = []
                                    secondcoordsnocoef[imgcounter] = []
                                    nullclick = 1
                            
                            
                            
                            
                        
         

        
        
        
       
        
        
        print(imglist)
        button(previousImg,645,10,previous,7)
        button(zoomImg,700,400,zoom,8)
        button(nextImg,770,10,nextimg,9)
        button(discardImg,700,700,discard,10)
        button(minusImg,650,250,minus,11)
        button(plusImg,800,250,plus,12)
        
        for name in namesid:
            if name[1] == currentid:
                namelocal = name[0]
                try:
                    
                    pass
                except:
                    pass
        if currentid > len(namesid)-1:
            currentid = len(namesid)-1
        if currentid < 0:
            currentid = 0
        
        local = font.render(str(namelocal), True, (0,0,255))
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
            if zoomming == 0:
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
                        
            if zoomming == 1:
                if firstpos == False:
                    rect = (
                        min(firstcoord[0], mousex),min(firstcoord[1], mousey),
                        abs(mousex-firstcoord[0]), abs(mousey-firstcoord[1]))
                    pygame.draw.rect(screen, (0,255,0), rect,5)
                    #pygame.draw.circle(screen, (255,0,0), firstcoord, 10)
                    
                    #pygame.draw.circle(screen, (255,0,0), (mousex,mousey), 10)
                    zoomready = 1
                
                if firstpos == True:
                    if secondpos == False:
                        if nullclick == 0:
                            if zoomready == 1:
                                
                                try:
                                    cropped_region = (firstcoord[0]-40*coef,firstcoord[1]-40*coef,secondcoord[0]-firstcoord[0],secondcoord[1]-firstcoord[1])
                                    zoomrect = (
                                        min(firstcoord[0], mousex),min(firstcoord[1], mousey),
                                        abs(mousex-firstcoord[0]), abs(mousey-firstcoord[1]))
                                    
                                    
                                        
                                    if backups == []:
                                        backups.append(replace(str(imglist[imgnum][0])).replace("backup","")+"backup.png")
                                        pygame.image.save(img, replace(str(imglist[imgnum][0])).replace("backup","")+"backup.png")
                                        
                                        imglist[imgcounter] = [replace(str(imglist[imgnum][0])).replace("backup","")+".png",imglist[imgcounter][1]]
                                        imglist[imgcounter] = (imglist[imgcounter][0], imglist[imgcounter][1])
                                        
                                    spriteimg = img.subsurface((zoomrect[0]-40*coef,zoomrect[1]-40*coef,zoomrect[2],zoomrect[3]))
                                    spriteimg = pygame.transform.scale(spriteimg,(imgsize,imgsize))
                                    pygame.image.save(spriteimg, replace(str(imglist[imgnum][0])).replace("backup","")+".png")
                                    
                                    
                                    #screen.blit(spriteimg, (40*coef, 40*coef))
                                    zoomming = 0
                                    zoomready = 0
                                except Exception as e:
                                    print(e)
                            
                                #secondcoord = [secondcoord[0],secondcoord[1]]
                                #firstcoord = [firstcoord[0],firstcoord[1]]
                            
                        if nullclick == 1:
                            nullclick = 0
                
                
        if visualiz==1:
            try:
                if not os.path.getsize(replacetxt(imglist[countervis][0])) == 0:
                    
                    datafile = open(replacetxt(imglist[countervis][0]))             
                    for line in datafile:
                        print(line)
                        backup = ""
                        word = ""
                        infos = []
                        for char in line:
                            if char != " ":
                                
                                backup = backup+char
                                
                            if char == " ":
                                word = backup.replace("\n"," ")
                                infos.append(float(word))
                                print(word)
                                backup = ""
                            
                                
                    
                        word = backup.replace("\n","")
                        infos.append(float(word))
                        infos[0] = int(infos[0])
                        print(infos)
                        centerx = infos[1]
                        centery = infos[2]
                        width = infos[3]
                        height = infos[4]
                        
                        rect = pygame.Rect(0, 0, width*600, height*600)
                        centerx = centerx*600
                        centery = centery*600
                        rect.center = (centerx+40,centery+40)
                        
                        print("coef"+str(coef))
                        
                        visbox = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                        pygame.draw.rect(screen, (0,255,255), rect,5)
                        print(namesid)
                        boxtext = font.render(namesid[infos[0]][0], True, (0,255,255))
                        boxtextRect = boxtext.get_rect()
                        if secondposlist[0] - firstposlist[0] < 0:
                            
                            boxtextRect.center = (centerx*600-width/2*600+100*coef,centery*600-height/2*600)
                            #boxtextRect.center = (int(coef*boxtextRect.center[0]),int(coef*boxtextRect.center[1]))
                        else:
                            
                            
                            boxtextRect.center = (centerx*600-width/2*600+100*coef,centery*600-height/2*600)
                        screen.blit(boxtext,boxtextRect)
                else:
                    
                    pass
                    """
                    pygame.draw.circle(screen, (255,0,0), rect.topleft, 10)
                    
                    pygame.draw.circle(screen, (255,0,0), rect.bottomleft, 10)
                    """
            except:
                pass
                
            
        else:
            counterlocal = 0
            for firstposlist, secondposlist in zip(firstcoords[imgcounter],secondcoords[imgcounter]):
                
                box = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                
                rect = (
                    min(secondposlist[0], firstposlist[0]), min(secondposlist[1], firstposlist[1]),
                    abs(secondposlist[0]-firstposlist[0]), abs(secondposlist[1]-firstposlist[1]))
                for val in rect:
                    val = int(coef*val)
                if firstframeinit == 1:
                    pass
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
        
        if imgnum < len(imglist) and countervis < len(imglist):
            if "buffer" in imglist[imgnum][0]:
                pygame.image.save(img, str(backupvid).replace(".mp4","")+"imagefromvideo"+str(buffercounter)+".png")

                #print(str(backupvid).replace("mp4","")+str(buffercounter)+".png")
                imglist[imgnum] = (str(backupvid).replace(".mp4","")+"imagefromvideo"+str(buffercounter)+".png",imglist[imgnum][1])
                
                imgsfromvid.append((str(backupvid).replace(".mp4","")+"imagefromvideo"+str(buffercounter)+".png",imglist[imgnum][1]))
                
                # Check si imgsfromvid contient des images qui ne sont pas dans imglist et les ajouter
                
                buffercounter += 1
                firstframeinit = 0
                
            
        
                
            
        
        
        
        pygame.display.flip()
        pygame.display.update()



    pygame.quit()
except Exception as e:
    
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 24)
    bigfont = pygame.font.Font('freesansbold.ttf', 30)
    boxid = [[]]

    screen = pygame.display.set_mode([900, 900])
    pygame.display.set_caption('Annot tool GUI v1.9')
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
            print(error)
            print(str(exc_tb.tb_lineno))
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


