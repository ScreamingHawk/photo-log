# photo-log

Python time lapse video creator

## Usage

Install and create virtual environment

```sh
python3 -m pip install --user virtualenv
python3 -m venv env
```

```ps1
py -m pip install virtualenv
py -m venv env
```

Use the virtual env

```sh
source env/bin/activate
```

```ps1
env/Scripts/activate.bat
```

Install dependencies

```sh
pip install -r requirements.txt
```

```ps1
py -m pip install -r requirements.txt
```

Run the program

> See below sections

Leave virtual env

```sh
deactivate
```

```ps1
deactivate
```

### Clear images

Clear all the images in the `imgs` folder

```sh
python3 clear_images.py
```

```ps1
py clear_images.py
```

Confirm the prompt

### Capture images

Capture images on a schedule

```sh
python3 capture_images.py
```

```ps1
py capture_images.py
```

Confirm the schedule in the prompt
