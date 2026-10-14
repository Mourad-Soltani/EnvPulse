# EnvPulse

Minimal zero-dependency CLI to scan .env files for secrets and validate against .env.example.

Built by Mourad.Soltani

## Features

- Secret pattern detection (AWS, GitHub, OpenAI, Stripe, generic API keys, private keys)
- Compare .env vs .env.example for missing/extra keys
- Generate redacted .env.example from current .env
- JSON output for CI
- Zero external dependencies (Python 3.8+ stdlib only)

## Quick Start

```bash
python envpulse.py scan
python envpulse.py diff
python envpulse.py generate
```

## Requirements

- Python 3.8+
- No pip packages needed

## Buyer Notes

You get a single-file CLI (`envpulse.py`) + tests + README + MIT license.

How to run: `python envpulse.py --help`

Drop into any repo, add as pre-commit or CI step.

Signature: Mourad.Soltani
