# photo-log

Python time lapse video creator

## Usage

#### Install and create virtual environment

Linux:
```sh
python3 -m pip install --user virtualenv
python3 -m venv env
```

Windows:
```ps1
py -m pip install virtualenv
py -m venv env
```

#### Use the virtual env

Linux:
```sh
source env/bin/activate
```

Windows:
```ps1
env/Scripts/activate.bat
```

#### Install dependencies

Linux:
```sh
pip install -r requirements.txt
```

Windows:
```ps1
py -m pip install -r requirements.txt
```

#### Run the program

> See below sections

#### Leave virtual env

Linux:
```sh
deactivate
```

Windows:
```ps1
deactivate
```

### Clear images

#### Clear all the images in the `imgs` folder

Linux:
```sh
python3 clear_images.py
```

Windows:
```ps1
py clear_images.py
```

Confirm the prompt

### Capture images

#### Capture images on a schedule

Linux:
```sh
python3 capture_images.py
```

Windows:
```ps1
py capture_images.py
```

Confirm the schedule in the prompt
