from calculation import calculation_total

if __name__ == '__main__':
    # ユーザーからの入力を受け取る
    input_data = input("データを入力してください(スペース区切り) > ")

    print(input_data)
    # 文字列リストに変換
    numbers_as_str = input_data.split(" ")
    print(numbers_as_str)

    # 整数リストに変換する
    numbers = []  # 空のリストを作成
    for number_as_str in numbers_as_str:
        int_num = int(number_as_str)

        numbers.append(int_num)

    print(numbers)

    # 各統計量を計算する(合計, 平均, ...)
    total = calculation_total(numbers)

    # ユーザーに見やすいようにフォーマットする

    # 出力する
    print(f"合計: {total}")
