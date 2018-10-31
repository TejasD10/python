LOCATION = r'C:\CareEngine\Yaml_pwd.txt'


def main():
    with open(mode="r", file=LOCATION, ) as file:
        uniq = set()
        props = {}
        for data in file.readlines():
            idx = data.find(':')
            pwd = data[idx + 1:]
            prop = pwd[:pwd.find(':')]
            if not prop in uniq:
                uniq.add(prop)
                props[prop] = pwd
            # if out.find('=') == -1 and out.find(':') == -1:
            #     out = data[data.rfind(':', idx) + 1:]
            uniq.add(pwd)

    for prop, pwd in props.items():
        print(f'{pwd}', end="")


if __name__ == '__main__':
    main()
