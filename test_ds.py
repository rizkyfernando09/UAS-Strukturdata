from data_structures import LinkedList, Stack

def test_ds():
    print("Testing Linked List...")
    ll = LinkedList()
    ll.append({'ID_Barang': '001', 'Nama_Barang': 'Laptop', 'Jumlah': 10, 'Harga': 5000000})
    ll.append({'ID_Barang': '002', 'Nama_Barang': 'Mouse', 'Jumlah': 50, 'Harga': 150000})
    
    assert len(ll.get_all()) == 2
    assert ll.find_by_id('001')['Nama_Barang'] == 'Laptop'
    
    ll.update_by_id('001', {'Jumlah': 15})
    assert ll.find_by_id('001')['Jumlah'] == 15
    
    deleted = ll.delete_by_id('002')
    assert deleted['ID_Barang'] == '002'
    assert len(ll.get_all()) == 1
    
    print("Testing Stack...")
    st = Stack()
    st.push(deleted)
    assert st.size() == 1
    
    restored = st.pop()
    assert restored['ID_Barang'] == '002'
    assert st.is_empty()
    
    print("All tests passed!")

if __name__ == "__main__":
    test_ds()
