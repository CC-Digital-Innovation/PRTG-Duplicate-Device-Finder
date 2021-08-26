# PRTG-Duplicate-Device-Finder

## Summary
This script looks at devices in a PRTG instance and detects if a
device's name or IPv4 address appears more than once for a probe. It
then prints its results to the console.

_Note: If you have any questions or comments you can always use GitHub
discussions, or email me at farinaanthony96@gmail.com._

#### Why
Provides insight to inconsistencies in a PRTG instance so that they may be
exposed and corrected to maintain the cleanliness of the PRTG instance.

## Requirements
- Python >= 3.9.5
- configparser >= 5.0.2
- requests >= 2.25.1

## Usage
- Add any additional filtering logic to the API URLs to get specific
  devices if desired.
    - _Make sure you configure filtering options accordingly. Available
      options for filtering can be found on the PRTG API:
      https://www.paessler.com/manuals/prtg/live_multiple_object_property_status#advanced_filtering_

- Add additional device properties to make records include more information
  about a device.

- Edit the config.ini file with relevant PRTG access information.

- Simply run the script using Python:
  `python PRTG-Duplicate-Device-Finder.py`

## Compatibility
Should be able to run on any machine with a Python interpreter. This script
was only tested on a Windows machine running Python 3.9.5.

## Disclaimer
The code provided in this project is an open source example and should not
be treated as an officially supported product. Use at your own risk. If you
encounter any problems, please log an
[issue](https://github.com/CC-Digital-Innovation/PRTG-Duplicate-Device-Finder/issues).

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
-  version 1.0.0 - 2021/08/26
    - (initial release)

## Credits
Anthony Farina <<farinaanthony96@gmail.com>>

## License
MIT License

Copyright (c) [2021] [Anthony G. Farina]

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
