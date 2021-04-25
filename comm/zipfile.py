import os

import zipfile 
from comm import comm


"""
    压缩指定文件夹
    :param _input: 目标文件夹绝对路径
    :param _output: 压缩文件绝对路径+filename.zip
    :return: 无
"""
def zip(_input, _output):
    
    if not comm.is_exists(_input):
        return 

    comm.delete_file(_output)
    _zip = zipfile.ZipFile(_output, 'w', zipfile.ZIP_DEFLATED)

    if os.path.isdir(_input):
        for path, _, fileList in os.walk(_input):
            relativePath = path.replace(_input, '')
            for filename in fileList:
                _zip.write(os.path.join(path, filename),
                    os.path.join(relativePath, filename))
    elif os.path.isfile(_input):
        _input_file = os.path.basename(_input)
        _input_path = os.path.dirname(_input)

        old_dir = comm.set_cur_dir(_input_path)
        _zip.write(_input_file)
        set_cur_dir(old_dir)

    _zip.close()

def uzzip(_input, _output):
    if not os.path.isfile(_input):
        return 

    # zfile = zipfile.ZipFile(_input,'r')
    # for filename in zfile.namelist():
    #     data = zfile.read(filename)
    #     file = open(filename,'w+b')
    #     file.write(data)
    #     file.close()