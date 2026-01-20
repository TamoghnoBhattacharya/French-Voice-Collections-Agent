# French Voice Collections Agent

A minimal, brand-safe French collections voice agent with:
- Configurable client presets
- Automatic pre-flight self-test harness
- End-to-end demo call simulation

## Requirements
- Python 3.10+

## Install
pip install -r requirements.txt

## Run demo (end-to-end call)
python demo/run_demo.py --preset presets/amazon.json

## Run automatic self-tests
python tests/runner.py --preset presets/amazon.json

## Change client tone
Edit any file in `presets/` and re-run the demo or tests.

## Notes
- French only on the call path
- No real personal data used
- Deterministic logic for reliability

## Design note: LLM usage

The agent is intentionally deterministic by default for safety and
testability. A narrow LLM adapter can be enabled for controlled
rephrasing of pre-approved French messages, without allowing the model
to make policy or payment decisions.

This mirrors production patterns in regulated collections workflows.

