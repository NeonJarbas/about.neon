from mycroft.skills import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder


class AboutSkill(MycroftSkill):
    def __init__(self):
        super(AboutSkill, self).__init__(name="AboutSkill")

    @intent_handler(IntentBuilder("license_intent").
                    optionally("Neon").optionally("Long").
                    require("Tell").require("License"))
    def read_license(self, message):
        if message.data.get("Long"):
            self.speak_dialog("license_long")
        else:
            self.speak_dialog("license_short")

    @intent_handler(IntentBuilder("list_skills_intent").optionally("Neon").
                    optionally("Tell").require("Skills"))
    def list_skills(self, message):
        skills_list = []
        # TODO bus api to retrieve loaded skills
        skills_list.sort()
        skills_to_speak = ", ".join(skills_list)
        self.speak_dialog("skills_list", data={"list": skills_to_speak})


def create_skill():
    return AboutSkill()
