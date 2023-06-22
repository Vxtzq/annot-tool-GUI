import webbrowser
import os
import pygame
import time

from glob import glob
from replaceformat import *
import random
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.slider import Slider
from pygame_widgets.toggle import Toggle

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
bigfont = pygame.font.Font('freesansbold.ttf', 30)
boxid = [[]]

screen = pygame.display.set_mode([900, 900])
pygame.display.set_caption('Annot tool GUI v1.4')
visualiz = 0
previousImg = pygame.image.load("ressources/previous.png")
previousImg = pygame.transform.scale(previousImg,((120,150)))
nextImg = pygame.image.load("ressources/next.png")
nextImg = pygame.transform.scale(nextImg,((120,150)))
discardImg = pygame.image.load("ressources/discard.png")
discardImg = pygame.transform.scale(discardImg,((155,150)))
endImg = pygame.image.load("ressources/end.png")
endImg = pygame.transform.scale(endImg,((150,150)))
visualizImg = pygame.image.load("ressources/visualize.png")
visualizImg = pygame.transform.scale(visualizImg,((150,150)))
okImg = pygame.image.load("ressources/ok.png")
okImg = pygame.transform.scale(okImg,((150,150)))
plusImg = pygame.image.load("ressources/+.png")
plusImg = pygame.transform.scale(plusImg,((70,70)))
blank2 = pygame.image.load("ressources/bg.jpg")
blank2 = pygame.transform.scale(blank2,((1200,900)))
blank2Rect = blank2.get_rect()
plusImg = pygame.transform.scale(plusImg,((70,70)))
minusImg = pygame.image.load("ressources/-.png")
minusImg = pygame.transform.scale(minusImg,((70,70)))
pointImg = pygame.image.load("ressources/point.png")
pointImg = pygame.transform.scale(pointImg,((40,40)))

icon = pygame.image.load('ressources/icon.png')

bg = pygame.image.load("ressources/bg.jpg")
bg = pygame.transform.scale(bg,((1200,900)))
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
    

    if len(names) == 1:
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
        for i in range(len(names)):
            
            counterlocal += 1
            class_num += 1
            for file in glob(names[i] + "/*"):
                if not "txt" in file:
                    namesid[counterlocal] = [namesid[counterlocal][0],namesid[counterlocal][1]]
                    namesid[counterlocal][1] = counterlocal
                    
                    namesid[counterlocal] = (namesid[counterlocal][0],namesid[counterlocal][1])
                    imglist.append((file,counterlocal))
    counterlocal = 0
    if namesid == []:
        namesid.append(("'@'",0))
        
                
        
        for file in glob("images/*"):
            if not "txt" in file:
                
                namesid[0] = [namesid[0][0],namesid[0][1]]
                namesid[counterlocal][1] = counterlocal
                
                namesid[0] = (namesid[0][0],namesid[0][1])
                imglist.append((file,0))
                
    
    
    
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
    textbox = TextBox(screen, 100, 150, 700, 40, fontSize=30,
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=output, radius=10, borderThickness=5, placeholderText="Your path here")
    textboxlist = TextBox(screen, 100, 550, 700, 40, fontSize=30,
                      borderColour=(0, 0, 0), textColour=(0, 200, 0),
                      onSubmit=func, radius=10, borderThickness=5, placeholderText="Your path here")
    if namesid[0][0] == '@':
        toggle = Toggle(screen, 350, 450, 100, 25,startOn=False)
    else:
        toggle = Toggle(screen, 350, 450, 100, 25,startOn=False)

    slider = Slider(screen, 100, 300, 700, 40, min=1, max=99, step=1, handleRadius=20,handleColour=(0,150,0))
    slider.setValue(20)
    val = TextBox(screen, 830, 300, 50, 50, fontSize=30)
    toggleval = TextBox(screen, 500, 440, 80, 50, fontSize=30)
    
    testpercent = 5
    on = True
    text = ""
    okclick = 0

    def okmenu():
        global on, text,okclick,namesid
        
        if text != "":
            
            names = fast_scandir(text)
            namesid = []
            for element in names:
                
                element = element.replace(os.path.abspath("images/"),"")
                
                element = element.replace("images/","")
                element = element.replace("/*","")
                element = element.replace("/","")
                namesid.append((element,0))
            
            class_num = 0
            
            for i in range(len(names)):
        
        
                class_num += 1
                for file in glob(names[i] + "/*"):
                    if not "txt" in file:
                        namesid[i] = [namesid[i][0],namesid[i][1]]
                        namesid[i][1] = i
                        namesid[i] = (namesid[i][0],namesid[i][1])
                        imglist.append((file,i))
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
        global nextclick,imgnum,imgcounter,firstpos,secondpos,box,imglist,firstcoordnew,secondcoordnew,visualiz,firstcoords,secondcoords,countervis
        if visualiz == 0:
            if annotfinish == 0:
                currentid = imglist[imgcounter][1]
                boxname.clear()
                if imgcounter < len(imglist):
                    nextclick = 1
                    firstcoords.append([])
                    secondcoords.append([])
                    boxid.append([])
                    ids.append([])
                    if visualiz == 0:
                        file = replacetxt(imglist[imgnum][0])
                        if box == None:
                            file = open(file,"a")
                            file.close()
                            
                            file = replacetxt(imglist[imgnum][0])
                            file = open(file, 'r+')
                            file.truncate(0) 
                            file.close()
                            file = replacetxt(imglist[imgnum][0])
                            file = open(file,"a")
                            file.close()
                            
                        else:
                            file = open(file,"a")
                            file.close()
                            file = replacetxt(imglist[imgnum][0])
                            
                            file = open(file, 'r+')
                            file.truncate(0)
                            file.close()
                            
                            file = replacetxt(imglist[imgnum][0])
                            file = open(file,"a")
                            
                            
                            counter = 0
                            for firstposlist,secondposlist in zip(firstcoords[imgcounter],secondcoords[imgcounter]):
                                
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
                                file.write(text)
                                counter += 1
                            file.close()
                                
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
            
        
    def colorize(image, newColor):
        """
        Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
        original).
        :param image: Surface to create a colorized copy of
        :param newColor: RGB color to use (original alpha values are preserved)
        :return: New colorized Surface instance
        """
        image = image.copy()

        
        image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        
        image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

        return image
    def visualize():
        global visualiz,countervis,firstcoords,secondcoords
        visualiz = 1
        
        try:
            img = pygame.image.load(imglist[countervis][0])
            img = pygame.transform.scale(img,((600,600)))
            
        except:
            pass
    imgcounter = 0 
    def traintestsplit():
        global testpercent,imglist
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
        
    def imgDraw(x,y):
        screen.blit(img, (x,y))
    def button(buttonimg,x,y,function):
        global mousex,mousey,imgnum,screen
        
        buttonRect = buttonimg.get_rect()
        screen.blit(buttonimg, (x,y))
        buttonRect[0] = x
        buttonRect[1] = y
        
        if buttonRect.collidepoint (mousex, mousey) :
            
            if pygame.mouse.get_pressed()[0]:
                
                time.sleep(0.35)
                
                function()

                
                    
                
                
            
            buttonimg = colorize(buttonimg,(125,125,125))
            screen.blit(buttonimg, (x,y))
    def discardlist():
        global nametext
        nametext.pop()
        
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
            greet = font.render("Welcome to Annot Tool GUI v1.4 !", True, (0,0,0))
            greetRect = greet.get_rect()
            greetRect.center = (450,20)
            sub = font.render("Are the images into subfolders ? (e. g images/class1/img.png)", True, (0,0,0))
            subRect = sub.get_rect()
            subRect.center = (450,400)
            classes = font.render("Choose classes name (one class at a time)", True, (0,0,0))
            classesRect = classes.get_rect()
            classesRect.center = (410,520)
            percent = font.render("Percentage of images in test.txt (by default : 20%)", True, (0,0,0))
            percentRect = greet.get_rect()
            percentRect.center = (300,255)
            classeslist = font.render(str(nametext), True, (0,0,255))
            classeslistRect = classeslist.get_rect()
            classeslistRect.center = (450,650)
            events = pygame.event.get()
            text = textbox.getText()
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    on = False
                    quit()
            
            path = font.render("Path to custom dataset (by default : images/'): ", True, (0,0,0))
            pathRect = greet.get_rect()
            pathRect.center = (300,100)
            
            button(pygame.transform.scale(discardImg,(60,60)),815,535,discardlist)
            pygame_widgets.update(events)
            screen.blit(path, pathRect)
            screen.blit(classeslist, classeslistRect)
            screen.blit(classes, classesRect)
            screen.blit(sub, subRect)
            screen.blit(percent, percentRect)
            screen.blit(greet, greetRect)
            if toggle.getValue() == True:
                blank2Rect.center = (465,950)
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

    visualizefinish = 0

    def plus():
        global nextclick,currentid
        nextclick = 1
        currentid += 1
        
    def minus():
        global nextclick,currentid
        nextclick = 1
        currentid -= 1
    def finishvisualize():
        global visualizefinish
        visualizefinish = 1
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
        
        try:
            pass
        except:
            pass
        try:
            img = pygame.image.load(imglist[imgnum][0])
            img = pygame.transform.scale(img,((600,600)))
            text = font.render(imglist[imgnum][0], True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (450,20)
            info = font.render("Space bar to delete image", True, (0,0,0))
            infoRect = info.get_rect()
            infoRect.center = (450,700)
            idtext = font.render("Change next box ID", True, (0,0,0))
            idtextRect = idtext.get_rect()
            idtextRect.center = (770,200)
            
            nextboxid = font.render(str(currentid), True, (0,0,0))
            nextboxidRect = nextboxid.get_rect()
            nextboxidRect.center = (760,290)
            
            
        except:
            
            if visualiz == 0:
                text = font.render("Annotation finished", True, (0,0,0))
                annotfinish = 1
                img = pygame.image.load("ressources/blank.png")
                img = pygame.transform.scale(img,((600,600)))
                firstpos = True
                secondpos = False
                firstcoordnew = []
                secondcoordnew = []
                firstcoord = []
                secondcoord = []
                textRect = text.get_rect()
                textRect.center = (300,300)
                button(endImg,340,700,traintestsplit)
                button(visualizImg,60,700,visualize)
            if visualiz == 1:
                if visualizefinish == 0:
                    text = font.render("", True, (0,0,0))
                    secondpos = False
                    fisrtpos = True
                    firstcoordnew = []
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
                                
                                if secondcoordnew[0] > 640:
                                    secondcoordnew[0] = 640
                                if secondcoordnew[1] > 640:
                                    secondcoordnew[1] = 640
                                if firstcoordnew[0] < 40:
                                    firstcoordnew[0] = 40
                                if firstcoordnew[1] < 40:
                                    firstcoordnew[1] = 40
                                if secondcoordnew[0] < 40:
                                    secondcoordnew[0] = 40
                                if secondcoordnew[1] < 40:
                                    secondcoordnew[1] = 40
                                if firstcoordnew[0] > 640:
                                    firstcoordnew[0] = 640
                                if firstcoordnew[1] > 640:
                                    firstcoordnew[1] = 640
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
        localRect.center = (765,355)
        screen.blit(local, localRect)
                        
        
        imgDraw(40,40)
        screen.blit(text, textRect)
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
                    pygame.draw.rect(screen, (0,0,255), pygame.Rect(firstcoord[0], firstcoord[1], mousex-firstcoord[0], mousey-firstcoord[1]),5)
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
                
                
            
                
                visbox = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                pygame.draw.rect(screen, (0,255,255), visbox,5)
                pygame.draw.rect(screen, (0,0,255), visbox,5)
                pygame.draw.circle(screen, (255,0,0), firstposlist, 10)
                
                pygame.draw.circle(screen, (255,0,0), secondposlist, 10)
            
        else:
            counterlocal = 0
            for firstposlist, secondposlist in zip(firstcoords[imgcounter],secondcoords[imgcounter]):
                
                box = pygame.Rect(firstposlist[0], firstposlist[1], secondposlist[0]-firstposlist[0], secondposlist[1]-firstposlist[1])
                
                
                pygame.draw.rect(screen, (0,0,255), box,5)
                
                button(pointImg,firstposlist[0]-20,firstposlist[1]-20,noUse)
                
                
                
                button(pointImg,secondposlist[0]-20,secondposlist[1]-20,noUse)
                for name in namesid:
                    if name[1] == boxid[imgcounter][counterlocal]:
                        namelocal = name[0]
                        
                boxtext = font.render(namelocal, True, (0,0,255))
                boxtextRect = boxtext.get_rect()
                boxtextRect.center = (firstposlist[0]+40,firstposlist[1]-40)
                screen.blit(boxtext,boxtextRect)
                counterlocal  +=1
                
            
        
                
            
        
        
        
        pygame.display.flip()
        pygame.display.update()



    pygame.quit()
except Exception as e:
    import sys
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 24)
    bigfont = pygame.font.Font('freesansbold.ttf', 30)
    boxid = [[]]

    screen = pygame.display.set_mode([900, 900])
    pygame.display.set_caption('Annot tool GUI v1.4')
    def error(error):
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        
        link_color = (100,100,255)
        while True:
            
            screen.fill((255,255,255))
            screen.blit(bg, bgRect)
            
            
            
            greet = font.render("ERROR", True, (0,0,0))
            greetRect = greet.get_rect()
            greetRect.center = (450,20)
            sub = bigfont.render("Error", True, (200,0,0))
            
            subRect = sub.get_rect()
            subRect.center = (450,400)
            
            cause1 = font.render(error + " at line "+str(exc_tb.tb_lineno), True, (200,0,0))
            
            
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
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if rect.collidepoint(pos):
                        webbrowser.open(r"https://github.com/proplayer2020/annot-data-GUI/issues/new")
            if rect.collidepoint(pygame.mouse.get_pos()):
                link_color = (70, 29, 219)

            else:
                link_color = (100, 100, 255)
            screen.blit(greet, greetRect)
            
            pygame.display.flip()
            pygame.display.update()
    error(str(e))

