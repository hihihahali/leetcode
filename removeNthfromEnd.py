# Định nghĩa lớp ListNode để biểu diễn một nút trong danh sách liên kết
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Định nghĩa hàm để xóa nút thứ n từ cuối danh sách liên kết
def removeNthFromEnd(head, n: int):
    # Hàm tính chiều dài của danh sách liên kết
    def length(head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    # Tạo một nút giả để đảm bảo truy cập dễ dàng đến đầu danh sách
    dummy = ListNode(0)
    dummy.next = head
    a = dummy
    i = 1

    # Duyệt đến nút trước nút cần xóa
    while i < length(head)+1 - n:
        a = a.next
        i = i + 1

    # Kiểm tra nếu a.next không phải là None trước khi truy cập
    if a.next:
        b = a.next
        a.next = b.next

    # Trả về danh sách liên kết sau khi xóa nút đầu tiên (dummy.next)
    return dummy.next

# Tạo danh sách liên kết
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
new_head = removeNthFromEnd(head, n)

# In danh sách liên kết sau khi xóa nút thứ 2 từ cuối
current = new_head
while current:
    print(current.val, end=" ")
    current = current.next