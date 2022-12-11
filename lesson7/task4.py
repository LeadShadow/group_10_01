def first_last(letter: str, st: str) -> tuple:
    first_index = st.find(letter)
    last_index = st.rfind(letter)
    if first_index == -1:
        first_index = None
    elif last_index == -1:
        last_index = None
    return first_index, last_index


print(first_last('a', 'abbaaaab'))

