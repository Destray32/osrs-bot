import random
import cv2 as cv
import os
from time import sleep, time
from windowCapture import WindowCapture
from wizja import Vision

import pyautogui as pag
import keyboard


def main():
# initialize the WindowCapture class
    wincap = WindowCapture('Runelite - destray32')
    pls_wait = Vision("zdjecia\\plswait.jpg")
    przycisk = Vision("zdjecia\\przycisk.jpg")
    play = Vision("zdjecia\\play.jpg")

    wielkosci_okna = []
    wielkosci_okna = wincap.wypisz_kordynaty()
    pierwszaPozycjaMyszki = pag.position()

    worldCounter = 0
    wDrugaStrone = False
    wLewo = False
    iloscZmianPozycji = 0

    # sleep na 3 sekundy aby przygotwać pozycje myszki itp.
    sleep(3)
    loop_time = time()

    while(True):
        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        punkty = pls_wait.find(screenshot, 0.5, '')
        punktyPrzycisk = przycisk.find(screenshot, 0.7, '')
        randomowaLiczba = random.randint(0, 5)

        if punktyPrzycisk:
            logowanie(punktyPrzycisk, wincap)
            sleep(18)
            print("czy to dziala?")
            pag.move(0, 10, duration=0.2)
            pag.click()
            sleep(2)
            pag.moveTo(pierwszaPozycjaMyszki, duration=0.2)
            

        if iloscZmianPozycji % 10 == 0:
            pag.moveTo(pierwszaPozycjaMyszki, duration=0.2)
            print("Powrot do pierwszej pozycji myszki")

        if punkty:
            # print("Znaleziono plswait")
            pass
        else:
            sleep(0.5)
            if wLewo == False:
                pag.move(randomowaLiczba, 0, duration=0.1)
                wLewo = True
                iloscZmianPozycji += 1
                print(iloscZmianPozycji)
            else:
                pag.move(-randomowaLiczba, 0, duration=0.1)
                wLewo = False
                iloscZmianPozycji += 1
                print(iloscZmianPozycji)
            pag.click()

            if wDrugaStrone == False:
                if worldCounter < 70:
                    pag.hotkey('ctrl', 'shift', 'right')
                    worldCounter += 1
                else:
                    wDrugaStrone = True
                    pag.hotkey('ctrl', 'shift', 'left')
                    worldCounter -= 1
            if wDrugaStrone == True:
                if worldCounter > 2:
                    pag.hotkey('ctrl', 'shift', 'left')
                    worldCounter -= 1
                else:
                    wDrugaStrone = False
                    pag.hotkey('ctrl', 'shift', 'right')
                    worldCounter += 1


        if keyboard.is_pressed('p'):
            exit()

def logowanie(punktyPrzycisk, wincap):
    tuplePrzycisk = (punktyPrzycisk[0][0], punktyPrzycisk[0][1])

    pozycjaPrzyciskuReal = wincap.get_screen_position(tuplePrzycisk)
    pag.moveTo(pozycjaPrzyciskuReal, duration=0.4)
    pag.click()
    
    sleep(1)
    # tutaj bylo haslo do konta
    sleep(1)

    pag.press('enter')



if __name__ == '__main__':
    main()
