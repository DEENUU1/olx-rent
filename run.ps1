$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location -Path $scriptDirectory

$venvPath = ".venv\Scripts\Activate"
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..."
    & $venvPath
} else {
    Write-Host "Virtual environment not found."
    exit 1
}

$pythonScript = "main.py"
if (Test-Path $pythonScript) {
    Write-Host "Running Python script..."
    try {
        python $pythonScript
    } catch {
        Write-Host "An error occurred. Press any key to exit..."
        $null = $host.UI.RawUI.ReadKey("NoEcho,IncludeNewLine")
    }
} else {
    Write-Host "Python script 'main.py' not found."
    exit 1
}