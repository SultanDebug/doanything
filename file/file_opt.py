# C:\Users\zhenqiang.huang\Desktop\searchprocess\pydata
def get_file_content(path, name):
    read = open(path + "/" + name, "r", encoding="utf-8")

    content = read.read()
    read.close()
    return content
def write_file(path,content):
    wrt = open(path, "w", encoding="utf-8")
    wrt.write(content)
    wrt.close()

if __name__ == '__main__':
    path = "C:/Users/zhenqiang.huang/Desktop/searchprocess/pydata"
    content = get_file_content(path, "source.txt")

    cntarr = content.split("\n")

    cntarr.sort()

    print(cntarr)

    # write_file(path+"/copy.txt",content+"cntarr")
