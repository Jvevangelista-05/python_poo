from frota import *

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = True)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
<<<<<<< HEAD
    while carro1.odometro < 600 and caro2.odometro< 600:
=======
    while carro1.odometro < 10000:
>>>>>>> origin/main
        try:
            print('1- Ligar motor')
            print('2- Desligar motor')
            print('3- Acelerar')

<<<<<<< HEAD
            op_carro= 0
            while op_carro not in (1,2):
                op_carro = int(input("Qual carro vai usar[1,2]? "))

            if op_carro== 1:
              operar_carro(carro1)
            else:
                operar_carro(carro2)
             except Exception as e:
=======
            op = 0
            while op not in (1,2,3):
                op = int(input("Digite as opcoes[1-3]: "))

            if op == 1:
                carro1.ligar()
            elif op == 2:
                carro1.desligar()
            elif op == 3:
                v = float(input("Informe a velocidade: "))
                t = float(input("Informe o tempo: "))
                carro1.acelerar(v, t)

            print('Infos atuais do carro')
            print(carro1)
        except Exception as e:
>>>>>>> origin/main
            print("Erro!")
            print(e)

    carro1.desligar()
<<<<<<< HEAD
    carro2.desligar()
    if carro1.odometro > carro2.odometro
    print(carro1)
else:
    (carro2)
=======
    print(carro1)
    print('Parar para trocar óleo!!!')
>>>>>>> origin/main

