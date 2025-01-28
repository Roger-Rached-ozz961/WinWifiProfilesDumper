@echo off
:: Set the console window title and background color
title Wi-Fi Profile Manager
color 0A

:: Function to display a banner with colorful text
:banner
cls
echo.
echo ==================================================
echo        Wi-Fi Profile Manager
echo ==================================================
echo.
echo 1. Specific Wi-Fi Password Retrieval.
echo 2. All Saved Wi-Fi Profiles Dumper.
echo 3. Credits/Author
echo 4. Exit
echo.
goto menu

:: Menu options
:menu
:: Show the menu
cls
echo ==================================================
echo            Welcome to WinWifiProfilesDumper
echo                    Main Menu
echo               Choose An Option.
echo        Kindly Note: if you choose option 2 to dump everything,
echo        check your results folder to see the dump.
echo ==================================================
echo.
echo 1. Specific Wi-Fi Password Retrieval.
echo 2. All Saved Wi-Fi Profiles Dumper.
echo 3. Credits/Author
echo 4. Exit
echo.
set /p option=Choose an option (1-4): 

if "%option%"=="1" goto option1
if "%option%"=="2" goto option2
if "%option%"=="3" goto credits
if "%option%"=="4" goto exit

echo Invalid choice, please choose again.
pause
goto menu

:: Option 1: Get password for a specific Wi-Fi
:option1
cls
:: Activate the virtual environment and then run opt1.py from the "scripts" folder using PowerShell
call venv\Scripts\activate
start powershell -NoExit -Command "python scripts\opt1.py"

:: After the script runs, the batch file will wait for the user to close the new PowerShell window.
:: Once closed, it will return to the main menu.
goto menu

:: Option 2: Dump all Wi-Fi profiles
:option2
cls
echo Dumping all Wi-Fi profiles and passwords...
echo You can check the results in the "results" folder.

:: Activate the virtual environment and then run opt2.py from the "scripts" folder using PowerShell
call venv\Scripts\activate
start powershell -NoExit -Command "python scripts\opt2.py"

:: After the script runs, it will return to the menu
goto menu

:: Option 3: Credits/Author
:credits
cls
echo ==================================================
echo              Author: Ozz961
echo       Saved Wi-Fi Profiles Dumper.
echo    Github Repo: https://github.com/Roger-Rached-ozz961/WinWifiProfilesDumper
echo ==================================================
echo.
echo Thanks for using this script, use it at your ease!
echo.
pause
goto menu

:: Exit Option
:exit
cls
echo Exiting gracefully...
exit
