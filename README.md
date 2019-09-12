# poTranslate
This script translates the different texts of a .po file into the language that the user wants.

## Requirements
 - Python 3
## Installations
```sh
   $ pip install polib
   $ pip install googletrans
```
#### *Parameters*
  - p - Input File with extension .po
  - i - The language to translate the source text into. The value should be one of the language codes listed in [googletrans.LANGUAGES](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages).
  - v - Software version.
  - h - Print this help.

#### *Examples*
  ```sh
   $ python3 poTranslate.py -i es -p /PATH/FILE.po
  ```
  
 ## Author
Brandon Madriz(b.madriz@cgiar.org / bmadriz@mrbotcr.com)
