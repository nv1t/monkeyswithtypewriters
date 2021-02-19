monkeyswithtypewriter
=====================
A utility for auto typing information into another window. 
No monkeys were harmed in making this tool

* be installed in venv
* be installed using `setup.py`
* be runned directly from source directory if environment dependencies already satisfied

## Table of Contents
  * [Installation](#installation)
    + [Method 1. System-wide install](#method-1-system-wide-install)
    + [Method 2. Running from project directory](#method-2-running-from-project-directory)
      - [Userland pip](#userland-pip)
      - [Tipp: Install from Github](#tipp--install-from-github)
  * [Basic Usage](#basic-usage)
  * [Known Bugs](#known-bugs)

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

## Basic Usage

```plain
-> % monkeyswithtypewriters -h
usage: monkeyswithtypewriters [-h] [-t TIME] [-H] {file,string} payload

                        .="=.                .="=.
                      _/.-.-.\_     _      _/.-.-.\_     _
                     ( ( o o ) )    ))    ( ( o o ) )    ))
                      |/  "  \|    //      |/  "  \|    //
      .-------.        \'---'/    //        \'---'/    //
     _|~~ ~~  |_       /`"""`\\  ((         /`"""`\\  ((
   =(_|_______|_)=    / /_,_\ \\  \\       / /_,_\ \\  \\
     |:::::::::|      \_\\_'__/ \  ))      \_\\_'__/ \  ))
     |:::::::[]|       /`  /`~\  |//        /`  /`~\  |//
     |o=======.|      /   /    \  /        /   /    \  /
     `"""""""""`  ,--`,--'\/\    /     ,--`,--'\/\    /
                   '-- "--'  '--'       '-- "--'  '--' 

positional arguments:
  {file,string}         do you want to output a string, or read a file
  payload               String or Filepath

optional arguments:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  Seconds to Wait until start typing
  -H, --human           Slows down the output to 1 char per 300ms
  ```

  It should be pretty self explanatory :) 
  The only weired feature is `-H` or `--human` with delays the output and types 1 character every 300ms (roughly). It tries to randomize the delay a little bit.


## Known Bugs
* It doesn't detect if the IDE you are trying to autotype in is doing some fancy auto completion...it will completly break