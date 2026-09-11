# 程序的入口
from app.client import translate
# 此处使用绝对导入，会从项目根目录去找app文件夹里的client文件
# 导入服务器里的translate函数，这个函数自己又会去调用build_prompt

if __name__ == '__main__':
    #result = translate('我能吞下玻璃而不伤身体', '英语')
    #print(result)
    print("输入原文，回车返回译文，Ctrl+C退出程序\n")
    try:
        while True:
            source_text = input().strip() #去除用户输入首尾的空格
            if not source_text:
                continue #这个if用来防止用户什么也没输入，source_text是空字符串，那就直接跳过重来一轮输入

            try:
                result = translate(source_text, '英语')
                print(result)
            except Exception as err: 
                print(f"错误： {err}\n") 
                #常用的异常处理，把Python里绝大多数异常的基类Exception绑定到变量e上从而显示

    except KeyboardInterrupt:
        print("\n程序退出\n") #让用户在终端用Ctrl+C中断程序时能看见退出
