class FileHandler:
    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
    
    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        print(f"Called enter")
        return self._file

    def __exit__(self, exc_tpye, exc_value, exc_traceback):
        self._file.close()
        print(f"Called exit")

with FileHandler("test.txt", 'w') as f:
    f.write("Test")
