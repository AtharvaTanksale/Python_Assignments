try:
    f1 = open('tsk_1.txt', 'r')
    print(f"Line 1:{f1.read(12)}")
    print(f"Line 2:{f1.read(15)}")
except FileNotFoundError:
    print('File not found')
