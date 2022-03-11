import subprocess, os
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
        "{{cookiecutter.version}}",
        "-RequiredModules",
        "('Pester', 'PSScriptAnalyzer')"
    ]).communicate()

def remove_appveyor_files():
    file_names = [
        "AppVeyor.yml",
        "Invoke-AppveyorBuild.ps1"
    ]
    for file_name in file_names:
        os.remove(file_name)

def remove_azure_pipelines_files():
    file_names = [
        "{{cookiecutter.project_name}}.AzurePipelines.yml",
    ]
    for file_name in file_names:
        os.remove(file_name)


def main():
    generate_manifest()

    if "{{cookiecutter.ci_cd}}" == "AppVeyor":
        remove_azure_pipelines_files()
    if  "{{cookiecutter.ci_cd}}" == "Azure Pipelines":
        remove_appveyor_files()


if __name__ == "__main__":
    main()