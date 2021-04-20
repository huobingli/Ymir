from comm import comm

# /curl.exe -F "file=@text.7z;filename=text.7z" http://172.0.80.1:81/upload.php

curl_tool = "tool/curl.exe"
upload_other_url = "http://172.0.80.1:81/upload.php"

# 通过curl 上传文件
def upload_file_to_url():

    # 获取工具路径
    curl_tool_path = comm.get_root_dir() + curl_tool
    if not comm.is_exists(curl_tool_path):
        return False
    
    file_name = ""
    
    upload_file = " -F " + '"file=@' + file_name + ";" + "filename=" + file_name + '"';

    upload_cmd = curl_tool_path + upload_file + upload_other_url
    
    # 执行
    comm.sync_exec(upload_cmd)




if __name__ == "__main__":
    pass