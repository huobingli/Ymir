from comm import comm
from comm import logger

if __name__ == "__main__":
    print(comm.get_root_dir())

    ret = comm.merge_file("zipfile", "aaa.py")

    print(ret)
    if not ret:
        print(comm.merge_file("zipfile", "aaa.py"))

    logger.test()
    # is_git_dir