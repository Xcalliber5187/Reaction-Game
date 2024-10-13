# This code was created to be used in conjuction with a BBC Microbit running the code in Microbit.py , with Pin0 acting as a start button ,
# and Pin 1 and 2 being assigned a left and right button respectively


#Basic Imports

import serial
import time
import pygame
import tkinter as tk
from tkinter import simpledialog

#Starts pygame
pygame.init()

#Sets tkinter variables
root = tk.Tk()
root.geometry("100x100+500+300")
root.withdraw()

#Sets is_running to base True
is_running = True

# 1=Game start  2=Go , 3=Right winner , 4=Left winner , 0 = False start

#Loads the sound file
pygame.mixer.music.load('microwave-beeps-101846.mp3')

# Lists available COM ports , and allows the user to select the appropiate one in the command line
import serial.tools.list_ports 
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
import time
portlist = []
for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))
val = input("select port: COM")
for x in range(0,len(portlist)):
    if portlist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portlist[x])


# Sets up the serial connection with the user specified com port and baud rate of 115200
ser = serial.Serial(portVar, 115200, timeout=0.001)




#Initiates pygame , sets screen size and font
pygame.init()
screen = pygame.display.set_mode((1200, 700))
font = pygame.font.Font(r'ARCADE.TTF', 80)

#Simple function to make text
def make_text(input_text):
    text = font.render(str(input_text), True, (0, 0, 0))
    return text


#Initialises the names
name1 = ""
name2 = ""

#Main loop
try:
    while True:

        #Checks for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break

        if not is_running:
            break


        #Reads the serial data
        data = ser.readline().decode('utf-8').strip()


        #Fills the screen white and displays the title
        screen.fill((255, 255, 255))
        text = font.render("Reaction  Speed  Game", True, (0, 0, 0))
        screen.blit(make_text("Reaction Speed Game"), (screen.get_width() // 2 - (text.get_width()-30) // 2, screen.get_height() // 2 - text.get_height() // 2))

            

        # Render "BitBros" in the custom font
        small_font = pygame.font.Font(r'ARCADE.TTF', 30)
        small_text = small_font.render("Created by BitBros Games ", True, (0, 0, 0))
        screen.blit(small_text, (10, screen.get_height() - small_text.get_height() - 10))
        pygame.display.flip()

        # Checks if names are not defined , and asks for them if they are not       
        if name1 == "" and name2 == "":
            

            

            

            
            name1 = simpledialog.askstring(title="Name", prompt="Right Player:", parent=root)
            name1 = simpledialog.askstring(title="Name", prompt="Right Player:", parent=root)


        #If data is 1 , game starts
        if data == "1":
            
            print("Game Start")
            screen.fill((255, 255, 255))

            #Countdown
            text = make_text(3)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
            pygame.display.flip()
            time.sleep(1)

            screen.fill((255, 255, 255))
            text = make_text(2)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
            pygame.display.flip()
            time.sleep(1)

            screen.fill((255, 255, 255))
            text = make_text(1)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
            pygame.display.flip()
            time.sleep(1)

            screen.fill((255, 255, 255))

            #Waits for data to be 2 to stop unwanted screen refreshing
            while data != "2":
                data = ser.readline().decode('utf-8').strip()

                #Keeps the pygame window responsive
                pygame.event.pump()

                #Break the loop when data=2
                if data == "2":
                    break
        
        #When data is 2, the screen goes black
        if data == "2":
            print("Go")
            pygame.mixer.music.play()
            time.sleep(0.05)
            screen.fill((0, 0, 0))

            #Waits for winner data, while still allowing the window to be exited from
            while data != "3" and data != "4":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                        break

                if not is_running:
                    break

                data = ser.readline().decode('utf-8').strip()

                #If data is 3, print right winner and the time taken
                if data == "3":
                    print("Right Winner")
                    screen.fill((255, 255, 255))
                    pygame.display.flip()

                    text = font.render("Right Winner", True, (0, 0, 0))
                    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
                    pygame.display.flip()

                    time.sleep(3)
                    pygame.event.pump()

                    screen.fill((255, 255, 255))
                    pygame.display.flip()

                    data = ser.readline().decode('utf-8').strip()
                    print("Time taken: ", data)
                    time_text = make_text("Time taken: " + data + "ms")
                    screen.blit(time_text, (screen.get_width() // 2 - time_text.get_width() // 2, screen.get_height() // 2 - time_text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.event.pump()
                    name1 = ""
                    name2 = ""
                    break

                #If data is 4, print left winner and the time taken
                elif data == "4":
                    print("Left Winner")
                    screen.fill((255, 255, 255))
                    pygame.display.flip()

                    text = font.render("Left Winner", True, (0, 0, 0))
                    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
                    pygame.display.flip()

                    time.sleep(3)
                    pygame.event.pump()

                    screen.fill((255, 255, 255))
                    pygame.display.flip()

                    data = ser.readline().decode('utf-8').strip()
                    print("Time taken: ", data)
                    time_text = make_text("Time taken: " + data + "ms")
                    screen.blit(time_text, (screen.get_width() // 2 - time_text.get_width() // 2, screen.get_height() // 2 - time_text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.event.pump()

                    #Resets names
                    name1 = ""
                    name2 = ""
                    break

                #Keeps the pygame window responsive and refreshes the screen
                pygame.event.pump()
                pygame.display.update()

        #Keeps the pygame window responsive , while updating the screen
        pygame.event.pump()
        pygame.display.update()

# Allows the user to exit the program using Ctrl+C
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
    pygame.quit()
