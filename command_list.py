from user_verification import transform
from recording_voice import recording


def command():
    recording()

    if transform() != False:
        print("Yes")