from speechbrain.pretrained import SpeakerRecognition
import speech_recognition as sr
import os
import const


def verification():
    dir_path = 'User_Voices'
    files = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            files.append(path)
    print(files)

    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                                   savedir="pretrained_models/spkrec-ecapa-voxceleb")

    for file in files:
        score, prediction = verification.verify_files(const.WAVE_OUTPUT_FILENAME, file)
        status = bool(prediction)
        if status == True:
            return status
            break

    return False


def transform():
    k = verification()
    if (k == True):
        r = sr.Recognizer()
        harvard = sr.AudioFile(const.WAVE_OUTPUT_FILENAME)
        with harvard as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text
    else:
        return False