print('Please, enter a data: ')
data = input()
sequence = data.split()
for i, j in enumerate(sequence):
    print('Yes' if j in sequence[:i] else 'No')

