import re
import json
import pprint

def main():
    # Load the file

    regx = re.compile(r"^[m[e|k]\d+]")
    with open(r'C:\CareEngine\datapipe\OneRecord', 'r') as myfile:
        line = myfile.readline()

    words = line.split(",")
    #print(words)
    for word in words:
        print(word.split(":")[0])
    # found = regx.findall(line)
    # with open(r'C:\CareEngine\datapipe\OutputNonMe', 'x') as myfile:
    #     if found:
    #         pprint.pprint(found)


def findinfile():
    try:
        mifile = open(r'C:\CareEngine\datapipe\Practice\MI_All_Columns', 'r')
        dfile = open(r'C:\CareEngine\datapipe\Practice\DF_Columns', 'r')
        data = dfile.readlines()
        removenewline = {}
        [removenewline.update({str(line.strip().upper()): None}) for line in data]
        col = mifile.readline().strip()
        missingcols = []
        while col:
            if col not in removenewline:
                print(col)
                missingcols.append(col)
            col = mifile.readline().strip()

        print(f'Missing columns: {len(missingcols)}')
    finally:
        mifile.close()
        dfile.close()


if __name__ == '__main__':
    findinfile()
