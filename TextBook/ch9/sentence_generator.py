import re

# 置換対象のキーワードリスト
keywords = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

# 入力ファイルのパス
input_file_path = 'input.txt'
# 出力ファイルのパス
output_file_path = 'output.txt'

# テキストファイルの読み込み
#with ステートメントを使用することで、ファイルのクローズを自動的に行います。
with open(input_file_path, 'r') as file:
    content = file.read()

# キーワードごとにユーザー入力を求める
replacements = {}
for keyword in keywords:
    while keyword in content:
        replacement = input(f"Enter an {keyword.lower()}: ")
        content = re.sub(keyword, replacement, content, 1)

# 結果を画面に表示
print("\nReplaced Text:\n")
print(content)

# 結果を新しいテキストファイルに保存
with open(output_file_path, 'w') as file:
    file.write(content)

