from discount import calculate_discount
def test_vip_customer():
    # hàm này tương tự assertEqual trong JAVA là kỳ vọng hàm calculate_discount(60000000) phải trả về 0.1
    assert calculate_discount(60000000) == 0.1
def test_normal_customer():
    # Kỳ vọng hàm calculate_discount(30000000) phải trả về 0
    assert calculate_discount(30000000) == 0
def test_TC03():
    # TC03: Tổng giá trị mua hàng trước đơn hàng: 49.000.000 VNĐ, mua 2.000.000 VNĐ, kỳ vọng trả về 0.1
    assert calculate_discount(49000000) == 0.1