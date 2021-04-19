import os
import sys
import shutil

def is_exists(_dir):
    if os.path.exists(_dir):
        return True
    return False

def is_file(_path):
    return os.path.isfile(_path)

def mk_dir(_file):
    if not os.path.exists(_file):
        os.makedirs(_file)

def delete_dir(_dir):
    if os.path.exists(_dir):
        shutil.rmtree(_dir)
        
def delete_file(_file):
    if os.path.exists(_file):
        os.remove(_file)

def rename_file(_old_name, _new_name):
    if os.path.exists(_old_name):
        os.rename(_old_name, _new_name)

def copy_file(_from_name, _to_name):
    shutil.copyfile(_from_name, _to_name)

def move_file(_from_name, _to_name):
    shutil.move(_from_name, _to_name)

def get_root_dir():
    __root_dir = os.path.abspath(os.path.dirname(__file__) + "\\..\\" )
    return __root_dir

def async_exec(_cmd):
    print(_cmd)
    return os.popen(_cmd)

def sync_exec(_cmd):
    print(_cmd)
    return os.system(_cmd)

def merge_file(_path, _file_name):
    if not is_exists(_path):
        return False

    ret_path = os.path.dirname(_path + "\\")
    return ret_path + "\\" + _file_name

# 拷贝目录
def cp_dir(_from_path,  _to_path):
    __from_path = _from_path
    __to_path   = _to_path

    if not is_exists(__from_path):
        return
        
    mk_dir(__to_path)

    if is_file(__from_path):
        shutil.copyfile(__from_path, __to_path)
    else:
        __list = os.listdir(__from_path)
        for i in range(0, len(__list)):
            fn = __list[i]
            from_f = os.path.join(__from_path, fn)
            to_f   = os.path.join(__to_path, fn)
            if os.path.isdir(from_f):
                __cp_files_to_dir(from_f, to_f)
            else:
                shutil.copyfile(from_f, to_f)

