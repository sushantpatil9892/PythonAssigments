filename = 'Sample1.txt'
try:
    file = open(filename, 'r')
    file_content = file.read()
except FileNotFoundError:
    print(f'Error: The {filename} was not found.')
    exit()
except Exception as e:
    print(f'Error: {e}')
    exit()
count = 0
for line in file_content.split('\n'):
    count += 1
    print(f'Line {count}: {line}')
exit