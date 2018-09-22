#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint
import sys
sys.path.append('./lib')
import piexif
from tqdm import tqdm


def main(args):
    print(args)
    path = Path(args.d)
    for f in tqdm(list(path.rglob("[0-9_]*.jpg"))):
        print(f)
        target_dt = datetime.strptime(f.name + "+0000", "%Y%m%d_%H%M%S_000.jpg%z")
        target_dt = target_dt + timedelta(hours=float(args.td))
        try:
            exif_original = piexif.load(f.as_posix())
        except piexif.InvalidImageDataError as iide:
            sys.stderr.write("{}".format(iide))
            continue
        if args.verbose:
            pprint(exif_original)
        exif_original["Exif"][piexif.ExifIFD.DateTimeOriginal] = target_dt.strftime("%Y:%m:%d %H:%M:%S")
        exif_bytes = piexif.dump(exif_original)
        piexif.insert(exif_bytes, f.as_posix())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="a-tempo",
        description="Set the correct 'DateTimeOriginal' ​​to downloaded Narrative Clip photos.",
        epilog="Produced by Shin'ichiro SUZUKI <shin@sforzando.co.jp>",
        add_help=True
    )
    parser.add_argument("-d",
                        help="Set target directory. (default='.')",
                        default="./")
    parser.add_argument("-td",
                        help="Time Differences [hours] from UTC. (default=9.0)",
                        default=9.0)
    parser.add_argument("-v", "--verbose",
                        help="Increse output verbosity.",
                        action="store_true")
    main(parser.parse_args())
