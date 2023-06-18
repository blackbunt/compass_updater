@echo off

REM Bestimme den Pfad zum aktuellen Verzeichnis der Batch-Datei.
set "CURRENT_DIR=%~dp0"

REM Setze den Pfad zur main.py-Datei.
set "SCRIPT=%CURRENT_DIR%main.py"

REM Setze den Pfad zum logo.ico-Icon.
set "ICON=%CURRENT_DIR%logo.ico"

REM Aktiviere das virtuelle Umgebung.
call "%CURRENT_DIR%venv\Scripts\activate"


REM Installiere PyInstaller, wenn es noch nicht installiert ist.
pip install pyinstaller

REM Entferne den dist-Ordner, falls vorhanden.
if exist "%CURRENT_DIR%dist" (
    rmdir /s /q "%CURRENT_DIR%dist"
)

REM Entferne den build-Ordner, falls vorhanden.
if exist "%CURRENT_DIR%build" (
    rmdir /s /q "%CURRENT_DIR%build"
)

REM Erstelle die .exe-Datei mit PyInstaller.
pyinstaller --onefile --icon="%ICON%" "%SCRIPT%"

REM Überprüfe, ob die Erstellung erfolgreich war.
if exist "%CURRENT_DIR%dist\main.exe" (
    echo Die Compass_Update_Helper.exe wurde erfolgreich erstellt!

    REM Benenne die main.exe in Compass Update Helper.exe um.
    ren "%CURRENT_DIR%dist\main.exe" "Compass_Update_Helper.exe"
) else (
    echo Fehler: Die Compass_Update_Helper.exe konnte nicht erstellt werden.
)

REM Deaktiviere das virtuelle Umgebung.
deactivate

REM Kopiere die Compass Update Helper.exe in den Ordner der Batch-Datei.
copy "%CURRENT_DIR%dist\Compass_Update_Helper.exe" "%CURRENT_DIR%"

REM Entferne den dist-Ordner.
if exist "%CURRENT_DIR%dist" (
    rmdir /s /q "%CURRENT_DIR%dist"
)

REM Entferne den build-Ordner.
if exist "%CURRENT_DIR%build" (
    rmdir /s /q "%CURRENT_DIR%build"
)

REM Entferne die main.spec-Datei.
if exist "%CURRENT_DIR%main.spec" (
    del "%CURRENT_DIR%main.spec"
)


REM Halte das Konsolenfenster offen, um die Ausgabe zu sehen.
pause
