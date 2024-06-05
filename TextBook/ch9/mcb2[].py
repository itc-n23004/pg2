import shelve,pyperclip,sys
mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
#コマンドライン引数が３つで最初の引数が'save'である場合はクリップボードの内容をshelveに保存
#指定されたキーワード (sys.argv[2]) に対して、クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

# キーワード一覧と、内容の読み込み
#list コマンドの場合,shelve内の全てのキーワードのリストをクリップボードにコピーする
#指定されたキーワードがshelveに存在する場合、そのキーワードに対応する内容をクリップボードにコピーする
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

