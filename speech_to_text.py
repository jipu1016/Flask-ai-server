import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile('sample_fixed.wav') as source:  # Pehle se recorded file ka use karega
    audio = recognizer.record(source)  

try:
    text = recognizer.recognize_google(audio, language="hi-IN")
    print("Suna gaya:", text)
except Exception as e:
    print("Error:", str(e))
