#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
replace header and footer in html files
                             -------------------
begin                : 2015-07-08
copyright            : (C) 2015 by Bernhard Stroebl
email                : bernhard.stroebl@jena.de
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import codecs
import sys
import glob

def main():
    headerFN = "head.html"
    footerFN = "footer.html"

    try:
        headerFile = codecs.open(headerFN, 'r', "utf_8")
    except:
        print headerFN + " not found!"
        return None

    try:
        footerFile = codecs.open(footerFN, 'r', "utf_8")
    except:
        print footerFN + " not found!"
        return None

    header = headerFile.read()
    footer = footerFile.read()
    headerFile.close()
    footerFile.close()

    for aFN in glob.glob('*.html'):
        if aFN != headerFN and aFN != footerFN:
            inFile = codecs.open(aFN, 'r', "utf_8")
            outFile = codecs.open("deploy/" + aFN, "w", "utf_8")
            contents = inFile.read()
            inFile.close()
            contents = contents.replace("<!--#include file=\"head.html\" -->", header)
            contents = contents.replace("<!--#include file=\"footer.html\" -->", footer)
            outFile.write(contents)
            outFile.close()

if __name__ == "__main__":

    main()
