import webbrowser, sys,pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else: 
    #クリップボードから住所を取得する
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
