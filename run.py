# 程序的入口
from app.client import translate
# 此处使用绝对导入，会从项目根目录去找app文件夹里的client文件
# 导入服务器里的translate函数，这个函数自己又会去调用build_prompt

if __name__ == '__main__':
    result = translate('我能吞下玻璃而不伤身体', '英语')
    print(result)
