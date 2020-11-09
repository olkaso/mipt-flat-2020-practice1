import sys


LTR_ALPH = {'a', 'b', 'c', '1'}


def find_divs(n):
    if n == 1:
        return [1]
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
        i = i+1
    return ans


def split(reg):
    st = []
    for ch in reg[:-1]:
        if ch in LTR_ALPH:
            st.append(ch)
        else:
            if ch == '*':
                if len(st) == 0:
                    sys.exit('ERROR: Incorrect input')
                a = st.pop()
                st.append(a + ch)
            else:
                if len(st) < 2:
                    sys.exit('ERROR: Incorrect input')
                b = st.pop()
                a = st.pop()
                st.append(a+b+ch)
    if len(st) != 2:
        sys.exit('ERROR: Incorrect input')
    return tuple(st)


def process(reg, ltr, cnt):
    if reg in LTR_ALPH:
        if reg == ltr:
            return cnt == 1
        return cnt == 0
    sym = reg[-1]
    if sym in LTR_ALPH:
        sys.exit('ERROR: Incorrect input')
    if sym == '*':
        if cnt == 0:
            return True
        divs = find_divs(cnt)
        for div in divs:
            if process(reg[:-1], ltr, div):
                return True
        return False
    reg1, reg2 = split(reg)
    if sym == '.':
        for i in range(cnt+1):
            if (process(reg1, ltr, i)) and (process(reg2, ltr, cnt - i)):
                return True
        return False
    if sym == '+':
        return process(reg1, ltr, cnt) or process(reg2, ltr, cnt)


inp = input().split()
if len(inp) != 3:
    sys.exit('ERROR: Incorrect input')

reg = inp[0]
ltr = inp[1]
cnt = inp[2]
if ltr not in ['a', 'b', 'c']:
    sys.exit('ERROR: Incorrect input')
try:
    cnt = int(cnt)
except ValueError:
    sys.exit('ERROR: Incorrect input')

if process(reg, ltr, cnt):
    print("YES")
else:
    print("NO")
