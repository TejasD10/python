import os
import re
import sys
import glob


def main(pattern, filetype, replace=None, path="C:\\Users\\TDesai\\Documents\\GitHub\\Puppet_Master\\hieradata\\18.04\\care_engine_18_04"):
    r"""
    This is a utility that will be used to replace properties in puppet.
    :param pattern: The python style regular expression to be passed
    :param filetype: This pertains to the environment to be used,
                    for e.g. passing in AZPRD*.eyaml looks for prod files only, QA1-*.eyaml looks for QA1 env only, etc.
    :param replace: The replace string - This will be a key:value pair that will be the exact property as desired.
    :param path: The path of your puppet_master repo for e.g. r'c:\Users\TDesai\Documents\GitHub\Puppet_Master\hieradata\18.04\care_engine_18_04'
    :return: None

    sample usage for changing the kafka bootstrap server in all QA1- files
    python PuppetUtil.py "C:\\Users\\TDesai\\Documents\\Puppet_Master\\hieradata\\18.04\\care_engine_18_04" \
                            "kafka_bootstrap_servers:\s*'.+' QA1*.eyaml "kafka_bootstrap_servers: 'nycuvqa2kafka01.ahmcert.com:9092'"
    """
    # Check if the path exists
    if not os.path.exists(path):
        raise NotADirectoryError
        return

    # Print the passed in arguments for debugging
    print(f'Pattern : {pattern}')
    print(f'filetype : {filetype}')
    print(f'replace : {replace}')
    print(f'path : {path}')
    # change to the directory mentioned
    currdir = os.getcwd()
    os.chdir(path)

    #Search for files  - AZPRD*.eyaml etc.
    files = glob.glob(filetype, recursive=True)
    print('Number of Files Found: ' + str(len(files)))
    matchingcount = 0
    replacecount = 0
    # Iterate through each file
    for file in files:
        with open(file, 'r') as ofile:
            data = ofile.read()

        #Pattern regex - To find the pattern in the current open file
        patternregex = re.compile(pattern)
        matches = patternregex.findall(data)

        if matches:
            print(f'Found {len(matches)} of {str(matches)} in {str(file)}')
        matchingcount += len(matches)
        # Ask to replace in the current file only
        replaceconfirm = input("Do you want to replace it in the current file (y/n)? :")
        if replaceconfirm == 'y' or replaceconfirm == 'Y':
            for item in matches:
                newdata = data.replace(item, replace)
                data = newdata
            # replace the file contents with the new data
            with open(file, 'w') as currfile:
                currfile.write(newdata)
            replacecount += 1
        else:
            print('Not Replacing')
    print(f'TOTAL MATCHES FOUND: {matchingcount}')
    print(f'TOTAL REPLACED: {replacecount}')

    # Change back to the current directory
    os.chdir(currdir)
    return None


def usage():
    print('PuppetUtil.py <Path_To_Dir> <PythonStyleRegularExpression> <FileTypeRegex> [<Replace-with-string>]')


if __name__ == '__main__':
    print(f'Command Args Len: {len(sys.argv)}')
    if len(sys.argv) < 4:
        usage()
        sys.exit()
    if len(sys.argv) == 4:
        main(sys.argv[2], sys.argv[3], path=sys.argv[1])
    elif len(sys.argv) == 4:
        main(sys.argv[2], sys.argv[3], path=sys.argv[1])
    else:
        main(sys.argv[2], sys.argv[3], path=sys.argv[1], replace=sys.argv[4])


