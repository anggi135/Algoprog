def perulangan_for():
    print('Perluangan For:')
    for i in range(8):
        print(i)
    print()
def perulangan_bertingkat():
        print('Perluangan bertingkat')
        for i in range(8):
            for j in range(2):
              print(f"nilai i:{i},Nilai j:{j}")
        print()
def main():
    while True:
        print('Menu')
        print('1. perulangan for')
        print('2. perulangan bertingkat')
        print('3. keluar')
        pilihan= input('Masukan pilihan :')

        if pilihan == '1':
            perulangan_for()
        if pilihan == '2':
            perulangan_bertingkat()
        elif pilihan == '3':
            print('Terimakasih')
            break
        else:
             print('Pilihan tidal valid')
if __name__ == '__main__':
    main()
