print("Continue :")
for i in range(1,11):
    if i == 3:
        continue
    print(i)

print("Break :")
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("Pass :(Using pass loop can be empty)")
for i in range(1,11):
    pass
