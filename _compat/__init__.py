import sys


def isWin():
    windows = False
    plat = sys.platform
    if plat.startswith('win'):
        windows = True
    return windows


def modifyPath(relativePath: str) -> str:
    """
    :param relativePath:  目标文件的相对路径,默认输入linux下路径
    :return:
    """
    if win:
        relativePath = '\\'.join(relativePath.split('\\'))
    return relativePath


win = isWin()
