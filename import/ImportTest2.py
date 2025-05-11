from temp_dir import TempFile

def test():
    assert TempFile.get_name() == "temp_dir.TempFile"
