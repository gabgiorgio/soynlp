import sys
sys.path.insert(0, '../')
import soynlp
from soynlp.lemmatizer import conjugate

def main():
    testset = [
        ('깨닫', '아'), # ㄷ 불규칙
        ('구르', '어'), ('구르', '었다'), # 르 불규칙
        ('덥', '어'), ('줍', '어'), ('곱', '아'), ('곱', '어'), ('곱', '아서'),  # ㅂ 불규칙 모음조화
        ('아름답', '았다'), ('아니꼽', '어서'), ('아깝', '아서'), ('아깝', '어서'), ('감미롭', '아서'), # ㅂ 불규칙 모음조화가 깨진 경우
        ('이', 'ㅂ니다'), ('이', 'ㄹ지라도'), ('이', 'ㄴ'), ('이', 'ㅆ다'), # 어미의 첫글자가 초성일 경우
        ('벗', '어서'), ('긋', '어서'), ('긋', '었어'), ('낫', '아야지'), # ㅅ 불규칙
        ('푸', '어'), ('주', '어'), ('주', '었다'), # 우 불규칙
        ('오', '았어'), ('사오', '았다'), ('돌아오', '았지용'), # 오 규칙 활용
        ('끄', '었다'), ('끄', '어'), ('트', '었던건데'), ('들', '었다'),  # ㅡ 탈락 불규칙
        ('가', '아라'), ('삼가', '어라'), ('삼가', '아라니까'), ('돌아오', '아라'), # 거라/너라 불규칙
        ('이르', '어'), ('푸르', '어'), ('이르', '었다던'), # 러 불규칙
        ('아니하', '았다'), ('영원하', '었던'), # 여 불규칙
        ('파랗', '으면'), ('파랗', '면'), ('동그랗', 'ㄴ'), # ㅎ (탈락) 불규칙 
        ('파랗', '았다'), ('시퍼렇', '었다'), # ㅎ (축약) 불규칙
        ('그렇', '네'), ('파랗', '네요'), # ㅎ + 네 불규칙
        ('좋', '아'), ('좋', '았어'),
        ('하', '았다'), ('하', '었다'), # 여 불규칙 (2)
        ('좋아지', '었던'), # 이었 -> 였 규칙
        ('이', '었어') # 이었어, 였어
    ]

    for stem, eomi in testset:
        print('{} + {} -> {}'.format(stem, eomi, conjugate(stem, eomi)))

if __name__ == '__main__':
    main()