''' csv2deluxetable.py -- a script to convert a csv file to an AAS delux table

    Benjamin Rose
    benjamin.rose@me.com
    Universtiy of Notre Dame
    Python 3
    2016-06-17
    Licesed under the MIT License
'''
import numpy as np

# Read in csv file
data = np.array([['x', 'y', 'z'],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
        )


# determin number of columns
colNum = data.shape[1]


# ask for user changinging setting (tabletypesize, or more)


# make table meta
#double "{" for each single set requred for latex, cuase python format
#keep raw text to help with '\'
style = 'c'*colNum

tableMeta = r'''\begin{{deluxtable}}{{{}}}
\tablecolumns{{{}}}
\tabletypesize{{\small}}
\tablewidth{{0pt}}
%add in your table title and label
\tablecaption{{ \label{{tab:1}} }}
'''.format(style, colNum)

# make table head
header = ''
#todo(update for multiple header lines, look at design of `inside`)
for i in data[0]:
    header = header + '\colhdead{' + str(i) + '} & '
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
for i in data[1:]:
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