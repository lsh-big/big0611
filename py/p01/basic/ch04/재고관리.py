# inventory = {'사과': 50, '바나나': 30, '오렌지': 25,}
# inventory.add('포도': 40)
# inventory.remove() 

class InventoryManager:
    def __init__(self):
        # 1. 초기 재고 설정
        self.inventory = {
            '사과': 50,
            '바나나': 30,
            '오렌지': 25
        }

    # 2-1. 새 상품 추가
    def add_new_item(self, item, quantity):
        self.inventory[item] = quantity
        print(f"{item} 재고 추가 완료")

    # 2-2. 기존 상품 재고 수정 (강제 변경)
    def update_item_stock(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] = quantity
            print(f"🔄 {item} 재고가 {quantity}개로 수정되었습니다.")
        else:
            print(f"❌ {item}은(는) 존재하지 않는 상품입니다.")

    # 2-3. 상품 삭제
    def delete_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"🗑️ {item} 상품이 삭제되었습니다.")
        else:
            print(f"❌ {item}은(는) 존재하지 않는 상품입니다.")

    # 3-1. 전체 재고 현황 출력
    def show_all_inventory(self):
        print("=== 현재 재고 현황 ===")
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}개")

    # 3-2. 특정 상품 재고 확인
    def check_item_stock(self, item):
        if item in self.inventory:
            print(f"{item} 재고: {self.inventory[item]}개")
        else:
            print(f"❌ {item} 상품을 찾을 수 없습니다.")

    # 3-3. 재고 부족 상품 찾기 (30개 미만)
    def check_low_stock(self, threshold=30):
        print("=== 재고 부족 상품 ===")
        for item, qty in self.inventory.items():
            if qty < threshold:
                print(f"{item}: {qty}개(재고 부족)")

    # 4-1 & 4-3. 상품 판매 (재고 차감 및 부족 시 경고)
    def sell_item(self, item, quantity):
        if item not in self.inventory:
            print(f"❌ {item}은(는) 판매할 수 없는 상품입니다.")
            return

        if self.inventory[item] < quantity:
            print(f"⚠️ [경고] {item}의 재고가 부족합니다. (현재 재고: {self.inventory[item]}개)")
        else:
            self.inventory[item] -= quantity
            print(f"{item} {quantity}개 판매 완료")

    # 4-2. 상품 입고 (재고 증가)
    def receive_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
            print(f"📦 {item} {quantity}개 입고 완료")
        else:
            print(f"❌ 등록되지 않은 상품입니다. 새 상품 추가 기능을 이용하세요.")


# --- 실행 및 결과 검증 (출력 예시 맞춤) ---
if __name__ == "__main__":
    # 시스템 가동
    manager = InventoryManager()

    # 포도 40개 추가
    manager.add_new_item('포도', 40)

    # 전체 재고 현황 출력
    manager.show_all_inventory()

    # 특정 상품 재고 확인 (사과)
    manager.check_item_stock('사과')

    # 재고 부족 상품 찾기 (30개 미만)
    manager.check_low_stock(30)

    # 사과 10개 판매
    manager.sell_item('사과', 10)

    # 사과 현재 재고 확인
    manager.check_item_stock('사과')