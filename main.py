import csv
import os
import sys
from data_structures import LinkedList, Stack

# File CSV Database
CSV_FILE = 'inventory.csv'
CSV_HEADERS = ['ID_Barang', 'Nama_Barang', 'Kategori', 'Jumlah', 'Harga']

# Inisialisasi Struktur Data Utama
inventory_list = LinkedList()
undo_stack = Stack()

def load_data():
    """Membaca data dari CSV dan memasukkannya ke Linked List"""
    if not os.path.exists(CSV_FILE):
        return
    
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory_list.append(row)
    except Exception as e:
        print(f"Error loading database: {e}")

def save_data():
    """Menulis isi Linked List ke dalam file CSV"""
    items = inventory_list.get_all()
    try:
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(items)
    except Exception as e:
        print(f"Error saving database: {e}")

def clear_screen():
    # Membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n" + "="*45)
    print("📦  SISTEM INVENTORI GUDANG  📦")
    print("="*45)
    print("1. Tampilkan Semua Barang")
    print("2. Tambah Barang Baru")
    print("3. Ubah Data Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Urutkan Barang")
    print("7. Undo Hapus Barang")
    print("8. Simpan & Keluar")
    print("="*45)

def print_items(items):
    if not items:
        print("\n[!] Data barang kosong.")
        return
    
    print("\n" + "-"*85)
    print(f"{'ID':<10} | {'Nama Barang':<20} | {'Kategori':<15} | {'Jumlah':<8} | {'Harga':<15}")
    print("-" * 85)
    for item in items:
        print(f"{item['ID_Barang']:<10} | {item['Nama_Barang']:<20} | {item['Kategori']:<15} | {item['Jumlah']:<8} | Rp {float(item['Harga']):<12,.2f}")
    print("-" * 85)

def main():
    load_data()
    
    while True:
        display_menu()
        choice = input("Pilih menu (1-8): ")
        
        if choice == '1':
            clear_screen()
            print(">>> DAFTAR BARANG <<<")
            print_items(inventory_list.get_all())
            
        elif choice == '2':
            clear_screen()
            print(">>> TAMBAH BARANG BARU <<<")
            id_barang = input("ID Barang: ").strip()
            
            if not id_barang:
                print("[!] ID Barang tidak boleh kosong.")
                input("\nTekan Enter untuk kembali...")
                continue

            if inventory_list.find_by_id(id_barang):
                print(f"[!] Barang dengan ID '{id_barang}' sudah ada!")
                input("\nTekan Enter untuk kembali...")
                continue
                
            nama = input("Nama Barang: ").strip()
            kategori = input("Kategori: ").strip()
            
            while True:
                try:
                    jumlah = int(input("Jumlah (Stok): "))
                    if jumlah < 0: raise ValueError
                    break
                except ValueError:
                    print("[!] Jumlah harus berupa angka bulat positif.")
                    
            while True:
                try:
                    harga = float(input("Harga (Rp): "))
                    if harga < 0: raise ValueError
                    break
                except ValueError:
                    print("[!] Harga harus berupa angka positif.")
            
            new_item = {
                'ID_Barang': id_barang,
                'Nama_Barang': nama,
                'Kategori': kategori,
                'Jumlah': jumlah,
                'Harga': harga
            }
            inventory_list.append(new_item)
            print("[+] Barang berhasil ditambahkan!")
            
        elif choice == '3':
            clear_screen()
            print(">>> UBAH DATA BARANG <<<")
            id_barang = input("Masukkan ID Barang yang akan diubah: ").strip()
            item = inventory_list.find_by_id(id_barang)
            
            if not item:
                print(f"[!] Barang dengan ID '{id_barang}' tidak ditemukan.")
            else:
                print(f"Data saat ini: {item['Nama_Barang']} (Stok: {item['Jumlah']}, Harga: Rp {float(item['Harga']):.2f})")
                print("Kosongkan isian lalu tekan Enter jika tidak ingin mengubah data tertentu.")
                
                nama = input(f"Nama Baru ({item['Nama_Barang']}): ").strip() or item['Nama_Barang']
                kategori = input(f"Kategori Baru ({item['Kategori']}): ").strip() or item['Kategori']
                
                jumlah_str = input(f"Jumlah Baru ({item['Jumlah']}): ").strip()
                jumlah = int(jumlah_str) if jumlah_str.isdigit() else item['Jumlah']
                
                harga_str = input(f"Harga Baru ({item['Harga']}): ").strip()
                try:
                    harga = float(harga_str) if harga_str else item['Harga']
                except ValueError:
                    harga = item['Harga']
                
                updated_data = {
                    'Nama_Barang': nama,
                    'Kategori': kategori,
                    'Jumlah': jumlah,
                    'Harga': harga
                }
                
                inventory_list.update_by_id(id_barang, updated_data)
                print("[+] Data barang berhasil diubah!")
                
        elif choice == '4':
            clear_screen()
            print(">>> HAPUS BARANG <<<")
            id_barang = input("Masukkan ID Barang yang akan dihapus: ").strip()
            
            deleted_item = inventory_list.delete_by_id(id_barang)
            if deleted_item:
                # Push ke stack untuk fitur undo
                undo_stack.push(deleted_item)
                print(f"[-] Barang '{deleted_item['Nama_Barang']}' berhasil dihapus.")
                print(f"[i] Gunakan fitur 'Undo' (menu 7) jika ingin mengembalikan data ini.")
            else:
                print(f"[!] Barang dengan ID '{id_barang}' tidak ditemukan.")
                
        elif choice == '5':
            clear_screen()
            print(">>> CARI BARANG <<<")
            print("1. Berdasarkan ID Barang")
            print("2. Berdasarkan Nama Barang")
            sub_choice = input("Pilih metode pencarian (1/2): ").strip()
            
            if sub_choice == '1':
                id_barang = input("Masukkan ID: ").strip()
                item = inventory_list.find_by_id(id_barang)
                print_items([item] if item else [])
            elif sub_choice == '2':
                nama = input("Masukkan keyword Nama: ").strip()
                results = inventory_list.search_by_name(nama)
                print_items(results)
            else:
                print("[!] Pilihan tidak valid.")
                
        elif choice == '6':
            clear_screen()
            print(">>> URUTKAN BARANG <<<")
            print("1. Berdasarkan Nama (A-Z)")
            print("2. Berdasarkan Jumlah Stok (Terbanyak - Terdikit)")
            print("3. Berdasarkan Harga (Termurah - Termahal)")
            sub_choice = input("Pilih metode pengurutan (1-3): ").strip()
            
            if sub_choice == '1':
                inventory_list.bubble_sort('Nama_Barang', descending=False)
                print("[+] Data berhasil diurutkan berdasarkan Nama.")
            elif sub_choice == '2':
                inventory_list.bubble_sort('Jumlah', descending=True)
                print("[+] Data berhasil diurutkan berdasarkan Stok terbanyak.")
            elif sub_choice == '3':
                inventory_list.bubble_sort('Harga', descending=False)
                print("[+] Data berhasil diurutkan berdasarkan Harga termurah.")
            else:
                print("[!] Pilihan tidak valid.")
                continue
            
            print_items(inventory_list.get_all())
            
        elif choice == '7':
            clear_screen()
            print(">>> UNDO HAPUS BARANG <<<")
            if undo_stack.is_empty():
                print("[!] Tidak ada data yang bisa di-undo (Stack kosong).")
            else:
                restored_item = undo_stack.pop()
                # Pastikan ID tidak bentrok
                if inventory_list.find_by_id(restored_item['ID_Barang']):
                    print(f"[!] Gagal undo: ID {restored_item['ID_Barang']} sudah ada di database.")
                    undo_stack.push(restored_item)
                else:
                    inventory_list.append(restored_item)
                    print(f"[+] Barang '{restored_item['Nama_Barang']}' berhasil dikembalikan ke dalam list!")
                    
        elif choice == '8':
            print("\nMenyimpan data ke database...")
            save_data()
            print("Data berhasil disimpan. Keluar dari aplikasi. Sampai jumpa!")
            sys.exit(0)
            
        else:
            print("[!] Pilihan tidak valid. Silakan coba lagi.")

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
