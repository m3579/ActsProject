from time import sleep
import colorama
import sys

class Terminal():
    def __init__(self, maxRows=50, maxColumns=79):
        colorama.init()

        self.maxRows = maxRows
        self.maxColumns = maxColumns

        self.frame = 0

        self.resetdelay = 0.02

    def draw(self, text, resetdelay=None):
        if resetdelay == None:
            resetdelay = self.resetdelay

        lines = text.split("\n")

        lineCount = 0

        for line in lines:

            length = len(line)

            if length > self.maxColumns:
                error(lineCount + 1, "Too many columns in this animation")
            elif length < self.maxColumns:
                while len(line) < self.maxColumns:
                    line += " "
                    
            lineCount += 1

            print(line)

        self.reset(lineCount, resetdelay)

    def reset(self, lineCount, delay):
        sleep(delay)

        for i in range(lineCount):
            sys.stdout.write("\033[1A")

        sys.stdout.write("\r")

    def error(self, line, message):
        print("Error (", self.frame, " : ", line, "): ", message, sep="")
        sys.exit(1)
