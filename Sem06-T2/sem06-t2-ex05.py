
def converter(c):
    return (c * (9 / 5)) + 32

def main():

    celcius = float(input("Insira a temperatura em celsius: "))
    print(f"{converter(celcius):.2f}")

if __name__ == "__main__":
    main()