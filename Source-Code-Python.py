# Program Transformasi Gambar
# Nama: Agustinus Angelo Christian Fernando
# NIM: 21/473804/TK/52235

# Import library yang dibutuhkan
import numpy as np # Untuk perhitungan matematis
import cv2 # Untuk mengimport gambar

# Fungsi untuk melakukan translasi
def translasi(img, x, y):
    # Parameter img adalah path image yang ingin kita translasikan
    # Parameter x adalah jarak translasi secara horizontal
    # Parameter y adalah jarak translasi secara vertikal
    # Satuannya adalah pixel
    # Mengambil ukuran image
    baris, kolom = img.shape[:2]
    # Mendefinisikan matriks translasi
    M = np.float32([[1, 0, x], [0, 1, y]])
    # Melakukan transformasi pada gambar berdasarkan matriks transformasi yang sudah kita definisikan tadi
    hasilTranslasi = cv2.warpAffine(img, M, (kolom, baris))
    # Return hasil translasinya
    return hasilTranslasi


# Fungsi untuk melakukan dilasi
def dilasi(img, x, y):
    # Parameter img adalah path image yang ingin kita translasikan
    # Parameter x adalah besar scalling secara horizontal
    # Parameter y adalah besar scalling secara vertikal
    # Mengambil ukuran image
    baris, kolom = img.shape[:2]
    # Mendefinisikan matriks translasi
    M = np.float32([[x, 0, 0], [0, y, 0]])
    # Melakukan dilasi pada gambar berdasarkan matriks transformasi yang sudah kita definisikan tadi
    hasilDilasi = cv2.warpAffine(img, M, (kolom, baris))
    # Return hasil dilasinya
    return hasilDilasi


# Fungsi untuk melakukan refleksi
def refleksi(img, axis):
    # Parameter img adalah path image yang ingin kita translasikan
    # Parameter axis adalah arah refleksi yang ingin kita lakukan, yaitu x atau y.
    # Mengambil ukuran image
    baris, kolom = img.shape[:2]
    # 1. Jika axisnya x, maka dilakukan pencerminan terhadap x
    #    Oleh karena itu, kita mendefinisikan matriks transformasi untuk mencerminkan terhadap x
    # 2. Jika axisnya y, maka dilakukan pencerminan terhadap y
    #    Oleh karena itu, kita mendefinisikan matriks transformasi untuk mencerminkan terhadap y
    # 3. Jika inputan axisnya selain x dan y, maka sistem akan menampilkan tulisan bahwa inputan harus dalam bentuk x atau y.
    if axis == 'x':
        M = np.float32([[1, 0, 0], [0, -1, baris]])
    elif axis == 'y':
        M = np.float32([[-1, 0, kolom], [0, 1, 0]])
    else:
        print("================================================================")
        print("Inputan yang Anda masukkan salah. Pastikan inputan Anda x atau y")
        print("================================================================")
        exit()
    # Melakukan refleksi pada gambar berdasarkan matriks transformasi yang sudah kita definisikan tadi
    hasilRefleksi = cv2.warpAffine(img, M, (kolom, baris))
    # Return hasil refleksinya
    return hasilRefleksi


# Fungsi untuk melakukan rotasi
# Parameter img adalah image yang akan ditransformasikan
# Parameter angle adalah besar sudut rotasi yang akan diinginkan
def rotasi(img, sudut):
    # Mengambil ukuran image
    baris, kolom = img.shape[:2]
    # Mendefinisikan matriks transformasi untuk rotasi
    M = cv2.getRotationMatrix2D((kolom/2, baris/2), sudut, 1)
    # Melakukan rotasi pada gambar berdasarkan matriks transformasi yang sudah kita definisikan tadi
    hasilRotasi = cv2.warpAffine(img, M, (kolom, baris))
    # Return hasil rotasinya
    return hasilRotasi


# Fungsi untuk melakukan shearing
# Parameter img adalah image yang akan ditransformasikan
# Parameter x adalah besar shearing secara horizontal
# Parameter y adalah besar shearing secara vertikal
def shearing(img, x, y):
    # Mengambil ukuran image
    baris, kolom = img.shape[:2]
    # Mendefinisikan matriks transformasi untuk shearing
    M = np.float32([[1, x, 0], [y, 1, 0]])
    # Melakukan shearing pada gambar berdasarkan matriks transformasi yang sudah kita definisikan tadi
    hasilShearing = cv2.warpAffine(img, M, (kolom, baris))
    # Return hasil shearingnya
    return hasilShearing


# Fungsi untuk menampilkan pesan bahwa gambar hasil transformasi berhasil disimpan
def message():
    print("")
    print("=============================================================")
    print("Gambar hasil transformasi berhasil disimpan di perangkat Anda.")
    print("Silakan cek gambar hasil transformasinya di folder yang sama dengan lokasi file program ini.")
    print("=============================================================")
    print("")


# Fungsi utama
def main():
    # Pembuka Program
    print("")
    print("==============================================")
    print("Selamat Datang di Aplikasi Transformasi Gambar")
    print("==============================================")
    print("Mohon pastikan sudah membaca file README dahulu sebelum mengisi inputan")
    print(" ")

    # Inputan nama file gambar yang ingin ditransformasikan
    imgPath = input("Masukkan nama file gambar yang ingin ditransformasikan (contoh: gambar1.jpg): ")
    img = cv2.imread(imgPath)

    # Jika file gambar tidak ditemukan, maka akan muncul pesan error
    if img is None:
        print("==============================================================================")
        print("File gambar tidak ditemukan. Pastikan nama file yang Anda inputkan sudah benar.")
        print("==============================================================================")
        input("Press enter to exit...")
        exit()

    # User memilih transformasi yang diinginkan
    print("Transformasi yang dapat dilakukan:")
    print("1. Translasi")
    print("2. Rotasi")
    print("3. Refleksi")
    print("4. Dilasi")
    print("5. Shearing")
    kodeAngka = int(input("Silakan pilih kode angka jenis transformasi yang ingin dilakukan (contoh: 1): "))

    # Translasi
    if(kodeAngka == 1):
        xTranslasi = float(input("Masukkan jarak translasi horizontal (contoh: 130): "))
        yTranslasi = float(input("Masukkan jarak translasi vertikal (contoh: 90): "))
        hasilTranslasi = translasi(img, xTranslasi, yTranslasi)
        cv2.imwrite('Hasil_Translasi.png', hasilTranslasi)
        message()

    # Rotasi
    elif(kodeAngka == 2):
        sudutRotasi = float(input("Masukkan besar sudut rotasi (contoh: 45): "))
        hasilRotasi = rotasi(img, sudutRotasi)
        cv2.imwrite('Hasil_Rotasi.png', hasilRotasi)
        message()

    # Refleksi
    elif(kodeAngka == 3):
        sumbuPencerminan = input("Mau dicerminkan terhadap sumbu apa? (x atau y): ")
        hasilRefleksi = refleksi(img, sumbuPencerminan)
        cv2.imwrite('Hasil_Refleksi.png', hasilRefleksi)
        message()

    # Dilasi
    elif(kodeAngka == 4):
        skalaDilasiX = float(input("Berapa kali dilasi horizontal? (contoh: 3): "))
        skalaDilasiY = float(input("Berapa kali dilasi vertikal? (contoh: 1.3): "))
        hasilDilasi = dilasi(img, skalaDilasiX, skalaDilasiY)
        cv2.imwrite('Hasil_Dilasi.png', hasilDilasi)
        message()

    # Shearing
    elif(kodeAngka == 5):
        xShearing = float(input("Masukkan jarak shearing horizontal (contoh: 0.5): "))
        yShearing = float(input("Masukkan jarak shearing vertikal (contoh: 0.3): "))
        hasilShearing = shearing(img, xShearing, yShearing)
        cv2.imwrite('Hasil_Shearing.png', hasilShearing)
        message()

    # Jika kode angka yang dimasukkan salah, maka akan muncul pesan error
    else:
        print("=======================================================")
        print("Kode angka yang Anda masukkan salah. Silakan coba lagi.")
        print("=======================================================")

    input("Press enter to exit...")


# Memanggil fungsi main ketika program dijalankan
if __name__ == "__main__":
    main()
