import speech_recognition as sr
import pyautogui as pg
import platform
import webbrowser

moveCommands = { 'left': (-20, 0),
            'right': (20, 0),
            'up': (0, -20),
            'down': (0, 20)}
hotkeyCommands = {'open new window': ('command', 'n'),
            'open new page': ('command', 't'),
            'page one': ('command', '1'),
            'page 1': ('command', '1'),
            'page two': ('command', '2'),
            'page 2': ('command', '2'),
            'page three': ('command', '3'),
            'page 3': ('command', '3'),
            'page four': ('command', '4'),
            'page 4': ('command', '4'),
            'page five': ('command', '5'),
            'page 5': ('command', '5'),
            'page six': ('command', '6'),
            'page 6': ('command', '6'),
            'page seven': ('command', '7'),
            'page 7': ('command', '7'),
            'page eight': ('command', '8'),
            'page 8': ('command', '8'),
            'final page': ('command', '9'),
            'next page': ('command', '1')
          }
websiteCommands = {'open google': 'https://www.google.com/',
                   'open youtube': 'https://www.youtube.com/',
                   'open facebook': 'https://www.facebook.com/',
                   'open twitter': 'https://www.twitter.com/',
                   'open instagram': 'https://www.instagram.com/',
                   'open wikipedia': 'https://www.wikipedia.org/',
                   'open amazon': 'https://www.amazon.com/',
                   'open chatgpt': 'https://chat.openai.com/',}

my_system = platform.uname()

print(f"System: {my_system.system}")
offSwitch = 0
responseSwitch = False

def callback(recognizer, audio):
    global offSwitch
    global responseSwitch
    try:
        response = recognizer.recognize_google(audio)
        print(response)
        if responseSwitch:
            pg.write(response)
            responseSwitch = False
        else:
            if "stop listening" == response:
                offSwitch = 1
                print("found stop")
            if response in moveCommands.keys():
                pg.moveRel(moveCommands[response], duration = 0.2)
            elif response in hotkeyCommands.keys():
                pg.hotkey(hotkeyCommands[response])
            elif response.lower() in websiteCommands.keys():
                webbrowser.open(websiteCommands[response.lower()])
            elif response == "click":
                pg.click(pg.position())
            elif response == "enter" or response == "search":
                pg.press('enter')
            elif response == "scroll down":
                pg.scroll(50)
            elif response == "scroll up":
                pg.scroll(-50)
            elif response == "type":
                print("Typing next response:")
                responseSwitch = True
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
    print("ready")

stop_listening = r.listen_in_background(m, callback)

while True:
    if offSwitch == 1:
        stop_listening(wait_for_stop=False)
        print("listening stopped")
        break