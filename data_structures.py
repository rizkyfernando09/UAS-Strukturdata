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

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Menambahkan data ke baris paling belakang antrean
    def enqueue(self, item):
        self.items.append(item)

    # Mengambil data dari baris paling depan (FIFO)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def get_all(self):
        return self.items

class TreeNode:
    def __init__(self, item_data):
        self.data = item_data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item_data):
        if self.root is None:
            self.root = TreeNode(item_data)
        else:
            self._insert_recursive(self.root, item_data)

    def _insert_recursive(self, node, item_data):
        # Kita urutkan berdasarkan Harga
        harga_baru = float(item_data['Harga'])
        harga_node = float(node.data['Harga'])
        
        if harga_baru < harga_node:
            if node.left is None:
                node.left = TreeNode(item_data)
            else:
                self._insert_recursive(node.left, item_data)
        else:
            # Jika harga sama atau lebih besar, ke kanan
            if node.right is None:
                node.right = TreeNode(item_data)
            else:
                self._insert_recursive(node.right, item_data)

    def get_min(self):
        """Mendapatkan barang dengan harga termurah (Node paling kiri)"""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def get_max(self):
        """Mendapatkan barang dengan harga termahal (Node paling kanan)"""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
