import pygame_widgets
import urllib.request
import sys 
import pygame
from pygame.locals import *
from pygame_widgets.progressbar import ProgressBar

currentfile = ""
error = 0

percent = 0
size = ""

def Handle_Progress(block_num, block_size, total_size):
        global percent, currentfile
        read_data= 0
        
        # calculating the progress
        # storing a temporary value  to store downloaded bytesso that we can add it later to the overall downloaded data
        temp = block_num * block_size
        read_data = temp + read_data
        #calculating the remaining size
        remaining_size = total_size - read_data
        if(remaining_size<=0):
            downloaded_percentage = 100
            remaining_size = 0
        else:
            downloaded_percentage = int(((total_size-remaining_size) / total_size)*(100))
        percent = downloaded_percentage
        screen.fill((255, 255, 255))
        file = font.render(str(currentfile), True, (0,0,0))
        fileRect = file.get_rect()
        fileRect.center = (int(300),int(180))
        downloading = font.render("Downloading :", True, (0,0,0))
        downloadingRect = downloading.get_rect()
        downloadingRect.center = (int(300),int(50))
        sizetext = font.render(str(round(float(total_size/1000000-remaining_size/1000000),1)) +" MB"+"/"+str(round(total_size/1000000, 1)) + " MB", True, (0,0,0))
        sizeRect = sizetext.get_rect()
        sizeRect.center = (int(300),int(400))
        
        screen.blit(sizetext, sizeRect)
        screen.blit(file, fileRect)
        screen.blit(downloading, downloadingRect)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
              pygame.quit()
              sys.exit()

        # Update.

        # Draw.
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(fps)
        
def Download_File(url,save):
        #the url where the file is found
        download_url = url
        #opening the file
        site = urllib.request.urlopen(download_url)
        #getting the meta data
        meta = site.info()
        print("size :", meta.get("Content-Length") + " B")
        
        #where the file will be saved
        save_location = save
        #downloading the file
        urllib.request.urlretrieve(download_url,save_location, Handle_Progress)


 
pygame.init()

font = pygame.font.Font('freesansbold.ttf', int(24))

fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 600, 480
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load('ressources/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Annot tool GUI v1.9')


progressBar = ProgressBar(screen, 50, 100, 500, 40, lambda: percent/100, curved=False)

currentfile = "yolov4-tiny.conv.29"
Download_File('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-tiny/yolov4-tiny.conv.29',"result/yolov4-tiny.conv.29")
currentfile = "yolov4-tiny.weights"
Download_File('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-tiny-weights/yolov4-tiny.weights',"result/yolov4-tiny.weights")
currentfile = "result/yolov4.conv.137"
Download_File('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo/yolov4.conv.137',"result/yolov4.conv.137")
currentfile = "result/yolov4.weights"
Download_File('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-weights/yolov4.weights',"result/yolov4.weights")
pygame.quit()
