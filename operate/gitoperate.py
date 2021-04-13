from comm import comm

# 是否是git目录，判断是否包含.git文件夹
def is_git_dir(_work_dir):
    if not comm.is_exists(_work_dir):
        return False

    check_path = _work_dir + "/.git"
    if comm.is_exists(check_path):
        return True
    return False
