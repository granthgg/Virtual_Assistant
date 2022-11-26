import datetime
import json
import os
import smtplib
import socket
import sys
import time
import urllib
import webbrowser
import cv2
import pyautogui
import pyttsx3
import pywhatkit as pyw
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary as diction
# install the modules first which are not pre-installed

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

# Give your name here and whatever you want to call your virtual assistant.
ainame = "Paiko"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    wt = time.strftime("%I:%M %p")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print(f"Hello, Good Morning {author}, It's {wt}")
        speak(f"Hello, Good Morning {author}, It's {wt}")
    elif 12 <= hour < 18:
        print(f"Hello, Good Afternoon {author}, It's {wt}")
        speak(f"Hello, Good Afternoon {author}, It's {wt}")
    else:
        print(f"Hello, Good Evening {author}, It's {wt}")
        speak(f"Hello, Good Evening {author}, It's {wt}")

    print(f"Welcome {author}, I am your Virtual Assistant {ainame}. \nHow may i help you now?")
    speak(f"Welcome {author}, I am your Virtual Assistant {ainame}. \nHow may i help you now?")


def hearMe():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # audio = r.listen(source, timeout=4, phrase_time_limit=7)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"{author} said: {query} \n")

    except Exception as e:
        # print(f"Sorry {author}, Say that again....")
        return "None"
    query = query.lower()
    return query


def hearMe_workNow():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # audio = r.listen(source, timeout=4, phrase_time_limit=7)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print("\n")

    except Exception as e:
        # print(f"Sorry {author}, Say that again....")
        return "None"
    query = query.lower()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('heyabuddies5', 'Heya@123')
    server.sendmail('heyabuddies5', to, content)
    server.close()
# User need to put their gmail account email address and password in it, for email function to work.

def TaskExecution():
    wishMe()
    while True:
        query = hearMe().lower()
        if query == 0:
            continue

        if "sleep now" in query or "wait" in query or "pause" in query or "bye" in query:
            print(f"Virtual assistant {ainame} is now sleeping, but you can call me anytime by saying Wake Up")
            speak(f"Virtual assistant {ainame} is now sleeping, but you can call me anytime by saying Wake Up")
            break

        elif 'who are you' in query or 'what can you do' in query:
            print(f'I am your virtual assistant {ainame}. I am programmed to minor tasks like '
                  'opening youtube,google chrome,predict time,search wikipedia,predict weather,'
                  'get top news headline and you can ask me computational or geographical questions too!'
                  '\nJust ask me anything to do.')

            speak(f'I am your virtual assistant {ainame}. I am programmed to minor tasks like '
                  'opening youtube,google chrome,predict time,search wikipedia,predict weather,'
                  'get top news headline and you can ask me computational or geographical questions too!'
                  '\nJust ask me anything to do.')


        elif "made you" in query or "created you" in query:
            print("I was built by the team of 5 members, Who includes Ekta, Riya, Alok, Abhay and Granth.")
            speak("I was built by the team of 5 members, Who includes Ekta, Riya, Alok, Abhay and Granth.")


        elif 'how are you' in query:
            print(f"I'm fine. You're very kind to ask {author}")
            speak(f"I'm fine. You're very kind to ask {author}")

        elif 'what is my name' in query or "what's my name" in query:
            print(f"Your name is {author}")
            speak(f"Your name is {author}")

        elif 'what is your name' in query or "what's your name" in query:
            print(f"My name is {ainame}")
            speak(f"My name is {ainame}")

        elif 'what is love' in query:
            print("It is 7th sense that destroy all other senses")
            speak("It is 7th sense that destroy all other senses")


        elif 'wikipedia' in query or 'search wikipedia' in query:
            print("What you want to search from wikipedia")
            speak("What you want to search from wikipedia")
            z = hearMe().lower()
            print(wikipedia.summary(z, sentences=2) + "\nFor more information opening wikipedia.")
            speak(wikipedia.summary(z, sentences=2) + "for more information opening wikipedia.")
            webbrowser.open_new_tab(wikipedia.page(z).url)
            time.sleep(10)

        elif 'dictionary' in query or 'meaning' in query:
            print("Which word you want to search on dictionary")
            speak("Which word you want to search on dictionary")
            dict = hearMe()
            dict = dict.replace("what is the","")
            dict = dict.replace("of","")
            dict = dict.replace("meaning", "")
            answer = diction.meaning(dict)
            print(f"The meaning of {dict} is {answer}")
            speak(f"The meaning of {dict} is {answer}")
            time.sleep(4)

        elif 'current time' in query or 'time' in query:
            current_time = time.strftime("%I:%M %p")
            print(f"The current time is: {current_time}")
            speak(f"The current time is: {current_time}")
            time.sleep(2)


        elif 'news' in query or 'news headlines' in query or 'current news' in query:
            speak("News headlines are")
            print("News headlines are")
            query = query.replace("news", "")
            n_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=88442216a9c04e40b98743f3bb9dceb7"
            news = requests.get(n_url).text
            news = json.loads(news)
            art = news['articles']
            i = 0
            for article in art:
                i += 1
                if i == 2:
                    print(article['title'])
                    speak(article['title'])
                    print(article['description'])
                    speak(article['description'])
                    speak("Say Yes for more news otherwise no")
                    option = hearMe().lower()
                    if 'yes' in option:
                        speak("Moving forward to Next news ")
                        i = 0
                        continue

                    elif 'no' in option:
                        break

                    elif 'none' in option:
                        speak("Moving forward to Next news, as you did not say anything")
                        i = 0
                        continue

            time.sleep(3)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            print("Google chrome is now opened")
            speak("Google chrome is now opened")
            time.sleep(10)


        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            print("Instagram is now opened")
            speak("Instagram is now opened")
            time.sleep(10)
        # here we can repeat the above lines to open various websites.

        elif 'search google' in query or 'search on google' in query:
            print(f"What do you need to search on Google {author} ?")
            speak(f"What do you need to search on Google {author} ?")
            um = hearMe().lower()
            print(f"{um}")
            speak(f"{um}")
            webbrowser.open(f"https://www.google.com/search?q={um}")
            time.sleep(12)

        elif 'ip address' in query:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")
            time.sleep(2)


        elif 'location' in query or 'where am i' in query:
            print("Checking your approximate location")
            speak("Checking your approximate location")
            try:
                with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                    data = json.loads(url.read().decode())
                    country = data['country_name']
                    state = data['state']
                    city = data['city']
                    print('We are in ' + city + ' of state ' + state + ' in ' + country)
                    speak('We are in ' + city + ' of state ' + state + ' in ' + country)
                    time.sleep(3)

            except Exception as e:
                print(f"Sorry {author}, can't find due to network problem")
                speak(f"Sorry {author}, can't find due to network problem")


        elif 'open command prompt' in query:
            os.system("start cmd")
            print(f"Opening command prompt")
            speak(f"Opening command prompt")
            time.sleep(5)


        elif 'open control panel' in query:
            os.system("start Control Panel")
            print(f"Opening Control Panel")
            speak(f"Opening Control Panel")
            time.sleep(5)


        elif 'open steam' in query:
            filepath = "C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(filepath)
            print(f"Opening steam")
            speak(f"Opening steam")
            time.sleep(8)

        elif 'open application' in query:
            speak("which app do you want to open")
            z = hearMe().lower()
            x = "opening" + z
            speak(x)
            os.system(z)


        elif 'open vs code' in query:
            filepath = "C:\\Users\\grant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile("filepath")
            print(f"Opening VS Code")
            speak(f"Opening VS code")
            time.sleep(5)
        # here we can repeat the above lines to open various program on our local system of author or user
        # we just need provide the file path of program we need to open here

        elif 'close steam' in query:
            print("Closing steam")
            speak("Closing steam")
            os.system("taskkill /f /im steam.exe")
            time.sleep(5)
        # here we can repeat the above lines to close various program on our local system of author or user

        elif 'play youtube' in query or 'search youtube' in query or 'open youtube' in query:
            print(f"What do you want to see on YouTube")
            speak(f"What do you want to see on YouTube")
            um = hearMe().lower()
            pyw.playonyt(f"{um}")
            time.sleep(5)

        elif 'send message' in query or 'send whatsapp message' in query:
            print("Whom would you like to send messages")
            speak("Whom would you like to send messages")
            num = input("Enter the number: \n")

            print("What is your message")
            speak("What is your message")
            msg = hearMe().lower()
            print(f"Your message: {msg}")

            print("Please Enter the time to send this message")
            speak("Please Enter the time to send this message")
            TH = int(input("Enter Hour in 24hr format: \n"))
            TM = int(input("Enter Minute: \n"))

            pyw.sendwhatmsg(num, msg, TH, TM)
            time.sleep(5)

        elif 'send email' in query:
            print(f"What would you like to send {author}")
            speak(f"What would you like to send {author}")
            content = hearMe().lower()
            print("Whom would you like to send this, Enter the Email address")
            speak("Whom would you like to send this, Enter the Email address")
            to = input("Enter the Email address: \n")
            sendEmail(to, content)
            print("Email has been sent")
            speak("Email has been sent")
            time.sleep(5)


        elif 'click photo' in query or 'photo' in query:
            print("To click the photo, Say Cheese otherwise Say Close Camera")
            speak("To click the photo, Say Cheese otherwise Say Close Camera")
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("Camera")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                cv2.imshow("Camera", frame)
                k = cv2.waitKey(1)
                cp = hearMe().lower()
                if 'close camera' in cp:
                    print("Closing Camera")
                    break
                elif 'cheese' in cp:
                    img_name = "Picture{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} Captured!".format(img_name))
                    img_counter += 1

            cam.release()
            cv2.destroyAllWindows()
            print("Photo's are taken and saved in the main folder")
            speak("Photo's are taken and saved in the main folder")
            time.sleep(10)


        elif 'take screenshot' in query or 'screenshot' in query:
            print("please give name for screenshot file")
            speak("please give name for screenshot file")
            file_name = hearMe().lower()
            speak("Please hold the screen,while i am taking the screenshot in 3 seconds")
            print("Please hold the screen,while i am taking the screenshot in 3 seconds")
            time.sleep(4)
            img = pyautogui.screenshot()
            img.save(f"{file_name}.png")
            print("Screenshot is taken and saved in the main folder")
            speak("Screenshot is taken and saved in the main folder")


        elif 'shut down this pc' in query:
            print('Are you sure to shutdown the pc: yes/no')
            speak("Are you sure to shutdown the pc ")
            speak("Say Yes if you are sure else say No")
            x = hearMe().lower()
            if 'yes' in x:
                print("Ok , your pc will shutdown now")
                speak("Ok , your pc will shutdown now")
                os.system("shutdown /s /t 1")
                time.sleep(3)
            else:
                exit()

        elif 'log out from this pc' in query:
            print('Are you sure to logout the pc: yes/no')
            speak("Are you sure to logout the pc ")
            speak("Say Yes if you are sure else say No")
            x = hearMe().lower()
            if 'yes' in x:
                print("Ok , your pc will logout now")
                speak("Ok , your pc will logout now")
                os.system("shutdown -l")
                time.sleep(3)
            else:
                exit()

        elif 'restart this pc' in query:
            print("Are you sure to restart the pc: Yes/No")
            speak("Are you sure to restart the pc ")
            speak("Say Yes if you are sure else say No")
            x = hearMe().lower()
            if 'yes' in x:
                print("Ok , your pc will restart now")
                speak("Ok , your pc will restart now")
                os.system("shutdown /r /t 1")
                time.sleep(3)
            else:
                exit()

        elif 'sleep this pc' in query:
            print("are you sure to keep the pc in sleep mode: yes/no")
            speak("are you sure to keep the pc in sleep mode")
            speak("say yes if you are sure else say no")
            x = hearMe().lower()
            if 'yes' in x:
                print("Ok , your pc will sleep now")
                speak("Ok , your pc will sleep now")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                time.sleep(3)
            else:
                exit()

        elif 'weather' in query or 'temperature' in query:
            print("Please give place for weather")
            speak("Please give place for weather")
            city_name = hearMe()
            print(city_name)
            w_url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + "5e1ebf12be9907e4e359b1078088aab6" + "&q=" + city_name
            response = requests.get(w_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                tempC = (y["temp"] - 273)
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print("Temperature in C : " + ("{0:.2f}".format(tempC)) +
                      "\nHumidity in % : " + str(current_humidity) +
                      "\nDescription : " + str(weather_description))
                speak("Temperature in celsius = " + ("{0:.2f}".format(tempC)) +
                      "\nhumidity in % = " + str(current_humidity) +
                      "\ndescription = " + str(weather_description))
                time.sleep(5)



            else:
                print("City not found")
                speak("City not found")

        elif 'tell me' in query or 'solve this question' in query or 'answer me' in query or 'calculate' in query or 'solve' in query:
            print('what question do you want to ask')
            speak('what question do you want to ask')
            question = hearMe()
            app_id = "W4V9XT-3V832PWHAW"
            client = wolframalpha.Client('W4V9XT-3V832PWHAW')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)
            time.sleep(4)



        elif 'joke' in query or 'tell jokes' in query or 'jokes' in query:
            print(f"Here are some jokes for you {author}")
            speak(f"Here are some jokes for you {author}")
            query = query.replace("joke" or "jokes", "")
            j_url = 'https://bestlifeonline.com/hilariously-silly-jokes/'
            jokes = requests.get(j_url)
            parser = BeautifulSoup(jokes.text, 'html.parser')
            joke_s = parser.find('ol').find_all('li')
            i = 0
            for pj in joke_s:
                print(pj.text.strip())
                speak(pj.text.strip())
                i += 1
                if i == 4:
                    print("Do you want to hear more . \nIf yes,then say  yes otherwise  say no")
                    speak("Do you want to hear more . \nIf yes,then say  yes otherwise  say no")
                    choice = hearMe().lower()
                    if 'yes' in choice:
                        i = 0
                        continue
                    elif 'no' in choice:
                        break

        elif 'none' in query:
            print(f"Sorry I did not get anything, Please speak again {author}")
            speak(f"Sorry I did not get anything, Please speak again {author}")

        elif 'hold on' in query:
            print("For now how long you wish to pause me.\nGive in seconds")
            speak("For now how long you wish to pause me")
            wait_sec= int(input("Enter the seconds: "))
            print(f"Sleeping for {wait_sec} seconds")
            speak(f"Sleeping for {wait_sec} seconds")
            time.sleep(wait_sec)

        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            print("sorry! I cant understand but I searched from internet to give your answer")
            speak("sorry! I cant understand but I searched from internet to give your answer")
            speak("Do you want to open it")
            choice = hearMe().lower()
            if 'yes' in choice:
                webbrowser.open(g_url + temp)
                time.sleep(8)
            if 'no' in choice:
                pass
            if 'none' in choice:
                pass


if __name__ == "__main__":
    while True:
        workNow = hearMe_workNow().lower()
        if "wake up" in workNow:
            speak(f"Virtual assistant {ainame} is now waking up")
            speak("Hello, What should i call you from now on? \nPlease enter your name!")
            print("Hello, What should i call you from now on? \nPlease enter your name:")
            author = input("")

            TaskExecution()
        elif "goodbye" in workNow or "stop" in workNow:
            print(f"Virtual assistant {ainame} is now shutting down,Good bye and Thank You")
            speak(f"Virtual assistant {ainame} is now shutting down,Good bye and Thank You")
            sys.exit()
