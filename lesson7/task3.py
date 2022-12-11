def search_substr(subst: str, st: str) -> str:
    lower_subst = subst.lower()
    lower_st = st.lower()
    print(lower_st)
    print(lower_subst)
    if lower_subst in lower_st:
        return 'Є контакт!'
    else:
        return 'Промах!'


print(search_substr('Кол', 'коЛокОл'))
