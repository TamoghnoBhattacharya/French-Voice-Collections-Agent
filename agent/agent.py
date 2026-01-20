from agent import prompts, safety

class Agent:
    def __init__(self, preset: dict):
        self.preset = preset
        self.state = "START"

    def respond(self, user_input: str) -> str:
        text = ""

        if "robot" in user_input.lower():
            text = prompts.robot_answer(self.preset)
            self.state = "ROBOT"
        elif "marre" in user_input.lower():
            text = prompts.deescalation()
            self.state = "DEESCALATE"
        elif self.state == "START":
            text = prompts.opening_line(self.preset)
            self.state = "IDENTIFICATION"
        elif self.state == "IDENTIFICATION":
            text = prompts.identification()
            self.state = "CONTEXT"
        elif self.state == "CONTEXT":
            text = prompts.context()
            self.state = "PAYMENT"
        elif self.state == "PAYMENT":
            text = prompts.payment_offer()
            self.state = "RESOLUTION"
        else:
            text = prompts.closing()
            self.state = "END"

        assert safety.is_safe(text)
        assert safety.is_french_only(text)

        return text
