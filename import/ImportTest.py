import ImportFile

def test_file_name():
    assert ImportFile.get_name() == "ImportFile"

def test_main_file_name():
    assert __name__ == "__main__"

print(f"file name: {__name__}")
test_file_name()
test_main_file_name()

# do not test with pytest
