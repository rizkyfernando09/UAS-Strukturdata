class Node:
    def __init__(self, item_data):
        # item_data is a dictionary containing ID, Nama_Barang, dll.
        self.data = item_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # CREATE: Menambahkan barang di akhir list
    def append(self, item_data):
        new_node = Node(item_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # READ: Mendapatkan semua data dalam bentuk array/list Python
    def get_all(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    # SEARCHING: Pencarian linier berdasarkan ID (Linear Search)
    def find_by_id(self, item_id):
        current = self.head
        while current is not None:
            if str(current.data['ID_Barang']) == str(item_id):
                return current.data
            current = current.next
        return None

    # SEARCHING: Pencarian linier berdasarkan Nama (Linear Search)
    def search_by_name(self, name_query):
        results = []
        current = self.head
        while current is not None:
            if name_query.lower() in current.data['Nama_Barang'].lower():
                results.append(current.data)
            current = current.next
        return results

    # UPDATE: Mengubah data barang berdasarkan ID
    def update_by_id(self, item_id, new_data):
        current = self.head
        while current is not None:
            if str(current.data['ID_Barang']) == str(item_id):
                current.data.update(new_data)
                return True
            current = current.next
        return False

    # DELETE: Menghapus barang berdasarkan ID dan mengembalikan datanya
    def delete_by_id(self, item_id):
        current = self.head
        
        # Jika barang yang dihapus ada di head
        if current is not None and str(current.data['ID_Barang']) == str(item_id):
            self.head = current.next
            return current.data

        # Cari barang yang mau dihapus
        prev = None
        while current is not None and str(current.data['ID_Barang']) != str(item_id):
            prev = current
            current = current.next

        # Jika ID tidak ditemukan
        if current is None:
            return None

        # Putuskan hubungan node yang dihapus
        prev.next = current.next
        return current.data

    # SORTING: Mengurutkan list menggunakan Bubble Sort
    def bubble_sort(self, key, descending=False):
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                val1 = current.data[key]
                val2 = current.next.data[key]
                
                # Konversi tipe data untuk komparasi angka
                if key in ['Jumlah', 'Harga']:
                    val1 = float(val1)
                    val2 = float(val2)
                else:
                    val1 = str(val1).lower()
                    val2 = str(val2).lower()
                
                condition = val1 < val2 if descending else val1 > val2
                
                if condition:
                    # Tukar datanya, bukan nodenya agar lebih mudah
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Menambahkan data ke dalam stack (Push)
    def push(self, item):
        self.items.append(item)

    # Mengambil data terakhir dari stack (Pop)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        
    def size(self):
        return len(self.items)
