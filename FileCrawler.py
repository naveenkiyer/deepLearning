def find_files(directory, pattern):
    for root, dirs, files in os.walk("."):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in find_files('src', '*.c'):
    print 'Found C source:', filename