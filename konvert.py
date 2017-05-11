from PIL import Image
import os
import shutil
from pyunpack import Archive
from random import choice
from string import ascii_letters

dir_files = "./media/"
old_dir_file = "./media/old_files/"



def rename_all_file(list_files, dir_files):
    for infile in list_files:
        if infile != 'old_files':
            new_name = ''.join(choice(ascii_letters) for i in range(15))
            os.rename(dir_files+infile, dir_files+new_name+infile[-4:])
            print(dir_files+new_name+infile[-4:])


def unarchive(list_files, dir_files, old_file):
    for infile in list_files:
        if infile[-3:] == "rar" or infile[-3:] == "zip":
            archive = Archive(dir_files+infile)
            archive.extractall(dir_files)
            print("move archive: {}".format(infile))
            shutil.move(dir_files + infile, old_file + infile)

def conver_to_jpg(list_image, dir_files):
    list_new = []
    for infile in list_image:
        print("curren file : {}".format(infile))
        if infile[-3:] == "tif" or infile[-3:] == 'png':
            print(infile)
            outfile = infile[:-3] + 'jpg'
            im = Image.open(dir_files + infile)
            print("convert file: {}".format(outfile))
            list_new.append(outfile)
            out = im.convert("RGB")
            out.save(dir_files+outfile, "JPEG", quality=90)
            print("move file : {}".format(old_dir_file+infile))
            shutil.move(dir_files+infile, old_dir_file+infile)
        if infile[-3:] == 'jpg':
            list_new.append(infile)
    if list_new == []:
        print("no file")
    return list_new

def image_compres(list_image, size, dir_files):
    for infile in list_image:
        file, ext = os.path.splitext(infile)
        im = Image.open(dir_files+infile)
        im.thumbnail(size)
        new_dir_file = dir_files+file+'210x297'+infile[-4:]
        print("compress file : {}".format(new_dir_file))
        im.save(new_dir_file, "JPEG")
        os.remove(dir_files+infile)
        print("remove file : {}".format(dir_files+infile))





unarchive(os.listdir(dir_files), dir_files, old_dir_file)
rename_all_file(os.listdir(dir_files), dir_files)
size = 210, 297
list_file = os.listdir(dir_files)
image_compres(conver_to_jpg(list_file, dir_files), size, dir_files)