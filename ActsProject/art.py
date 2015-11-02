from time import sleep
import colorama
import sys

class Terminal():
    def __init__(self, maxRows=50, maxColumns=79):
        colorama.init()

        self.maxRows = maxRows
        self.maxColumns = maxColumns

        self.frame = 0

        self.lineCount = 0
        self.prevLineCount = self.lineCount

        self.resetdelay = 0.02

    def draw(self, text, resetdelay=None):
        if resetdelay == None:
            resetdelay = self.resetdelay

        lines = text.split("\n")

        self.prevLineCount = self.lineCount
        self.lineCount = 0

        for line in lines:

            self.lineCount += 1

            length = len(line)

            if length > self.maxColumns:
                self.error(self.lineCount, "Too many columns in this animation")
            elif length < self.maxColumns:
                while len(line) < self.maxColumns:
                    line += " "

            print(line)

        self.frame += 1

        self.reset(resetdelay, self.lineCount)

    def reset(self, delay, linecount):
        sleep(delay)

        for i in range(linecount):
            sys.stdout.write("\033[1A")

        sys.stdout.write("\r")

    def finish(self, linecount):
        
        for i in range(linecount):
            print(" " * self.maxColumns)


    def error(self, line, message):
        self.reset(self.resetdelay, self.lineCount)
        self.finish(self.prevLineCount)
        print("Error (", self.frame, " : ", line, "): ", message, sep="")
        sys.exit(1)
