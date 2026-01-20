def generate_report(results):
    total = len(results)
    success = sum(1 for r in results if r["success"])
    return f"""# Pre-flight Test Report

Total scenarios: {total}
Success rate: {success / total:.0%}

## Failures
{[r for r in results if not r["success"]]}

## Latency (in ms)
{[r["latency_ms"] for r in results]}
"""
