def top3(st: str) -> str:
    dict1 = {}
    string_result = ''
    max = 0
    for i in st:
        dict1.update({i: st.count(i)})
    for k, v in dict1.items():
        if v > max:
            max = v
            string_result = f'{k} - {max}'
    return string_result


if __name__ == "__main__":
    print(top3('Улыбкой ясною природа Сквозь сон встречает утро года Синея блещут небеса. Еще прозрачные, леса'))