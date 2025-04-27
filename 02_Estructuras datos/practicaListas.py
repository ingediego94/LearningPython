nombres = [22,33,44]
otro = [99, 100, 105, True, True]

final = nombres + otro

print(final)

final.remove(True)

print(final)

final[0:0]= [00,11]
print(final)

final[5:5] = [55,66,77,88]
print(final)

final.remove(True)
print(final)

final.append(106)
print(final)

final.extend([107,108,109,110])
print(final)

final.remove(110)
print(final)

final[11:11] = [101,102,103,104]
print(final)

final.append(110)
print(final)