import easygui as g
import os

def search(path):
    os.chdir(path)
    all_files = os.listdir(os.curdir)
    for each_file in all_files:
        ext = os.path.splitext(each_file)[1]
        if ext in ext_all:
            type_file(ext)
            count_line(each_file,ext)
            
        if os.path.isdir(each_file):
            search(each_file)
            os.chdir(os.pardir)
            
                
def type_file(ext):
    type_file_dict.setdefault(ext,0)
    type_file_dict[ext]+=1
    
def count_line(each_file,ext):
    try:
        f = open(each_file,encoding='UTF-8')
        print('正在分析文件：%s ...' % each_file)
        for each in f.read():
            count_line_dict.setdefault(ext,0)
            count_line_dict[ext] +=1
        f.close()
    except FileNotFoundError:
        pass
    

def show():
    
    All = 0
    for each in count_line_dict.values():
        All+=each
    str1 =''
    rest = 100000 - All
    p = All/1000
    
    msg='您目前共累积编写了'+str(All)+'行代码，完成进度:%.2f%%'%p+'\n离10万行代码还差'+str(rest)+'行，请继续努力！'
    title='统计结果'
    
    for each in count_line_dict.keys():
        str1=str1+'【'+each+'】源文件'+str(type_file_dict[each])+'个,源代码'+str(count_line_dict[each])+'行\n'
        
    
    g.textbox(msg,title,str1)    

dir1=g.diropenbox(msg='请选择您的代码库：')

type_file_dict = {}
count_line_dict = {}


ext_all = ['.c', '.cpp','.py', '.cc', '.java', '.pas', '.asm']

search(dir1)
show()



    


                
