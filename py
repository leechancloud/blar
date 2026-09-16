tasks = []

while True:
    print("\n1. 할 일 추가  2. 목록 보기  3. 완료 처리  4. 종료")
    choice = input("선택: ")

    if choice == "1":
        tasks.append({"name": input("할 일: "), "done": False})

    elif choice == "2":
        if not tasks:
            print("등록된 할 일이 없습니다.")
        for i, task in enumerate(tasks, start=1):
            mark = "✓" if task["done"] else " "
            print(f"{i}. [{mark}] {task['name']}")

    elif choice == "3":
        try:
            number = int(input("완료한 할 일 번호: "))
            tasks[number - 1]["done"] = True
        except (ValueError, IndexError):
            print("올바른 번호를 입력하세요.")

    elif choice == "4":
        break

    else:
        print("1부터 4까지 선택하세요.")
