#!/usr/bin/env python3
import argparse
import shutil
import subprocess
from pathlib import Path

from constants import BUILD_DIR, PDF, HIDDEN_PDF


def run(cmd, cwd=None):
    print(">>", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def build_variant(tex_path: Path, out_dir: Path, hide: bool, output_pdf: Path, jobname: str):
    out_dir.mkdir(parents=True, exist_ok=True)

    tex_arg = rf"\def\HIDE{{{'true' if hide else 'false'}}}\input{{{tex_path.as_posix()}}}"

    cmd = [
        "pdflatex",
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        f"-output-directory={out_dir.as_posix()}",
        f"-jobname={jobname}",
        tex_arg,
    ]
    run(cmd)

    built_pdf = out_dir / f"{jobname}.pdf"
    shutil.copyfile(built_pdf, output_pdf)
    print(f"Copied -> {output_pdf}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tex", help="Path to main .tex file")
    args = p.parse_args()

    tex_path = Path(args.tex).resolve()

    build_variant(
        tex_path=tex_path,
        out_dir=BUILD_DIR,
        hide=False,
        output_pdf=PDF,
        jobname=f"resume_{tex_path.stem}_public",
    )

    build_variant(
        tex_path=tex_path,
        out_dir=BUILD_DIR,
        hide=True,
        output_pdf=HIDDEN_PDF,
        jobname=f"resume_{tex_path.stem}_hidden",
    )


if __name__ == "__main__":
    main()
