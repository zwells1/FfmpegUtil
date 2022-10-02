import sys
import os
import subprocess
from GrabSource import *


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def getFileNames(mergeSource):
    #ffmpeg needs this written to a text file

    listOfFiles = os.listdir(mergeSource)

    with open('ToMerge/FileList.txt', 'w+') as fp:
        for each in listOfFiles:
            fileAndPath = str(mergeSource + each)
            fp.write("file '%s'\n" % fileAndPath)
            print(fileAndPath)



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    TitleScreen.TerminalScreen(os.path.basename(__file__))

    getFileNames("ToMerge/")


    cmd = [
            "../FfmpegWindowsBuild/bin/ffmpeg.exe -f concat -safe 0 -i ToMerge/FileList.txt ",
            " -c copy Output/output.mp4"]

    cmd = ''.join([str(elem) for i,elem in enumerate(cmd)])

    print(cmd)
    #subprocess.run(cmd, shell=True)

    #cleanup, remove FileList
    os.remove("ToMerge/FileList.txt")


if __name__ == "__main__":
    main(sys.argv[1:])

