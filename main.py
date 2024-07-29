import pyzipper

indent = 0

def onTxtFile(zf, fileName):
    global indent
    test_bytes = zf.read(fileName)
    print(str(" "*indent),test_bytes)


def onZipFile(zf):
    global indent
    print(str(" "*indent), f"+{zf.filename}")
    indent += 4
    for fileName in zf.namelist():
        if "zip" in fileName:
            with pyzipper.AESZipFile(fileName) as nestedZf:
                onZipFile(nestedZf)
        elif "txt" in fileName:
            onTxtFile(zf, fileName)
    indent -= 4
    print(str(" "*indent), f"-{zf.filename}")


def main():
    tests = ["test-1", "test-2", "test-3", "test-4", "test-5", "test-6"]
    for test in tests:
        print(f"--- {test} ---")
        with pyzipper.AESZipFile(f'{test}.zip') as zf:
            onZipFile(zf)


if __name__ == "__main__":
    main()