from pathlib import Path

# PDF Paths
PDF = Path("resume.pdf")
HIDDEN_PDF = Path("resume_hidden_info.pdf") # These PDF Paths should not be named the same thing


# Git identity for CI commits
GIT_USER_NAME  = "[username]"
GIT_USER_EMAIL = "[username]@users.noreply.github.com"
GIT_DEST_REPO = "[username]/[repo_name]"

# Don't edit this
BUILD_DIR = Path("build")
