import pyautogui
import subprocess
import time

# time.sleep(5)

names = ['Evento_' + str(i) for i in range(1, 14)]

for name in names:

    # Run Simulation

    b = pyautogui.locateOnScreen('Ref/Ref1.PNG')
    w = b.width / 2 + b.left 
    h = b.height / 2 + b.top
    pyautogui.click(w, h, duration=0.25)
    time.sleep(1)

    # Right click on the 

    wh = pyautogui.size()
    w = wh.width/2
    h = wh.height/2 - 200
    pyautogui.moveTo(w, h, duration=0.25)
    pyautogui.rightClick()
    time.sleep(1)

    # Click in 'export .plt'

    b = pyautogui.locateOnScreen('Ref/Ref2.png')
    w = b.width / 2 + b.left 
    h = b.height / 2 + b.top
    pyautogui.click(w, h, duration=0.25)
    time.sleep(1)

    # Write the name and save

    time.sleep(1)
    pyautogui.write(name)
    time.sleep(1)
    pyautogui.write(['enter'])
    time.sleep(1)

    if name != names[-1]:

        # Click in events's names

        b = pyautogui.locateOnScreen('Ref/Ref1.PNG')
        w = b.width / 2 + b.left + 100 
        h = b.height / 2 + b.top
        pyautogui.click(w, h, duration=0.25)
        time.sleep(1)

        # Select Next event

        time.sleep(1)
        pyautogui.write(['down'])
        time.sleep(1)
        pyautogui.write(['enter'])
        time.sleep(1)




















