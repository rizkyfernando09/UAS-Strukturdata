0sc   0s 0scn  # 📦 Sistem Inventori Gudang (UAS Struktur Data)

Sistem Inventori Gudang adalah sebuah aplikasi manajemen barang berbasis *Command Line Interface* (CLI) yang dibangun menggunakan bahasa pemrograman Python. Proyek ini dibuat untuk memenuhi tugas Ujian Akhir Semester (UAS) mata kuliah Struktur Data.

Aplikasi ini mendemonstrasikan implementasi nyata dari berbagai struktur data fundamental untuk mengelola stok barang, melacak harga, menangani antrean pesanan, hingga menyediakan fitur pemulihan (*undo*).

## ✨ Fitur Utama

- **Manajemen Barang:** Tambah, baca, ubah, dan hapus (CRUD) data barang.
- **Pencarian Cepat:** Cari barang berdasarkan ID atau Nama.
- **Pengurutan Fleksibel:** Urutkan barang berdasarkan Nama, Stok, atau Harga menggunakan *Bubble Sort*.
- **Fitur Undo:** Kembalikan barang yang tidak sengaja terhapus.
- **Sistem Antrean:** Kelola pesanan keluar dengan sistem barisan (siapa cepat, dia dapat).
- **Statistik Cerdas:** Temukan barang termurah dan termahal dengan sangat efisien.
- **Penyimpanan Permanen:** Data otomatis tersimpan dalam file `inventory.csv`.

---

## 🏗️ Implementasi Struktur Data

Proyek ini tidak menggunakan tipe data bawaan Python (seperti list atau dictionary) secara langsung untuk logika intinya, melainkan mengimplementasikan 4 struktur data utama dari nol:

### 1. Linked List (Daftar Berantai)
- **Kegunaan:** Digunakan sebagai struktur data utama penyimpan semua item di gudang (`inventory_list`).
- **Alasan:** Memungkinkan penambahan dan penghapusan data secara dinamis tanpa batasan ukuran memori yang tetap. Linked List pada proyek ini dilengkapi dengan metode *Bubble Sort* untuk pengurutan data.

### 2. Stack (Tumpukan)
- **Kegunaan:** Digunakan untuk fitur **"Undo Hapus Barang"** (`undo_stack`).
- **Konsep LIFO (Last-In-First-Out):** Barang yang terakhir kali dihapus akan dimasukkan ke tumpukan paling atas. Ketika pengguna membatalkan penghapusan (Undo), barang di tumpukan paling atas itulah yang akan diambil dan dikembalikan ke dalam gudang (Linked List).

### 3. Queue (Antrean)
- **Kegunaan:** Digunakan untuk mengelola **"Antrean Pesanan Keluar"** (`order_queue`).
- **Konsep FIFO (First-In-First-Out):** Pesanan barang yang masuk lebih dulu akan diletakkan di depan antrean. Saat pesanan diproses (stok gudang dikurangi), sistem akan memproses dari antrean paling depan terlebih dahulu.

### 4. Binary Search Tree / BST (Pohon Pencarian Biner)
- **Kegunaan:** Digunakan pada fitur **"Statistik Harga Barang"**.
- **Alasan:** Sangat efisien untuk mencari nilai minimum (Termurah) dan nilai maksimum (Termahal) dari kumpulan data yang sangat besar. BST memungkinkan pencarian ini dilakukan dalam waktu logaritmik `O(log N)`, jauh lebih cepat daripada mencari satu per satu.

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan Anda telah menginstal **Python 3**.
2. *Clone* repository ini ke komputer Anda.
3. Buka terminal/CMD dan masuk ke folder proyek:
   ```bash
   cd SistemInventoriGudang
   ```
4. Jalankan file utama:
   ```bash
   python main.py
   ```
5. Untuk menjalankan *unit test* pengecekan struktur data:
   ```bash
   python test_ds.py
   ```

---
*Dibuat oleh Rizky Fernando*
