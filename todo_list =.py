todo_list = []

def show_menu():
    print("--- ToDoリスト メニュー ---")
    print("1. タスクを追加")
    print("2. タスクを表示")
    print("3. タスクを削除")
    print("4. 終了")

while True:
    show_menu()
    choice = input("番号を選んでください: ")

    if choice == "1":
        task = input("追加するタスクを入力してください: ")
        todo_list.append(task)
        print(f"「{task}」を追加しました。")

    elif choice == "2":
        print("\n--- 現在のToDoリスト ---")
        if not todo_list:
            print("タスクはありません。")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\n--- タスクを削除 ---")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
        try:
            num = int(input("削除するタスクの番号を入力してください: "))
            removed = todo_list.pop(num - 1)
            print(f"「{removed}」を削除しました。")
        except (ValueError, IndexError):
            print("無効な番号です。")

    elif choice == "4":
        print("ToDoリストを終了します。")
        break

    else:
        print("1〜4の番号を入力してください。")