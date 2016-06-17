''' csv2deluxetable.py -- a script to convert a csv file to an AAS delux table

    Benjamin Rose
    benjamin.rose@me.com
    Universtiy of Notre Dame
    Python 3
    2016-06-17
    Licesed under the MIT License
'''
import numpy as np
from astropy.table import Table


#### Read in csv file ####
#todo(test with complex and simple csv files)

#title is that last line, a footer comment
#first comment line is main header columns
#other comment lines will be added as secondary headers, like units
t = Table.read('data.csv', format='ascii')
colhead = t.colnames
title = t.meta['comments'][-1]
units = t.meta['comments'][:-1][0]
units = units.split(', ')    #add space here to remove it from the array
data = np.array(t)
# determin number of columns
colNum = len(t.colnames)


#### ask for user changinging setting (tabletypesize, or more) ####


#### make table meta ####
#double "{" for each single set requred for latex, cuase python format
#keep raw text to help with '\'
style = 'c'*colNum

tableMeta = r'''\begin{{deluxtable}}{{{}}}
\tablecolumns{{{}}}
\tabletypesize{{\small}}
\tablewidth{{0pt}}
%add in your table title and label
\tablecaption{{{} \label{{tab:1}} }}
'''.format(style, colNum, title)


#### make table head ####
header = ''
#itterate over colhead
for i in colhead:
    header = header + '\colhdead{' + str(i) + '} & '
# remove last '&' and add a new line at the end of a row
header = header[:-2] + r' \\ ' +'\n'
#iterate over units
#todo(what if units has multiple columns)
header += '    '     #tab in units line
for i in units:
    header += '\colhdead{' + str(i) + '} & '
# remove last '&' and add a new line at the end of a row
header = header[:-2] + r' \\ ' +'\n'

# remove last newline at the end of the header
header = header[:-1]

tableHead = r'''\tablehead{{
    {}
}}
'''.format(header)

# make data block
#todo(add in handleing for \nodata)

inside = ''
# for i in data[1:]:
for i in data:
    for j in i:
        inside = inside + str(j)
        inside += ' & '
    # remove last '&' and add a new line at the end of a row
    inside = inside[:-2] + r'\\ ' +'\n'
# remove last newline at the end of the inside
inside = inside[:-1]
tableData = r'''
\startdata
{}
\enddata
'''.format(inside)

# make table footer
tableFooter = r'''
%add \tablenotetext{a}{} to connect to \tablenotemark{a}

\end{deluxetable}
'''

# add in endnotes

# save file
table = tableMeta+tableHead+tableData+tableFooter
print table
"""
table = r'''\begin{deluxetable}{ccc|ccc|c}
\tablecolumns{7}
\tabletypesize{\small}
\tablewidth{0pt}
\tablecaption{Summary of \sn{} and their host galaxies. \label{tab:data}} %really a title
\tablehead{
    \colhead{SDSS SN ID} & \colhead{x} & \colhead{y} & \colhead{a}\tablenotemark{a} & \colhead{b}\tablenotemark{a}  & \colhead{theta} & \colhead{cut}\tablenotemark{b} \\
    \colhead{} & \colhead{} & \colhead{} & \colhead{} & \colhead{}  & \colhead{(radians)} & \colhead{}
    }
    
\startdata
SN6491  & x & y & a & b & theta & o \\
SN13038 & x & y & a & b & theta & lsb \\
\enddata

\tablenotetext{a}{Something about Source Extactor's scalling.}
\tablenotetext{b}{o - extra object in field of view, lsb - the host was not detected with HST because it was a low surface brightness}
\end{deluxetable}'''
"""