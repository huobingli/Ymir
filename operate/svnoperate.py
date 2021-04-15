from comm import comm 
from os

# 是否是svn目录，判断是否包含.svn文件夹
def is_svn_dir(_work_dir):
    if not comm.is_exists(_work_dir):
        return False

    check_path = _work_dir + "/.svn"
    if comm.is_exists(check_path):
        return True
    return False

def _get_svn_tools():
    return '"' + os.path.dirname(os.path.abspath(__file__)) + '/../tools/svn/bin/svn.exe"'
    
def svn_checkout(svn_path, loacl_path, svn_username, svn_password):
    svn_exe = _get_svn_tools()
    svn_op  = " co "
    svn_pwd = " --password " + svn_password + " --username " + svn_username + " "
    svn_cmd = svn_exe + svn_op + " " + svn_pwd + svn_path + " " + loacl_path
    return comm.sync_exec(svn_cmd)


def svn_update_file(loacl_path):
    svn_exe = _get_svn_tools()
    svn_op  = " up "
    svn_cmd = svn_exe + svn_op + " " + loacl_path
    return comm.sync_exec(svn_cmd)


def svn_checkout_empty(svn_path, loacl_path):
    svn_exe = _get_svn_tools()
    svn_op  = " co --depth=empty "
    svn_pwd = " --password " + svn_password + " --username " + svn_username + " "
    svn_cmd = svn_exe + svn_op + " " + svn_pwd + svn_path + " " + loacl_path
    return comm.sync_exec(svn_cmd)

def svn_info(loacl_path):
    if not is_svn_dir(loacl_path):
        return False

    svn_exe = _get_svn_tools()
    svn_op  = " info "
    svn_cmd = svn_exe + svn_op + " " + loacl_path
    return comm.sync_exec(svn_cmd)

def svn_cleanup(loacl_path):
    if not is_svn_dir(loacl_path):
        return False

    svn_exe = _get_svn_tools()
    svn_op  = " cleanup "
    svn_cmd = svn_exe + svn_op + " " + loacl_path
    
    return comm.sync_exec(svn_cmd)