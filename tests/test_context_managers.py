from my_advanced_lib.core.context_managers import FileManager

def test_file_manager():
    with FileManager("test.txt", "w") as f:
        f.write("test")
    assert True
