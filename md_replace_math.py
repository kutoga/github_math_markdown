from typing import Optional
import re
import os
import sys
import argparse
import hashlib
import pathlib
import urllib.request
from urllib.parse import quote

latex_math_regex = re.compile(r'\$(?P<math_expr>[^\$]*)\$')
image_type = 'svg'
base_url = 'http://latex.codecogs.com/{image_type}.download?%5Cinline%20%5Cdpi%7B120%7D%20%5Clarge%20{math_exp}'

def replace_latex_math_in_match(match, image_directory: Optional[str]) -> str:
    math_expr = match.groups('math_expr')[0]
    img_url = base_url.format(
        math_exp=quote(math_expr),
        image_type=quote(image_type))
    if image_directory is None:
        markdown_img = f'![mathematical expression]({img_url})'
    else:
        img = urllib.request.urlopen(img_url).read()
        m = hashlib.md5()
        m.update(img)
        img_file = os.path.join(image_directory, f'{m.hexdigest()}.{image_type}')
        with open(img_file, 'wb') as fh:
            fh.write(img)
        markdown_img = f'![mathematical expression]({img_file})'
    return markdown_img

def replace_latex_math(text: str, image_directory: Optional[str]) -> str:
    return latex_math_regex.sub(lambda match: replace_latex_math_in_match(match, image_directory), line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgdir', type=str, default=None, nargs='?', help='The (optional) output image directory.')
    args = parser.parse_args()
    image_directory = args.imgdir

    if image_directory is not None:
        pathlib.Path(image_directory).mkdir(parents=True, exist_ok=True)

    for line in sys.stdin:
        print(replace_latex_math(line, image_directory), end='')

