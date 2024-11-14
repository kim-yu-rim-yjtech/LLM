from utils.db_utils import load_complaints, save_results
from utils.text_cleaning import clean_text
from utils.spacing_correction import correct_spacing_and_typos
from utils.stopwords import remove_stopwords
from utils.summarization import summarize_text
from utils.keyword_extraction import extract_keywords

from datetime import datetime

def main():
    # 1. DB에서 민원 데이터 불러오기
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== 1. 민원 데이터 불러오기 시작 ======')

    complaints = load_complaints()
    
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== 1. 민원 데이터 불러오기 완료 ======')
    
    
    # 2. 텍스트 클린 작업
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== 2. 텍스트 클린작업 시작 ======')
    
    cleaned_data = [clean_text(text) for text in complaints]
    
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== 2. 텍스트 클린작업 완료 ======')
    
    # # 3. 띄어쓰기 및 맞춤법 교정
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 3. 띄어쓰기 및 맞춤법 교정 시작 ======')
    
    # corrected_data = [correct_spacing_and_typos(text) for text in cleaned_data]
    
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 3. 띄어쓰기 및 맞춤법 교정 시작 ======')
    
    # # 4. 불용어 제거
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 4. 불용어 제거 시작 ======')
    
    # processed_data = [remove_stopwords(text) for text in corrected_data]
    
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 4. 불용어 제거 완료 ======')
    
    # # 5. 요약
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 5. 텍스트 요약 시작 ======')
    
    # summaries = [summarize_text(text) for text in processed_data]
    
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 5. 텍스트 요약 완료 ======')
    
    # # 6. 키워드 추출
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 6. 키워드 추출 시작 ======')
    # keywords = [extract_keywords(text) for text in summaries]
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 6. 키워드 추출 완료 ======')
    
    # # 7. 결과 DB에 저장
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 7. 결과 db에 저장 시작 ======')
    
    # save_results(summaries, keywords)
    
    # _now_time = datetime.now().__str__()
    # print(f'[{_now_time}] ====== 7. 결과 db에 저장 완료 ======')
    
    print("모든 작업이 완료되었습니다.")

if __name__ == "__main__":
    main()
