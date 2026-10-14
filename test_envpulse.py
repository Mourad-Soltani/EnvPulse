"""
Health tests for EnvPulse.
Built by Mourad.Soltani
"""

import json
import tempfile
from pathlib import Path
import subprocess
import sys

# Signature: Mourad.Soltani

def run(cmd):
    result = subprocess.run(
        [sys.executable, "envpulse.py"] + cmd,
        capture_output=True, text=True, cwd=Path(__file__).parent
    )
    return result.returncode, result.stdout, result.stderr

def test_scan_clean():
    with tempfile.TemporaryDirectory() as tmp:
        env = Path(tmp) / ".env"
        env.write_text("NODE_ENV=development\nPORT=3000\n")
        code, out, _ = run(["scan", "--path", tmp])
        assert code == 0
        assert "No secrets" in out

def test_scan_secret():
    with tempfile.TemporaryDirectory() as tmp:
        env = Path(tmp) / ".env"
        env.write_text("AWS_KEY=AKIAIOSFODNN7EXAMPLE\n")
        code, out, _ = run(["scan", "--path", tmp])
        assert code == 1
        assert "AWS Access Key" in out

def test_diff_missing():
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / ".env.example").write_text("DATABASE_URL=\nSECRET=\n")
        (Path(tmp) / ".env").write_text("DATABASE_URL=postgres://\n")
        code, out, _ = run(["diff", "--env", str(Path(tmp)/".env"), "--example", str(Path(tmp)/".env.example")])
        assert code == 1
        assert "SECRET" in out

def test_generate():
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / ".env").write_text("FOO=bar\nBAZ=qux\n")
        code, out, _ = run(["generate", "--env", str(Path(tmp)/".env"), "--out", str(Path(tmp)/".env.example")])
        assert code == 0
        content = (Path(tmp) / ".env.example").read_text()
        assert "FOO=" in content
        assert "bar" not in content
        assert "Mourad.Soltani" in content

if __name__ == "__main__":
    test_scan_clean()
    test_scan_secret()
    test_diff_missing()
    test_generate()
    print("All health tests passed.")
