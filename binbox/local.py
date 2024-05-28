import subprocess
try:
    from . import _tool
except:
    import _tool

"""
定义 local 函数用于在本地执行命令，并处理命令的输出和错误
command : 指令
log : 可选参数，用于指定日志文件路径
logout : 可选参数，用于指定是否将命令输出打印到标准输出
"""
def local(command:str, log=None, logout=True):
    """ 在本地执行命令, 如果 stderr 非空, 则 raise 异常
            log: 指向打印的保存路径
            print: 是否打印到 stdout/stderr
        返回 stdout 
    """
    if log !=None:
        fp = open(log, "w")
    #清理命令字符串
    command=_tool.command_clear(command)
    out_list = ""
    print(f"[binbox] local:{command}")

    # 使用 subprocess.Popen 执行命令，并将标准输入、标准输出和标准错误管道打开。universal_newlines=True 使得输入输出为文本模式，bufsize=1 表示行缓冲。
    ret = subprocess.Popen(command, shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, universal_newlines=True, bufsize=1)
    
    for line in ret.stdout:
        if logout:
            print(line, end="")
        out_list += line
        if log !=None:
            fp.write(line)
            fp.flush()
    # 等待命令执行完成
    ret.wait()
    if log !=None:
        fp.close()
    if ret.returncode != 0:
        for line in ret.stderr:
            print(line, end="")
        raise Exception(f"[binbox][error] run \"{command}\" failed")
    else:
        return out_list


if __name__ == "__main__":
    command="ls -alh test1111"
    command="find / -name \"*.so\""

    ret = local(command)
    
    pass
