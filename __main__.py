from comm import comm

if __name__ == "__main__":
    print(comm.get_root_dir())

    ret = comm.merge_file("zipfile", "aaa.py")

    print(ret)
    if not ret:
        print(comm.merge_file("zipfile", "aaa.py"))
    # is_git_dir