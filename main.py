import cv2                         # OpenCV kütüphanesini içe aktarıyoruz (görüntü işleme için)
import matplotlib.pyplot as plt    # matplotlib ile görüntü göstereceğiz (grafik aracı gibi çalışır)

# opencv resmi BGR (Blue-Green-Red) formatında okur. Yani görüntü 'gizli' olarak 3 kanallıdır.
img = cv2.imread("v82wta66q5971.jpg")  # resmi yükledik, bu haliyle BGR (renkli) formattadır.

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Eğer matplotlib ile doğru renkli gösterim isteseydik bu satırı açmalıydık.
# Çünkü matplotlib RGB bekler, ama img BGR. Bu dönüşümle orijinal renge yaklaşılırdı.

# Aşağıdaki satır BGR olan resmi GRAY (tek kanallı gri tonlama) formata dönüştürür.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resim nesnesinin türünü ve özelliklerini yazdırıyoruz:
print(type(img))      # numpy.ndarray → görüntü verisi matris olarak tutulur
print(img)            # piksel değerlerini yazdırır
print(img.shape)      # (yükseklik, genişlik, kanal sayısı) — GRAY için (1085, 1080), BGR için (1085, 1080, 3)
print(img.size)       # toplam piksel sayısı (matris elemanlarının çarpımı)
print(img.dtype)      # veri tipi → genelde uint8 (0–255 arası piksel değeri)

# matplotlib, tek kanallı (gray) resmi 'colormap' eklemeden gösterirse renkli gibi görünür.
# cmap='gray' ekleyerek gerçekten gri görünmesini sağlıyoruz.
plt.imshow(img_gray, cmap="gray")   # gri resmi gösteriyoruz
plt.axis('off')                     # eksen çizgilerini kaldır
plt.show()                          # resmi pencereyle aç