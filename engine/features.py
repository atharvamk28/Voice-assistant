from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dir = "C:\\Users\\athar\\OneDrive\\Desktop\\Jarvis\\www\\assests\\audio\\start_sound.mp3"
    playsound(music_dir)
