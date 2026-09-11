# 程序的入口
from app.client import translate
# 此处使用绝对导入，会从项目根目录去找app文件夹里的client文件
# 导入服务器里的translate函数，这个函数自己又会去调用build_prompt

state = {
    'target_lang':'英文',

}

#切换翻译目标语言的函数
def lang_switch(state:dict, args:str) -> None:
    if not args:
        print("没有输入要切换的语言，请输入“:lang 目标语言”，如“:lang 英文”") #防止没输参数
        return
    state['target_lang'] = args.strip() #让目标语言替换为命令输入的字符

# 利用字典和函数即值的特性，实现命令表功能：输入相应命令，调用函数
commands = {
    ':lang':lang_switch,
}

if __name__ == '__main__':
    #result = translate('我能吞下玻璃而不伤身体', '英语')
    #print(result)
    print("输入原文，回车返回译文；输入:lang 目标语言，回车切换目标语言；Ctrl+C退出程序\n")
    try:
        while True:
            source_text = input().strip() #去除用户输入首尾的空格
            if not source_text:
                continue #这个if用来防止用户什么也没输入，source_text是空字符串，那就直接跳过重来一轮输入

            if source_text.startswith(':'):#通过找:开头的字符串来识别命令
                cmd,_,args = source_text.partition(' ') 
                #这里必须用partition来切分为元组，不能用split，因为前者能拆分为固定的：命令 分隔符 参数
                #  
                handler = commands.get(cmd) #利用函数即值，直接让handler等于字典里命令名对应的函数操作
                if handler:
                    handler(state,args)#如果在字典里找到了匹配的命令，就把拆出的参数传进去，执行这个函数
                else:
                    print(f"未知命令：{cmd}，重新输入")
                continue

            try:
                result = translate(source_text, state['target_lang'])
                print(result)
            except Exception as err: 
                print(f"错误： {err}\n") 
                #常用的异常处理，把Python里绝大多数异常的基类Exception绑定到变量e上从而显示

    except KeyboardInterrupt:
        print("\n程序退出\n") #让用户在终端用Ctrl+C中断程序时能看见退出
