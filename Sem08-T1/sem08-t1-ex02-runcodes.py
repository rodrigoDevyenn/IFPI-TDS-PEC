
def verificaData(dA, mA, aA, dB, mB, aB):
     if aA > aB:
          return (f'{dA}/{mA}/{aA}')
     elif aA == aB and mA > mB:
          return (f'{dA}/{mA}/{aA}')
     elif aA == aB and mA == mB and dA > dB:
          return (f'{dA}/{mA}/{aA}')
     else:
          return (f'{dB}/{mB}/{aB}')

def main():
     dataA_d = int(input())
     dataA_m = int(input())
     dataA_a = int(input())

     dataB_d = int(input())
     dataB_m = int(input())
     dataB_a = int(input())

     print(verificaData(dataA_d, dataA_m, dataA_a, dataB_d, dataB_m, dataB_a))

if __name__ == '__main__':
     main()