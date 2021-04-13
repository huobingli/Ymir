from comm import comm 

# 是否是svn目录，判断是否包含.svn文件夹
def is_svn_dir(_work_dir):
    if not comm.is_exists(_work_dir):
        return False

    check_path = _work_dir + "/.svn"
    if comm.is_exists(check_path):
        return True
    return False