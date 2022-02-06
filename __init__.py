from mycroft import MycroftSkill, intent_file_handler


class Control(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.intent')
    def handle_control(self, message):
        what = message.data.get('what')
        zone = message.data.get('zone')

        self.speak_dialog('control', data={
            'what': what,
            'zone': zone
        })


def create_skill():
    return Control()

