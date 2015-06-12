from distutils.core import setup, Extension
import os, glob,shutil


def installation():
    setup(
        name="FloorplanMaker",
        version="1.0",
        author="Pawel Weber",
        author_email="pawelweber@yahoo.pl",
        description="GUI app supporting creation of emulation files",
        platforms=["Linux"],
        packages=['FloorplanMaker', 'xmldoc', 'fmWidgets'],
        package_dir={'FloorplanMaker': 'src',
                     'xmldoc': 'src/xmldoc', 'fmWidgets': 'src/fmWidgets'},
        scripts=['scripts/FloorplanMaker'],
        package_data={'FloorplanMaker': ['src/images/*', 'images/*']}
    )

    dir_icons = "/usr/local/include/.icons"
    dir_fm = "/usr/local/include/.icons/FloorplanMaker"
    src_icons = "src/images/"

    try:
        print dir_icons
        os.mkdir(dir_icons)
        print("lol")
    except:
        os.stat(dir_icons)

    try:
        os.mkdir(dir_fm)
    except:
        os.stat(dir_fm)

    files = glob.iglob(os.path.join(os.getcwd()+"/"+src_icons, "*.png"))
    try:
        os.mkdir('/usr/local/include/.icons')
    except OSError:
        try:
            os.mkdir(dir_fm)
        except:
            pass

    for file in files:
        print file
        if os.path.isfile(file):
            shutil.copy2(file, dir_fm)

    for r,d,f in os.walk(dir_icons):
        os.chmod(r, 0755)

if __name__ == "__main__":
    installation()

