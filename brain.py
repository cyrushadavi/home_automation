__author__ = 'Cyrus'
import config
import speech_recognition as sr

config_dict = config.get_dict_of_params()


class Brain(object):
    def __init__(self, mic, profile):
        """
        Instantiates a new Brain object, which cross-references user
        input with a list of modules. Note that the order of brain.modules
        matters, as the Brain will cease execution on the first module
        that accepts a given input.
        Arguments:
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
        """

        self.mic = mic
        self.profile = profile
        self.get_modules()


passive = True
while passive == True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_wit(audio, config_dict['wit_token'])
