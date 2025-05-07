A=list(input())

alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
result=list(set(alphabet_list)-set(A))

print(result[0])