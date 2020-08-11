def pdf(pgs,links):
    import keyboard
    from time import sleep
    keyboard.press_and_release("alt+tab")
    link = links[:-1]  #enter the pdf link     
    for i in range(pgs):       
        keyboard.press_and_release('ctrl+t',do_press=True)
        sleep(1)
        keyboard.write(link+str(i))
        sleep(3)
        keyboard.press_and_release("enter")
        sleep(3)
        keyboard.press_and_release("ctrl+s")
        sleep(3)
        keyboard.write(str(i))
        keyboard.press_and_release("enter")
        sleep(1)
        keyboard.press_and_release("ctrl+w",do_press=True)
        if(i%22==0):
            keyboard.press_and_release('ctrl+r',do_press=True)
        sleep(1)
