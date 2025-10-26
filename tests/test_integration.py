import subprocess
import sys

def test_main_prints_hello_world():
    result = subprocess.run(
        [sys.executable, "-m", "hello.app"],
        capture_output=True,
        text=True,
        check=True
    )
    # main() prints a single line
    assert result.stdout.strip() == "Hello, World!"
    assert result.returncode == 0
