from googletrans import Translator
import qrcode

text_to_translate = "Hello my name is hong"

translator = Translator()
translated_text = translator.translate(text_to_translate, dest="ko").text

img = qrcode.make(translated_text)

img.save("번역문장qr코드.png")

print("QR 코드가 생성되었습니다.")
