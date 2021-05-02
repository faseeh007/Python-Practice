sal=[32000,16000,23000,42000]
r=map((lambda s:s if s>25
       else s+500),sal)
print(tuple(r))
