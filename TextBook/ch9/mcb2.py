import shelve,pyperclip,sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    # キーワードの削除
    elif sys.argv[1].lower().startswith('delete'):
        keyword = sys.argv[1][6:]  # 'delete' の後のキーワードを取得
        if keyword in mcb_shelf:
            del mcb_shelf[keyword]

mcb_shelf.close()

