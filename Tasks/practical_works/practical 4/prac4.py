def read_file(file_name):
    out = set()
    with open(file_name, encoding='UTF-8', mode='r') as file:
        for line in file:
            [out.lower() for out in line.split()]
    return out

def save_file(file_name, out):
    with open (file_name, encoding='utf-8', mode='w') as f:
        f.write(f'Количество уникальных слов: {len(out)}\n')
        f.write('\n'.join(out))

out = read_file("data.txt")
save_file('count.txt', sorted(out))