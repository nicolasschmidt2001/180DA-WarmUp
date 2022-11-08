import speech_recognition as sr  

# get audio from the microphone                                                                       
while True:
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        if r.recognize_google(audio) == "shoot":
            print("shoot!")
        elif r.recognize_google(audio) == "right":
            print("turn right!")
        elif r.recognize_google(audio) == "left":
            print("turn left!")
        elif r.recognize_google(audio) == "reload":
            print("reloading!")
        else:
            print("not a keyword")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
