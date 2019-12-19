import random

def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|'
    char_len = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        num = random.randint(0, char_len)
        code += all_chars[num]
    print(code)

def main():
    generate_code(8)

if __name__ == '__main__':
    main()