import os
import sys
from builtins import any as b_any

"""
FIRST FILE OF PIPELINE
(Following multi-zip download from PPMI / other source into dir JustDownloaded/)

Combines multiple zip files into a single directory.
Before running: navigate to external HD (or location of files) in terminal via
    `cd /Volumes/<name of HD>`
To run (requires argument):
    `python neuro_format.py <name_of_destination_directory>`

Next file to run will be   `make_bids.py`
"""

def move_files(destdir,maindir):
    print(f"Moving files from {maindir} and consolidating into {destdir}\n")
    if not os.path.exists(destdir):
        os.mkdir(destdir)

    fileroots = list([os.path.join(root,filename) for root,dirnames,filenames \
                        in os.walk(maindir) if len(root.split('/'))==7 \
                        for filename in filenames])
    for filepath in fileroots:
        filedest = list([rootd for rootd,dirnamesd,filenamesd \
                        in os.walk(destination)])
        for step in range(3,len(filepath.split('/')[:-1])):
            if not b_any('/'.join(filepath.split('/')[3:step+1]).upper()==\
                        '/'.join(dest.split('/')[2:step]).upper() \
                        for dest in filedest if len(dest.split('/'))>=step):
                os.mkdir(os.path.join(destination,\
                        '/'.join(filepath.split('/')[3:step+1])))
        os.rename(filepath, destination+'/'.join(filepath.split('/')[3:]))
    print(f'... empyting {maindir} ...\n')
    while len(os.listdir(maindir)) > 2:
        for root, dirnames, filenames in os.walk(main_dir):
            if os.path.isfile(os.path.join(root,'.DS_Store')):
                os.remove(os.path.join(root,'.DS_Store'))
            if os.path.isdir(root):
                if not os.listdir(root):
                    os.rmdir(root)
    print(f"All files moved from {maindir} and consolidated into {destdir}\n\n")
    return

if __name__=='__main__':

    destination = './'+sys.argv[1]+'/' # path to destination folder

    main_dir = "./JustDownloaded/"

    move_files(destination,main_dir)
