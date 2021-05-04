import os
import zipfile 
from comm import comm

def zip(_input, _output):
    """
    压缩指定文件夹
    :param _input: 目标文件夹绝对路径
    :param _output: 压缩文件绝对路径+filename.zip
    :return: 无
    """
    if not os.path.exists(_input):
        return 
    os.path.delete_file(_output)
    _zip = zipfile.ZipFile(_output, 'w', zipfile.ZIP_DEFLATED)

    for path, _, fileList in os.walk(_input):
        relativePath = path.replace(_input, '')
        for filename in fileList:
            _zip.write(os.path.join(path, filename),
                os.path.join(relativePath, filename))
    _zip.close()

def uzzip(_input, _output):
    """
    解压指定zip文件
    :param _input: 目标文件夹绝对路径
    :param _output: 压缩文件绝对路径+filename.zip
    :return: 无
    """
    if not os.path.isfile(_input):
        return 
    zfile = zipfile.ZipFile(_input,'r')
    for filename in zfile.namelist():
        data = zfile.read(filename)
        file = open(filename,'w+b')
        file.write(data)
        file.close()