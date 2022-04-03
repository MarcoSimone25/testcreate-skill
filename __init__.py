from mycroft import MycroftSkill, intent_file_handler


class Testcreate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testcreate.intent')
    def handle_testcreate(self, message):
        self.speak_dialog('testcreate')


def create_skill():
    return Testcreate()

