import requests

from .prompt import build_prompt
# 使用相对导入，client从自己所在的包中找prompt
# 导入拼接提示词的函数

base_payload = {
    'max_tokens': 512,
    'temperature': 0.7,
    'top_k': 20,
    'top_p': 0.6,
    'repeat_penalty': 1.05, #重复惩罚不要用官方示例的repetition_penalty，llama.cpp不能识别
    'stream': False, #流式输出开关
    # 还缺提示词，待会在函数中拼接避免这些固定参数重复处理
}

def translate(source_text:str, target_lang: str) -> str:
    payload = {**base_payload, 'messages': [{'role': 'user', 'content': build_prompt(source_text,target_lang)}]}
    #新字典payload = 把字典base_payload解包复制一份，然后拼接prompt进去
    #需要注意的是，使用openai端口，要发送的是'message'，而非'prompt'

    #连接服务及错误处理
    try:
        r = requests.post('http://127.0.0.1:8080/v1/chat/completions', json=payload, timeout=60) 
        #发给llama.cpp，requests自动把字典转换为json
        r.raise_for_status() # 错误检查，如果客户端/服务端错误则抛出异常
    except requests.Timeout:
        raise RuntimeError("翻译请求超时")
    except requests.ConnectionError:
        raise RuntimeError(f"无法连接服务，请确认服务已启动")
    except requests.HTTPError as e:
        raise RuntimeError(f"服务返回错误 {r.status_code}: {r.text}") from e
    
    data = r.json() #拿到模型返回值，requests 把响应体解析成 Python 对象（字典/列表）

    # 调试信息
    print("finish_reason:", data['choices'][0].get('finish_reason'))  # stop / length，停止原因是正常停止还是撞上最长限制了
    usage = data.get('usage', {})
    timings = data.get('timings', {})
    print("prompt_tokens:", usage.get('prompt_tokens'))
    print("completion_tokens:", usage.get('completion_tokens'))
    print(f"speed: {timings.get('predicted_per_second'):.2f} tokens/s")
    #格式化输出，控制小数位数
    return data['choices'][0]['message']['content']