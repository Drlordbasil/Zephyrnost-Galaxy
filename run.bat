Sure, here's the code for the run.bat file:

```
@echo off

REM Run pip install command to install dependencies
pip install -r requirements.txt

REM Run main.py
python main.py

REM Pause the script to keep the command window open
pause
```

Make sure to place this run.bat file in the same directory as main.py and requirements.txt. When the user double-clicks on the run.bat file, it will install the required dependencies from the requirements.txt file and then run the main.py file. The `pause` command is included to keep the command window open after the execution is complete.