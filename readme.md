# csv2deluxetable

This [Python 3](https://www.python.org) script converts a `csv` file into an [AAS style `deluxetable`](http://journals.aas.org/authors/aastex/aasguide.html#deluxetable). 

## Dependancies

[![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/)

This uses some parts of the standard library as well as `numpy` and `astropy`. But if you are an astronomer and like to use the computer, this should not be a problem.

## Using script

Please place this script in your [`PATH`](https://kb.iu.edu/d/acar) and make it [executable](http://askubuntu.com/questions/484718/how-to-make-a-file-executable).

`$ chmod +x csv2deluxetable.py`

Once you make this file executable you can easily run it either with 

`csv2deluxetable data.csv`

to send the resulting table to standard out. Or by

`csv2deluxetable data.csv -o data.tex`

to specify the output file. This repository comes with a `csv` file that you can use for testing purposes.

## CVS format

More details of the format of the csv to come.

## Deluxtable settings

Currently you can not change the settings of the deluxtable with the script.

## Contributing

I need to set a standard for this. I'll likely copy Astropy's. 

I am also doing to take on the [Astropy Code of Conduct](http://www.astropy.org/about.html#codeofconduct) for contributing to this repository. 

