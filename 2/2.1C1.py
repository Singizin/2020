import numpy as np
# Sample Input:
#
# 4
# qqzbbacabadaba
# Sample Output:
#
# aacaaacaaacaaa
P = 4
s = 'qqzbbacabadaba'
d = len(s) % P
s += '#'*d
string_s = s
print(len(s))
s_np = np.array(list(string_s))
ss = np.reshape(s_np, (4, s_np.shape[0]//4))
print(ss)

def zfun(s):
     out = []
     if not s: return out
     i, slen = 1, len(s)
     out.append(slen)
     while i < slen:
         left, right = 0, i
         while right < slen and s[left] == s[right]:
             left += 1
             right += 1
         out.append(left)
         i += 1
     return out
print(zfun(s))
print(zfun('aacaaacaaacaaa'))