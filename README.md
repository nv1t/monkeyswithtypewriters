monkeyswithtypewriter
=====================
A utility for auto typing information into another window. 
No monkeys were harmed in making this tool

* be installed in venv
* be installed using `setup.py`
* be runned directly from source directory if environment dependencies already satisfied

## Installation

### Method 1. System-wide install

Run in project directory:

```bash
python3 -m pip install .
```

Package scripts shall be available in standard executable locations upon completion.

### Method 2. Running from project directory

Installing dependencies:


```bash
python3 -m pip install -r requirements.txt
```

Now script can be run right from source directory.

#### Userland pip

Both previous methods can be run with `--user` option of `pip` installer. In this case superuser privileges are not required and package shall be installed to user home directory. So, for first method script executabled will appear in `~/.local/bin`.

#### Tipp: Install from Github

You can install this as well in any virtualenv by using the git+https wrapper from pip
```bash
python -m pip install git+https://github.com/nv1t/monkeyswithtypewriters
```

## Known Bugs
* It doesn't detect if the IDE you are trying to autotype in is doing some fancy auto completion...it will completly break