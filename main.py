import pyzipper


def onTxtFiles(zf):
    for fileName in zf.namelist():
            if "txt" in fileName:
                test_bytes = zf.read(fileName)
                print(test_bytes)


def main():
    tests = ["test-1", "test-2", "test-3", "test-4", "test-5"]
    for test in tests:
        print(f"--- {test} ---")
        with pyzipper.AESZipFile(f'{test}.zip') as zf:
            for fileName in zf.namelist():
                if "zip" in fileName:
                    with pyzipper.AESZipFile(zf.open(fileName)) as nestedZf:
                        onTxtFiles(nestedZf)
            if not all(["zip" in fileName for fileName in zf.namelist()]):
                onTxtFiles(zf)
        


if __name__ == "__main__":
    main()