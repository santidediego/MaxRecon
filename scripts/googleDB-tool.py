#!/usr/bin/python
# -*- coding: utf8 -*-

# ################################################################################
# ## Redistributions of source code must retain the above copyright notice
# ## DATE: 2011-04-05
# ## AUTHOR: SecPoint ApS
# ## MAIL: info@secpoint.com
# ## SITE: http://www.secpoint.com
# ##
# ## LICENSE: BSD http://www.opensource.org/licenses/bsd-license.php
# ################################################################################
# ## 1.0 initial release

from optparse import OptionParser
import os.path
import urllib.parse

VERSION = '1.0'

def get_strings(src_file):
    """getting strings from file"""
    res = []
    try:
        res = open(src_file,'r').readlines()
        res = [x.strip() for x in res]
    except:
        res = []
    return res

def append_sitename(strs,site):
    """adding site name to strings"""
    strs = [x+' site:'+site for x in strs]
    return strs

def save_output(strs,out_f):
    """saving/printing results"""
    res = "\n".join(strs)

    if out_f:
        try:
            open(out_f,'w').write(res)
        except:
            print ("Error! Couldn't save output file!")
            exit()
    else:
        print (res)

def main():
    """Parsing options and starting engine"""
    parser = OptionParser(usage="%prog <sourcefile> [-s site] [-q] [-t] [-f outfile]",
              version="SecPoint.com %prog "+VERSION,
              epilog="SecPoint.com Google Penetration Testing Hack Database v. "+VERSION)
    parser.add_option("-o", "--output", dest="filename",
                      help="save output to file", metavar="FILE")
    parser.add_option("-s", "--site", dest="sitename",
                      help="generate queries for the SITE", metavar="SITE")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        exit()
        #parser.error("please set source file (could be found in 'db' dir)")
    #all options
    site_name = options.sitename
    out_file = options.filename
    db_dir = os.path.join(os.path.dirname(__file__),'db')
    source_file = os.path.join(db_dir,args[0])
    if not os.path.isfile(source_file):
        parser.error("could not find source file! Please check if it exists in 'db' dir")

    #starting!
    strs = get_strings(source_file)
    if not strs:
        print ("Can't get data from your source file!")
        exit()
    queries = []
    if site_name:
        strs = append_sitename(strs,site_name)

    save_output(strs,out_file)


if __name__ == "__main__":
    main()
