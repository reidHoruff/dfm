import os, sys, shutil

SETTINGS_FILE = 'settings'
ME_AND_MY_BROTHER = ['push.py', 'pull.py']
BUCKET_DIR_NAME = 'files'

def error_out(msg):
    print '[error]', msg
    sys.exit(-1)

def proper_path(slang_path):
    return os.path.abspath(os.path.expanduser(slang_path))

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def ensure_bucket_exists_and_is_empty():
    if is_file(BUCKET_DIR_NAME):
        error_out('\'files\' in working dir must be a director')
    if is_dir(BUCKET_DIR_NAME):
        shutil.rmtree(proper_path(BUCKET_DIR_NAME))
    os.makedirs(BUCKET_DIR_NAME)

"""
heres the meat...
"""

def parse_settings_file():
    file = open(proper_path(SETTINGS_FILE))
    valid_lines = []
    for line in file:
        stripped_line = line.strip()
        if stripped_line and stripped_line[0] != '#':
            valid_lines.append(stripped_line)

    return  valid_lines

def copy_directory(path):
    pass

if __name__ == "__main__":
    ensure_bucket_exists_and_is_empty()
    files = parse_settings_file()
    for file in files:
        file_proper = proper_path(file)
        print file
        if is_file(file_proper):
            print 'file'
        elif is_dir(file_proper):
            print 'dir'
        else:
            print 'file does not exist:', file

