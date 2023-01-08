# Toaster

## Overview

Reminder for Windows

## Requirements

- Python 3.7.0 (I haven't tried it, but it probably works in all versions.)
- Redis-server

## Usage

1. Download "Toaster" via git. Only the toaster directory and the `exec_toaster.bat` file are needed; other files and directories can be deleted.

```bash
  git clone git@github.com:YutoUrushima/toaster.git
```

2. Install redis and plyer modules with pip.

```bash
  pip install redis plyer
```

3. Place the `exec_toaster.bat` file in the startup directory. This way, you don't have to call the "call" process yourself in `python call.py` each time you start up windows.

```bash
  python call.py
```

4. Call `main.py` to register toaster.

```bash
  python main.py
```

5. If the toaster registration is successful, a toast notification appears at the set time.
![スクリーンショット_20221222_201528](https://user-images.githubusercontent.com/56684832/211191421-ee8b3229-36d3-478b-81e5-97c5ecbb5409.png)

## Note

- exec_toaster.bat describes to call `call.py` like `python %homepath%\works\call.py`, so rewrite this path accordingly.
- The Redis server configuration is written in `setting.json`, so rewrite this if you want to change it.
- Windows seems to ignore the time set in "time for the toast to stay alive", so adjust the time in the settings.<br/>
   Reference: https://github.com/kivy/plyer/issues/503
