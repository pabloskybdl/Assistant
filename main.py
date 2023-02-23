# region Imports
import pyttsx3
from decouple import config
from datetime import datetime
# endregion

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# region Starting Engine
engine = pyttsx3.init('sapi5')
# endregion

# region Set Rate
engine.setProperty('rate', 190)
# endregion

# region Set Volume
engine.setProperty('volume', 1.0)
# endregion

# region Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# endregion

# region Conversión Texto a Voz
def speak(text):
    """Usado para decir cualquier texto que le sea entregado"""

    engine.say(text)
    engine.runAndWait()
# endregion

# region Greeting
def greet_user():
    """Saluda al usuario de acuerdo al horario"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos días {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Buenas tardes {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Buenas noches {USERNAME}")
    speak(f"Yo soy {BOTNAME}. ¿Cómo puedo asistirle?")
# endregion