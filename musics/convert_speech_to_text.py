import pyttsx3
import speech_recognition as sr
def convert_speech_to_text(request):

    r = sr.Recognizer()
    file_path = (request.data['audio_file'])

    hellow = sr.AudioFile(file_path)
    with hellow as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: " + s)
    except Exception as e:
        print("Exception: " + str(e))

    return s

    # print(request.data['audio_file'])
    # file_path = (request.data['audio_file'])
    # print(file_path)
    #
    # audio_file = sr.AudioFile(file_path)
    # r = sr.Recognizer()
    # # r.energy_threshold == 300
    # with sr.AudioFile(file_path) as source:
    #     # listen for the data (load audio to memory)
    #     audio_data = r.record(source)
    #     # recognize (convert from speech to text)
    #     text = r.recognize_google(audio_data)
    #     print(text)
