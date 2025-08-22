from frota import Carro

if __name__ == '__main__':
    c1 = Carro("Fusca", "Branco", "Volkswagen", 5, 100)
    c2 = Carro("320i", "Preto", "BMW", 2, 80)

    c1.ligar()
    c2.ligar()

    tempo = 2
    velocidade1 = 6
    velocidade2 = 3
    distancia_final = 600

    try:
        while c1.odometro < distancia_final and c2.odometro < distancia_final:
            c1.acelerar(velocidade1, tempo)
            c2.acelerar(velocidade2, tempo)
    except Exception as e:
        print(f"\nCorrida interrompida: {e}")

    print(c1)
    print(c2)

    if c1.odometro > c2.odometro:
        print(f"\nO {c1.modelo} da {c1.marca} ganhou a corrida!")
    elif c2.odometro > c1.odometro:
        print(f"\nO {c2.modelo} da {c2.marca} ganhou a corrida!")
    else:
        print("\nEmpate!")

    try:
        c1.desligar()
        c2.desligar()
    except Exception:
        pass
