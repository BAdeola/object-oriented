from pessoa import Pessoa

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Amanada', 40)

    p1.comendo = False

    try:
        p1.falar('Artes')
        p1.falar('Artes')
    except Exception as e:
        print(e)

    print(p1.ano_atual)