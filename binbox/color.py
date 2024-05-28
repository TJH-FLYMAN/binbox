# 定义一些颜色和文本样式的ANSI转义码 

HEADER = '\033[95m'     #紫色
OKBLUE = '\033[94m'     #蓝色
OKCYAN = '\033[96m'     #青色
OKGREEN = '\033[92m'    #绿色
WARNING = '\033[93m'    #黄色
FAIL = '\033[91m'       #红色
ENDC = '\033[0m'        #重置
BOLD = '\033[1m'        #粗体
UNDERLINE = '\033[4m'   #下划线

if __name__ == "__main__":
    #终端中打印带有颜色和样式的文本 ，ENDC末尾重置颜色
    print(HEADER + "TEST:HEADER" + ENDC)
    print(OKBLUE + "TEST:OKBLUE" + ENDC)
    print(OKCYAN + "TEST:OKCYAN" + ENDC)
    print(OKGREEN + "TEST:OKGREEN" + ENDC)
    print(WARNING + "TEST:WARNING" + ENDC)
    print(FAIL + "TEST:FAIL" + ENDC)
    print(BOLD + "TEST:BOLD" + ENDC)
    print(UNDERLINE + "TEST:UNDERLINE" + ENDC)
    pass
