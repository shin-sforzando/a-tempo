# a-tempo

![a-tempo](https://user-images.githubusercontent.com/32637762/37560311-37fb6f02-2a79-11e8-8d19-401cdcc4f0df.png)

Set the correct "DateTimeOriginal" ​​to downloaded Narrative Clip photos.

Google Photos is looking at EXIF of images, but images downloaded from Narrative Clip are missing EXIF.
In particular, if "DataTimeOriginal" does not exist, all images are taken on the day of uploading.
This program gives the local shooting date and time as EXIF using the file name of the image.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

- [Requirements](#requirements)
- [How to Setup](#how-to-setup)
- [Usage](#usage)
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

## Special thanks

* [hMatoba/Piexif](https://github.com/hMatoba/Piexif).
