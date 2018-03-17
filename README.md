# a-tempo

Set the correct "DateTimeOriginal" in EXIF ​​to downloaded Narrative Clip photos.

- [Requirements](#requirements)
- [How to Setup](#how-to-setup)
- [Usage](#usage)
- [Misc.](#misc)
    - [Special thanks](#special-thanks)

## Requirements

* Python 3
* [piexif](https://github.com/hMatoba/Piexif)
* tqdm

## How to Setup

```
$ pip install -r requirements.txt --upgrade
```

## Usage

```
$ python3 atempo.py -h
usage: a-tempo [-h] [-d D] [-td TD] [-v]

Set the correct 'DateTimeOriginal' in EXIF ​​to downloaded Narrative Clip photos.

optional arguments:
  -h, --help     show this help message and exit
  -d D           Set target directory. (default='.')
  -td TD         Time Differences [hours] from UTC. (default=9.0)
  -v, --verbose  Increse output verbosity.

Produced by Shin'ichiro SUZUKI <shin@sforzando.co.jp>
```

## Misc.

### Special thanks

* [hMatoba](https://github.com/hMatoba/Piexif).
