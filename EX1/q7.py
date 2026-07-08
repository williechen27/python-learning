password = input('請輸入密碼：')

if password[0].isupper():
    if not password.isupper():
        if len(password) >= 7 and len(password) <= 12:
            password = password[:2] + '*' * (len(password) - 3) + password[-1]
            print(f"{password = }")
        else:
            print('密碼長度不符合規定')
    else:
        print('密碼不可全為大寫')
else:
    print('密碼必須以大寫字母開頭')
