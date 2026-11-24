"""Write this bounty's one-line entry text to entry.txt.

Standard library only, no network. The text is written as UTF-8 bytes with no
trailing newline into $MAKEFUN_OUTPUT_DIR (or /output when unset), creating the
directory if needed, and the character count is printed to stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "On leave until the 14th. A wasp has built a nest in the mailbox and I respect her. All my mail is being held at the post office, and by the wasp."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = None
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            out_dir = Path(value)
            break
    if out_dir is None:
        out_dir = Path("/output")

    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
