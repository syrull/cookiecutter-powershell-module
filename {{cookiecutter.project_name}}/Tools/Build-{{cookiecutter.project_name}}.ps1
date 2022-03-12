[CmdletBinding()]
param (
    [ValidateSet("CurrentUser", "AllUsers")]
    [string]
    $Scope = "CurrentUser",

    [Parameter(Mandatory = $false )]
    [string]
    $MinNugetVersion = "2.8.5.201"
)

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Initializing the requirements
. $PSScriptRoot\Build.requirements.ps1

$Modules = Get-Module -ListAvailable

if ( -not (Get-PackageProvider -Name "NuGet") ) 
{
    Install-PackageProvider -Name NuGet -MinimumVersion $MinNugetVersion -Force -Scope $Scope
}

foreach ($Module in $RequiredModules)
{
    if ( -not (Get-Module -ListAvailable -Name $Module.ModuleName))
    {
        Install-Module -Name $Module.ModuleName -Scope $Scope -RequiredVersion $Module.RequiredVersion -Force -SkipPublisherCheck 
    }
}

Invoke-ScriptAnalyzer -Path $PSScriptRoot\..\src\ -Recurse