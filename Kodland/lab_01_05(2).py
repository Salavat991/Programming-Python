l = 'qwerty'
x = len(l)
for a in range(x):
    w1 = l[a]
    for b in range(x):
        if l[b] != l[a]:
            w2 = l[b]
        else:
            continue
        st = w1 + w2
        for c in range(x):
            if l[c] != w1 and l[c] != w2:
                w3 = l[c]
            else:
                continue
            st += w3
            for d in range(x):
                if l[d] != w1 and l[d] != w2 and l[d] != w3:
                    w4 = l[d]
                else:
                    continue
                st += w4
                for e in range(x):
                    if l[e] != w1 and l[e] != w2 and l[e] != w3 and l[e] != w4:
                        w5 = l[e]
                    else:
                        continue
                    st += w5
                    for f in range(x):
                        if l[f] != w1 and l[f] != w2 and l[f] != w3 and l[f] != w4 and l[f] != w5:
                            w6 = l[f]
                        else:
                            continue
                        st += w6
                        print(st)