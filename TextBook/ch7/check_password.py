import re

def is_strong_password(password):
    # 8文字以上かどうかをチェック
    if len(password) < 8:
        return False
    
    # 大文字を含むかどうかをチェック
    if not re.search(r'[A-Z]', password):
        return False
    
    # 小文字を含むかどうかをチェック
    if not re.search(r'[a-z]', password):
        return False
    
    # 数字を含むかどうかをチェック
    if not re.search(r'\d', password):
        return False
    
    # すべての条件を満たしていればTrueを返す
    return True

 
passwords = ["password", "Password123", "pass123", "PASSWORD123", "Pass1234"]
for pwd in passwords:
    print(f"{pwd}: {is_strong_password(pwd)}")

