def apply_plus(desired_count, lhs, rhs):
    res = [False for i in range(desired_count + 1)]
    for i in range(desired_count + 1):
        res[i] = lhs[i] or rhs[i]
    return res


def apply_point(desired_count, lhs, rhs):
    res = [False for i in range(desired_count + 1)]
    for i in range(desired_count + 1):
        for j in range(desired_count + 1):
            if lhs[i] and rhs[j] and i + j < desired_count+1:
                res[i+j] = True
    return res


def apply_star(desired_count, possible_count_array):
    res = [False for i in range(desired_count + 1)]
    res[0] = True
    counts_list = []
    for i in range(desired_count + 1):
        if possible_count_array[i]:
            counts_list.append(i)
    for i in range(desired_count + 1):
        if res[i]:
            for count in counts_list:
                if i + count < desired_count + 1:
                    res[i + count] = True
    return res


def create_count_array(desired_count, symbol, letter):
    res = [symbol != letter, symbol == letter]
    for i in range(desired_count - 1):
        res.append(False)
    return res


def process(regexp, letter, desired_count):
    st = []
    for ch in regexp:
        if ch in {'a', 'b', 'c', '1'}:
            st.append(create_count_array(desired_count, ch, letter))
        else:
            if len(st) == 0:
                return 2
            lhs = st.pop()
            if ch == '*':
                st.append(apply_star(desired_count, lhs))
                continue
            if len(st) == 0:
                return 2
            rhs = st.pop()
            if ch == '.':
                st.append(apply_point(desired_count, lhs, rhs))
            elif ch == '+':
                st.append(apply_plus(desired_count, lhs, rhs))
    if len(st) != 1:
        return 2
    return st[0][-1]


def main():
    inp = input().split()

    regexp = inp[0]
    letter = inp[1]
    desired_count = int(inp[2])

    return_code = process(regexp, letter, desired_count)
    if return_code == 2:
        print("ERROR")
    elif return_code:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
