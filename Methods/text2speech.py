def read(string):
    from time import sleep
    import pyttsx3
    engine = pyttsx3.init()
    string = string.split("~*~")
     
    engine.say(string[0]+" says")
    engine.runAndWait()
    sleep(0.1)
    
    engine.say(string[1])
    engine.runAndWait()
    sleep(0.1)
    return 1