@echo off
setlocal enabledelayedexpansion

rem Get all Python files in the directory
for %%f in (*.py) do (
    if "%%f" neq "Analysis_Grp3.py" (
        echo Running %%f...
        python "%%f"
    )
)
