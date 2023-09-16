class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Hàm để nhập danh sách liên kết từ người dùng
def inputLinkedList():
    # Khởi tạo danh sách liên kết rỗng
    head = None
    current = None

    while True:
        # Nhập giá trị cho nút mới
        value = input("Nhập giá trị cho nút (nhập 'q' để kết thúc): ")
        
        # Kiểm tra nếu người dùng muốn kết thúc
        if value == 'q':
            break
        
        # Tạo một đối tượng ListNode mới
        new_node = ListNode(int(value))
        
        # Nếu danh sách liên kết rỗng, đặt nút mới làm đầu danh sách
        if head is None:
            head = new_node
            current = head
        else:
            # Nếu danh sách liên kết không rỗng, thêm nút mới vào cuối danh sách
            current.next = new_node
            current = current.next

    return head

# Hàm để chèn một phần tử mới vào danh sách liên kết ở vị trí bất kỳ
def insertNode(head, position, value_to_insert):
    # Tạo một đối tượng mới với giá trị cần chèn
    new_node = ListNode(value_to_insert)

    # Trường hợp đặc biệt: chèn vào đầu danh sách
    if position == 1:
        new_node.next = head
        return new_node

    # Duyệt danh sách liên kết để tìm vị trí chèn
    current = head
    i=1
    while i<position-1:
        i=i+1
        current=current.next
    # Chèn phần tử mới vào vị trí đã xác định
    new_node.next = current.next
    current.next = new_node

    return head

# Tạo danh sách liên kết ban đầu
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
current = head

# Chèn một phần tử có giá trị 4 vào vị trí thứ 1 (số thứ tự bắt đầu từ 0)
head = insertNode(head, 3, 4)

# In danh sách liên kết sau khi chèn
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next