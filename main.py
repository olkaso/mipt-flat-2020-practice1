LTR_ALPH = {'a', 'b', 'c', '1'}


def process(reg, ltr, cnt):
    st = []
    for ch in reg:
        if ch in LTR_ALPH:
            lst = [ch != ltr, ch == ltr]
            for i in range(cnt-1):
                lst.append(False)
            st.append(lst)
        else:
            if len(st) == 0:
                return 2
            cnt2 = st.pop()
            res = [False for i in range(cnt+1)]
            if ch == '*':
                for i in range(cnt+1):
                    if i == 0:
                        res[0] = True
                    elif cnt2[i]:
                        k = 1
                        while k*i < cnt + 1:
                            res[k*i] = True
                            k += 1
                st.append(res)
                continue
            if len(st) == 0:
                return 2
            cnt1 = st.pop()
            if ch == '.':
                for i in range(cnt+1):
                    for j in range(cnt+1):
                        if cnt1[i] and cnt2[j] and i + j < cnt+1:
                            res[i+j] = True
                st.append(res)
                continue
            if ch == '+':
                for i in range(cnt+1):
                    res[i] = cnt1[i] or cnt2[i]
                st.append(res)
    if len(st) != 1:
        return 2
    return st[0][-1]


inp = input().split()

reg = inp[0]
ltr = inp[1]
cnt = int(inp[2])

ans = process(reg, ltr, cnt)
if ans == 2:
    print("ERROR")
elif ans:
    print("YES")
else:
    print("NO")
