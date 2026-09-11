#默认翻译提示词模板
def build_prompt(source_text:str, target_lang: str) -> str:
    return(
        f'将以下文本翻译为 {target_lang}，注意只需要输出翻译后的结果，不要额外解释：\n\n'
        f'{source_text}'
    )