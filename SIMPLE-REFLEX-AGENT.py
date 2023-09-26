# Định nghĩa tập luật: Một điều kiện trạng thái và một hành động tương ứng
rules = {
    "A": "MOVE_RIGHT",
    "B": "MOVE_DOWN",
    "C": "MOVE_LEFT"
}

# Hàm để tìm hành động dựa trên trạng thái hiện tại và tập luật
def simple_reflex_agent(state, rules):
    if state in rules:
        return rules[state]
    else:
        # Hành động mặc định nếu không có luật phù hợp
        return "STAY"

# Hàm mô phỏng quá trình nhận thông tin từ môi trường và ra quyết định
def simulate_agent(percept):
    action = simple_reflex_agent(percept, rules)
    return action

# Hàm mô phỏng quá trình làm việc của tác tử trong môi trường
def run_simulation():
    current_state = "A"  # Trạng thái ban đầu
    while True:
        print(f"Trạng thái hiện tại: {current_state}")
        action = simulate_agent(current_state)
        print(f"Hành động: {action}")
        if action == "STAY":
            print("Tác tử đã dừng")
            break
        # Mô phỏng cập nhật trạng thái mới
        if current_state == "A":
            current_state = "B"
        elif current_state == "B":
            current_state = "C"
        else:
            current_state = "A"

# Chạy mô phỏng
run_simulation()


