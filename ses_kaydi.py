import whisper
import os


file_path = input("Lütfen mp3 dosyasının tam yolunu yapıştırın: ").strip('"')

if not os.path.exists(file_path):
    print("Hata: Dosya bulunamadı!")
    exit()

print("Model yükleniyor... (Bu işlem biraz sürebilir)")
model = whisper.load_model("small")

print("Transkript oluşturuluyor...")

result = model.transcribe(file_path, language="tr", verbose=True)


print("\n--- SONUÇ ---\n")
print(result["text"])


txt_path = os.path.splitext(file_path)[0] + "_transkript.txt"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\nBaşarılı! Transkript şuraya kaydedildi: {txt_path}")