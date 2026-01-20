import yaml
import time
from agent.agent import Agent
from agent.presets_loader import load_preset
from tests.report import generate_report
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--preset", required=True)
args = parser.parse_args()

preset = load_preset(args.preset)

with open("tests/scenarios.yaml", "r", encoding="utf-8") as f:
    scenarios = yaml.safe_load(f)

results = []

for scenario in scenarios:
    agent = Agent(preset)
    success = True
    start = time.time()

    last_response = ""
    for turn in scenario["turns"]:
        last_response = agent.respond(turn)

    if "expect_contains" in scenario:
        if scenario["expect_contains"] not in last_response:
            success = False

    elapsed = time.time() - start
    results.append(
        {
            "scenario": scenario["name"],
            "success": success,
            "latency_ms": int(elapsed * 1000),
        }
    )

report = generate_report(results)
print(report)
