import re

def text_clean(text):
    '''
    텍스트에서 기본적인 전처리 작업을 실행하는 함수
    '''
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern, '', text)
    
    # pattern = '[^\w\s]'         # 특수기호제거
    # text = re.sub(pattern, '', text)
    
    pattern = '(?<!\d)-|\b(?!\d+-\d)\d+\b|[^\w\s-]' # 번지수
    text = re.sub(pattern, '', text)
    
    pattern = '\s{2, }'           # 중복 공백 제거
    text = re.sub(pattern, '', text).strip() 
    
    pattern = '\n'            # 줄 바꿈 제거
    text = re.sub(pattern, '', text) 

    # pattern = '\d+'        # 숫자 제거
    # text = re.sub(pattern, '', text) 

    return text 