"""Exhaustive search (odd b <= 4000, L <= 11, starts +-2^(L-1)) for rational points where the CLOSED window
[-2^(L-1), 2^(L-1)] contains more distinct orbit values than p_v(L). Exact integers."""
def T(a,b): return a//2 if a%2==0 else (3*a+b)//2
found=[]
for L in range(1,12):
  M=1<<(L-1)
  for b in range(1,4001,2):
    for start in (M,-M):
      orb=[];pos={};x=start
      while x not in pos:
        pos[x]=len(orb);orb.append(x);x=T(x,b)
      if not(M in pos and -M in pos): continue
      pre=pos[x];per=len(orb)-pre;n=len(orb)
      ext=orb+[orb[pre+(i-pre)%per] for i in range(n,n+L+1)]
      w=[y&1 for y in ext]
      p=len({tuple(w[i:i+L]) for i in range(n)})
      cc=len({y for y in orb if -M<=y<=M})
      if cc>p: found.append((L,b,start,cc,p))
print("closed-window violations (L, b, a, #values in closed window, p(L)):", found)
