#!/usr/bin/env python3
from pathlib import Path
import sys

# Ensure we can import constants.py regardless of where we run from
sys.path.insert(0, str(Path(__file__).parent))

import constants as c
def main():
    # Print lines in KEY=VALUE format
    print(f"HIDDEN_PDF={c.HIDDEN_PDF}")

    print(f"GIT_AUTHOR_NAME={c.GIT_USER_NAME}")
    print(f"GIT_AUTHOR_EMAIL={c.GIT_USER_EMAIL}")
    print(f"GIT_DEST_REPO={c.GIT_DEST_REPO}")

if __name__ == "__main__":
    main()
