result = 'test string'

def open_file( filename ):
    with open(filename) as f:
        result = f.read()
        return result

