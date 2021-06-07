@echo off
@REM https://stackoverflow.com/questions/1794547/how-can-i-make-an-are-you-sure-prompt-in-a-windows-batchfile

setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure you want to delete the database (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

echo Deleting database
python python\setup_database.py delete

:END
endlocal
