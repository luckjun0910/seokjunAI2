from googletrans import Translator
import qrcode

# 번역할 텍스트
text_to_translate = "Hello my name is hong"

# 번역
translator = Translator()
translated_text = translator.translate(text_to_translate, dest="ko").text

# QR 코드 생성
img = qrcode.make(translated_text)

# QR 코드 이미지 파일로 저장
img.save("translated_qr_code.png")

print("QR 코드가 생성되었습니다.")
