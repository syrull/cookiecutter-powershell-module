import subprocess, sys, os
from pathlib import Path


def generate_manifest():
    path = Path.cwd() / "src" / "{{cookiecutter.project_name}}.psd1"
    subprocess.Popen([
        "powershell.exe",
        "New-ModuleManifest", 
        "-Path",
        f"'{path}'",
        "-Author",
        "'{{cookiecutter.author}}'",
        "-CompanyName",
        "'{{cookiecutter.company_name}}'",
        "-ModuleVersion",
        "{{cookiecutter.version}}"
    ]).communicate()

def main():
    generate_manifest()


if __name__ == "__main__":
    main()