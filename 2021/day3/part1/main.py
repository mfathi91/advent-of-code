import os

input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
with open(input_file) as f:
    lines = f.read().splitlines()
    commonBitIndicator = []    # if commonBitIndicator[x] is positive, '1' is the most common bit at index x
    for i in range(len(lines[0])):
        commonBitIndicator.append(0)

    for line in lines:
        for i in range(len(line)):
            commonBitIndicator[i] = commonBitIndicator[i] + 1 if line[i] == '1' else commonBitIndicator[i] - 1

    gammaRate = ""
    epsilonRate = ""
    for n in commonBitIndicator:
        gammaRate += "1" if n > 0 else "0"
        epsilonRate += "0" if n > 0 else "1"

    print(int(gammaRate, 2) * int(epsilonRate, 2))    # 3912944
