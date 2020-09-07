# photo-log

Python time lapse video creator

## Usage

Install and create virtual environment

```sh
python3 -m pip install --user virtualenv
python3 -m venv env
```

Use the virtual env

```sh
source env/bin/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```

Run the program

> See below sections

Leave virtual env

```sh
deactivate
```

### Clear images

Clear all the images in the `imgs` folder

```sh
python3 clear_images.py
```

Confirm the prompt

### Capture images

Capture images on a schedule

```sh
python3 capture_images.py
```

Confirm the schedule in the prompt
