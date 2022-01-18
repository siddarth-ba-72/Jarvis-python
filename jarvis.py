import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(name):
	hour = int(datetime.datetime.now().hour)
	if hour >= 0  and hour < 12:
		speak(f"Good Morning {name}")
	elif hour >= 12 and hour < 18:
		speak(f"Good Afternoon {name}")
	else:
		speak(f"Good Evening {name}")
	speak("Hope you are doing well, How can I help you?")


def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source,duration=1)
		print("Listening...")
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print("Say that again please...")
		return "None"
	return query


def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('youremail@email.com', 'your_password')
	server.sendmail('youremail@email.com', to, content)
	server.close()


if __name__ == '__main__':
	name = input("What is your name? ")
	wishMe(name)

	if 1:
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Please wait a moment, I am searching wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			speak(results)

		elif 'open youtube' in query:
			speak("Opening Youtube")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Opening Google")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Opening Stackoverflow")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			music_dir = 'D:\\Non Critical\\Songs'
			songs = os.listdir(music_dir)
			print(songs)
			speak(f"Okay, playing your favorite song")
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"The time is {strTime}")

		elif 'open code' in query:
			codepath = "C:\\Users\\Siddarth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codepath)

		elif 'email to me' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "sender_email@email.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry my friend siddarth. I am not able to send this email")


