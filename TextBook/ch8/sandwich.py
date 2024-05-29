import pyinputplus as pyip

def sandwich_order():
    # パンの種類を選択
    bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='パンの種類を選んでください:\n')

    # タンパク質の種類を選択
    protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n')

    # チーズが必要かどうかを尋ねる
    cheese_needed = pyip.inputYesNo('チーズが必要ですか？ (yesまたはno):\n')

    # チーズが必要なら種類を選択
    cheese = None
    if cheese_needed == 'yes':
        cheese = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], prompt='チーズの種類を選んでください:\n')

    # その他のトッピングを尋ねる
    mayo = pyip.inputYesNo('マヨネーズが必要ですか？ (yesまたはno):\n')
    mustard = pyip.inputYesNo('からしが必要ですか？ (yesまたはno):\n')
    lettuce = pyip.inputYesNo('レタスが必要ですか？ (yesまたはno):\n')
    tomato = pyip.inputYesNo('トマトが必要ですか？ (yesまたはno):\n')

    # サンドイッチの個数を尋ねる
    number_of_sandwiches = pyip.inputInt('サンドイッチはいくつほしいですか？ (1以上の整数):\n', min=1)

    # 注文の確認
    print('\n注文内容:')
    print(f'パンの種類: {bread}')
    print(f'タンパク質の種類: {protein}')
    if cheese:
        print(f'チーズの種類: {cheese}')
    print(f'マヨネーズ: {"あり" if mayo == "yes" else "なし"}')
    print(f'からし: {"あり" if mustard == "yes" else "なし"}')
    print(f'レタス: {"あり" if lettuce == "yes" else "なし"}')
    print(f'トマト: {"あり" if tomato == "yes" else "なし"}')
    print(f'サンドイッチの個数: {number_of_sandwiches}')

if __name__ == "__main__":
    sandwich_order()

