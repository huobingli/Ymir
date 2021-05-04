
def FetchRecentLogToFile(output_dir, log_day, repo_dir):
    """
    获取log_day的日志
    :param output_dir: 输出目录
    :param log_day: 获取天数
    :param repo_dir: 仓库路径
    :return: 无
    """
    commit_log = FetchRecentLog(log_day, repo_dir)
    commit_log_file = output_dir + '\\commit.log'

    with open(commit_log_file, 'w', encoding='utf-8') as f:
        f.write(commit_log)
        f.close()

def FetchRecentLog(log_day, repo_dir):
    """
    获取log_day的日志
    :param log_day: 获取天数
    :param repo_dir: 仓库路径
    :return: 无
    """
    pass

def FetchGitLog(log_day, repo_dir):
    """
    gitlab获取log_day的日志
    :param log_day: 获取天数
    :param repo_dir: 仓库路径
    :return: 无
    """
    pass

def FetchSvnLog(log_day, repo_dir):
    """
    svn获取log_day的日志
    :param log_day: 获取天数
    :param repo_dir: 仓库路径
    :return: 无
    """
    pass

if __name__ == "__main__":
    pass