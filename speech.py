import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("🎤 Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("🔍 Recognizing...")
            text = recognizer.recognize_google(audio)
            print("✅ You said: " + text)
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand your audio.")
        except sr.RequestError:
            print("⚠ Could not request results from Google Speech Recognition service.")

if _name_ == "_main_":
    recognize_speech()
