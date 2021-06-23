import argparse
from cryptography.fernet import Fernet
parser = argparse.ArgumentParser(description='自制简单加密器')
parser.add_argument('-e', '--encode', help='保存加密信息到safe.txt')
parser.add_argument('-d', '--decode', help='输出plaintext')
args = parser.parse_args()


# 预设参数
# key = Fernet.generate_key()
lock = Fernet(b'8GiEHryrOId7fJd9K8CeMAuubCjsL1UX5DDZWARByCE=')
# token = f.encrypt(b"A really secret message. Not for prying eyes.")

if args.encode:
    f1 = open(args.encode, 'r', encoding='utf-8')
    safetext = lock.encrypt(bytes(f1.read(), encoding='utf-8')).decode()
    f2 = open('safe.txt', 'w', encoding='utf-8')
    f2.write(safetext)
    f1.close()
    f2.close()

if args.decode:
    f1 = open(args.decode, 'r', encoding='utf-8')
    print(lock.decrypt(bytes(f1.read(), encoding='utf-8')).decode())