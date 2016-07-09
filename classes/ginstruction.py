class GInstruction:
    def __init__(self, instructionType, xcoord, ycoord, zcoord, extrude, temperature):
        self.instructionType = instructionType
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord
        self.extrude = extrude
        self.temperature = temperature

    def toString(self):
        return "Type: " + self.instructionType + ", X: " + str(self.xcoord) + \
                ", Y: " + str(self.ycoord) + ", Z: " + str(self.zcoord) + \
                ", E: " + str(self.extrude) + \
                ", S: " + str(self.temperature);

    @staticmethod
    def fromLine(line):
        if len(line) == 0:
            return None

        if line[0] == 'G': # Handle G code
            xcoord = float(0)
            ycoord = float(0)
            zcoord = float(0)
            extrude = float(0)

            # Extract type
            instructionType = line[:GInstruction.getDelimiter(line)]

            # Extract X coord
            if 'X' in line:
                temp = line[line.index('X'):]
                temp = temp[1:GInstruction.getDelimiter(temp)]
                xcoord = float(temp)

            # Extract Y coord
            if 'Y' in line:
                temp = line[line.index('Y'):]
                temp = temp[1:GInstruction.getDelimiter(temp)]
                ycoord = float(temp)

            # Extract Z coord
            if 'Z' in line:
                temp = line[line.index('Z'):]
                temp = temp[1:GInstruction.getDelimiter(temp)]
                zcoord = float(temp)

            # Extract extrude
            if 'E' in line:
                temp = line[line.index('E'):]
                temp = temp[1:GInstruction.getDelimiter(temp)]
                extrude = float(temp)

            return GInstruction(instructionType, xcoord, ycoord, zcoord, extrude, float(0))
        elif line[0] == 'M': # Handle M code
            temperature = float(0)

            instructionType = line[:GInstruction.getDelimiter(line)]
            if line.index('S') >= 0:
                temp = line[line.index('S'):GInstruction.getDelimiter(line)]
                temperature = float(temp)

            return GInstruction(instructionType, 0, 0, 0, 0, temperature)
        else:
            return None


    @staticmethod
    def getDelimiter(string):
        index = string.index(' ')
        if index <= 0:
            index = len(string)-1

        offset = len(string) - index
        offset = offset * -1
        return offset
