import os 

from * import comm

# 是否是git目录，判断是否包含.git文件夹
def is_git_dir(_work_dir):
    if not comm.is_exists(_work_dir):
        return False

    check_path = _work_dir + "/.git"
    if comm.is_exists(check_path):
        return True
    return False

# 获取git工具
def _get_git_tools():
    return '"' + os.path.dirname(os.path.abspath(__file__)) + '/../tools/git/bin/git.exe"'

# 拉去分支
def git_pull(remote_url):
    # git_exe = _get_git_tools()
    
    # git_cmd = git_exe
    git_cmd = "git pull origin " + remote_url
    return comm.sync_exec(git_cmd)

# 克隆分支
def git_clone(remote_url, loacl_path, remote_branch):
    git_cmd = "git clone " + remote_url + " " + loacl_path + " --branch=" + remote_branch
    return comm.sync_exec(git_cmd)
    

# 切换分支
def git_switch_branch(remote_branch):
    git_cmd = "git switch " + remote_branch
    return comm.sync_exec(git_cmd)

# 切换tag
def git_switch_tag(git_tag):
    pass

def git_update():
    work_root = get_root_dir()
    # get work_dir
    # work_dir = comm.