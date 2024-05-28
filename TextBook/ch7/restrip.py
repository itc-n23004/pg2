def custom_strip(s, chars=None):
    if chars is None:
        chars = ' \t\n\r\x0b\x0c'  # 空白文字
    start = 0
    end = len(s)

    while start < end and s[start] in chars:
        start += 1

    while end > start and s[end - 1] in chars:
        end -= 1

    return s[start:end]

# テスト
print(f"[{custom_strip('  hello  ')}]")            # "[hello]"
print(f"[{custom_strip('  hello  ', ' ')}]")       # "[hello]"
print(f"[{custom_strip('...hello...', '.')}]")     # "[hello]"
print(f"[{custom_strip('xyzhellozyx', 'xyz')}]")   # "[hello]"

