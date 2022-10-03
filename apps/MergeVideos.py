import sys
import os
import subprocess
from GrabSource import *
from GrabSubmodules import *

#globals are generally bad....
gFfmpegListFile = "ToMerge/FileList.txt"

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def cleanUpFile(pathToFile):

    isExists = os.path.exists(pathToFile)
    if isExists:
        os.remove(pathToFile)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def makeFileNamesInTextFile(mergeSource):
    #ffmpeg needs this written to a text file
    global gFfmpegListFile

    #removing a weird bug where it will try to check the FileLists.txt
    #file if a user crashes out before previous run cleanus up the file
    cleanUpFile(gFfmpegListFile)

    listOfFiles = os.listdir(mergeSource)

    with open(gFfmpegListFile, 'w+') as fp:
        for each in listOfFiles:
            fileAndPath = str(mergeSource + each)
            fp.write("file '%s'\n" % each)
            print(fileAndPath)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):
    global gFfmpegListFile

    print(os.name)

    TitleScreen.TerminalScreen(os.path.basename(__file__))

    #first time make sure input and output directories exist.
    paths = ["ToMerge/", "Output"]
    for eachPath in paths:
        isExist = os.path.exists(eachPath)
        if not isExist:
            os.makedirs(eachPath)

    makeFileNamesInTextFile("ToMerge/")
    #changes the depth depending on the environment
    ffmpegPathDepth = None

    if Path.isScriptFrozen():
        ffmpegPathDepth = 1
    else:
        ffmpegPathDepth = 2

    ffmpegPath = Path.getAbsolutePathUpNLevels(
            Path.getAbsolutePathTolerantToFrozenExe(),
            ffmpegPathDepth)

    if os.name is 'posix':
        ffmpegPath = ffmpegPath + "FfmpegWindowsBuild/bin/ffmpeg.exe"
    else:
        ffmpegPath = ffmpegPath + "FfmpegWindowsBuild\\bin\\ffmpeg.exe"

    outputTimeStampedFile = Output.getTimeStampedPrependedFile("Output.mp4")

    cmd = [
            ffmpegPath,
            " -f concat -safe 0 -i ",
            gFfmpegListFile,
            " -c copy Output/",
            outputTimeStampedFile]

    cmd = ''.join([str(elem) for i,elem in enumerate(cmd)])

    print(cmd)
    subprocess.run(cmd, shell=True)

    #cleanup, remove FileList
    cleanUpFile(gFfmpegListFile)

if __name__ == "__main__":
    main(sys.argv[1:])

