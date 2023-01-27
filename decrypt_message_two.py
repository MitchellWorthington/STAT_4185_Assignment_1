encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
onehalf = encrypted_message[::2]
twohalf = encrypted_message[1::2]
twohalf = twohalf[::-1]

joined_list = []

for i in range(len(encrypted_message)):
    if i % 2 == 0:
        joined_list.append(onehalf[i//2])
    if i % 2 == 1:
        joined_list.append(twohalf[i//2])

output = ''.join(joined_list)
print(output)