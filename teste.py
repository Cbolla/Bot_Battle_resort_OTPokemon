
import pyautogui
import keyboard
import time
import win32api , win32con
bt=se1=se2=se3=sub=se4=se5=0
battle=str(input("Posicione no battle o mouce e digite b: "))
if battle == "b":
    bt=pyautogui.position()
querpoke=str(input("Quer usar o modo de substituir pokemon quando o seu morrer?  S/N"))
if querpoke.upper() == "S":
    seg1=str(input("posicione seu mouse e digite s1 para marcar outro poke caso o seu morra 1: "))
    if seg1 == "s1":
        se1=pyautogui.position()
    seg2=str(input("posicione seu mouse e digite s2 para marcar outro poke caso o seu morra 2: "))
    if seg2 == "s2":
        se2=pyautogui.position()
    seg3=str(input("posicione seu mouse e digite s3 para marcar outro poke caso o seu morra 3: "))
    if seg3 == "s3":
        se3=pyautogui.position()
    seg4=str(input("posicione seu mouse e digite s4 para marcar outro poke caso o seu morra 4: "))
    if seg4 == "s4":
        se4=pyautogui.position()
    seg5=str(input("posicione seu mouse e digite s5 para marcar outro poke caso o seu morra 5: "))
    if seg5 == "s5":
        se5=pyautogui.position()
    sub=1
viuda=0
while True:
    if pyautogui.locateOnScreen("bt.PNG"):
        print("Nada encontrado")
    else:
        pyautogui.moveTo(bt)
        pyautogui.click(bt)
        pyautogui.press("f1")
        pyautogui.press("f2")
        pyautogui.press("f3")
        pyautogui.press("f4")
        pyautogui.press("f5")
        pyautogui.press("f6")
        pyautogui.press("f7")
        pyautogui.press("f8")
        pyautogui.press("f9")
        pyautogui.press("f10")
    if sub == 1:
            if pyautogui.locateOnScreen("vida.PNG"):
                if viuda==0:
                    pyautogui.moveTo(se1)
                    time.sleep(0.3)
                    pyautogui.click(se1)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                elif viuda==1:
                    pyautogui.moveTo(se2)
                    time.sleep(0.3)
                    pyautogui.click(se2)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    time.sleep(0.5)
                elif viuda==2:
                    pyautogui.moveTo(se3)
                    time.sleep(0.3)
                    pyautogui.click(se3)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    time.sleep(0.5)
                elif viuda==3:
                    pyautogui.moveTo(se4)
                    time.sleep(0.3)
                    pyautogui.click(se4)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    time.sleep(0.5)
                elif viuda==4:
                    pyautogui.moveTo(se5)
                    time.sleep(0.3)
                    pyautogui.click(se5)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    time.sleep(0.5)
                    

       
