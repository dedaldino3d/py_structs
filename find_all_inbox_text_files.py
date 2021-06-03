##############
## Get all files and directories with inbox in text
##############

import os, threading, time


PATH = "C:/Users/dedaldino3D/Documents/Projects/Erlang/MongooseIM"

FILE_MONGO = "searched_inbox_text_in_all_files.txt"
DIR_FILE = "C:/Users/dedaldino3D/Documents"
SKIP_DIRS = ["big_tests", "test", "load_test", "tests", "inbox"]



def create_or_open_file(dir, name):
    if(os.path.exists(name)):
        mfile = open(os.path.join(dir,name), 'a')
    else:
        mfile = open(name, 'x')
    return mfile


def write_to_file(stream, root, file, data, type='info'):
    if(type == 'ERROR'):
        print("{:*^60}".format("ERROR: UnicodeDecodeError"), file=stream)
        print("root: {:<10} file: {:<10}".format(root, \
        file, data), file=stream, flush=True)
    else:
        print("root: {:<10} file: {:<10} \n Data: {}".format(root, \
        file, data), file=stream, flush=True)


def run(path, stream, skip=None):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.erl'): # check only erlang files
                    with open(os.path.join(root, f)) as mongo_file:
                        try:
                            for text in mongo_file:
                                if "inbox" in text:
                                    print("Writing in file...{:*^10} root: {}".format("", root))
                                    time.sleep(.5)
                                    write_to_file(stream=stream, root=root, file=f, data=text)
                        except UnicodeDecodeError:
                            write_to_file(stream=stream, root=root, file=f, data="", type='ERROR')
            if skip:
                for d in dirs:
                    if d in skip:
                        print("Removing {} in Search, {:>5}dir: {}".format(skip, "", d))
                        time.sleep(1)
                        dirs.remove(d) # dont visit directories in skip directory
    else:
        raise AssertionError("Give a directory to lookup occurrences.")



if __name__ == '__main__':
    print("RUNNING ALGORITHM")
    print("{:*^30}".format(""))
    print("{:*^30}".format("Finding all occurrences of inbox in files"))
    
    file = create_or_open_file(DIR_FILE, FILE_MONGO)
    run(PATH, stream=file, skip=SKIP_DIRS)

    print("ALL OPERATIONS HAS FINISHED...")
    print("{:*^20} Check file {} {:*^20}".format("",os.path.join(DIR_FILE, FILE_MONGO),""))
    print("{:*^60}".format(""))


