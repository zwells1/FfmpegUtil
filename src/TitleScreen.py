import os

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def TerminalScreen(programName, argv = None):

    programDetails = programName + ' '

    if argv != None:
        for eachArg in argv:
            programDetails += eachArg
            programDetails += ' '

    print("FFmpeg utility: ", programDetails)
