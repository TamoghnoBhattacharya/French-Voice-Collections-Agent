from agent.agent import Agent
from agent.presets_loader import load_preset
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--preset", required=True)
args = parser.parse_args()

preset = load_preset(args.preset)
agent = Agent(preset)

scripted_user = [
    "",
    "Oui, c’est moi.",
    "De quoi s’agit-il ?",
    "Vous êtes un robot ?",
    "D’accord."
]

print("=== DEMO CALL START ===\n")

for user in scripted_user:
    response = agent.respond(user)
    time.sleep(0.3)
    print(f"Agent: {response}\n")

print("=== DEMO CALL END ===")
