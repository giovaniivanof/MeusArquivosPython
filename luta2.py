from random import randint as r
from random import choice as c

print("Você encontrou um zombi lute contra ele")
vida = 200
zombi = 150



defesa = ('fracassou sucesso fracassou').split()
sorte = c(defesa)
jogo = True
while jogo:
    if vida <= 0:
        print("Você perdeu")
        break
    elif zombi <= 0:
        print("Parabens você ganhou")
        break
    print()

    print(f"your life: {vida}\nzombi life: {zombi}\n")
    escolha =input("ATACAR DEFENDER\n").lower().strip()[:1]
    
    if escolha == 'a':
        escolha_atacar = input('Para girar o dado aperte d: ')
        print()
        if escolha_atacar == 'd':
            dado = r(1,20)
            print(f"Seu ataque foi de {dado}pts")
            if escolha_atacar == 'd':
                zombi -= dado
            
        else:
            print("Você usou o comando errado e morreu")
            break
    else:
        dano_contra_ataque = r(1,5)
        if sorte == 'sucesso':
            print(f'voce conseguio defender e lançar um contra ataque de {dano_contra_ataque}pts')
            if sorte == 'sucesso':
                zombi -= dano_contra_ataque
        else:
            print('sua defesa fracassou\nvocê recebera dano x2 no proximo ataque')

    print()
    print('Agora o zombi ira atacar')
    ataque_zombi = r(1,20)
    if escolha == 'a':
        print(f'você recebeu {ataque_zombi} de dano')
        if escolha == 'a':
            vida -= ataque_zombi
    else:
        if sorte == 'sucesso':
            print('defendeu')
            continue
        else:
            print(f'você recebeu {ataque_zombi*2} de dano')
            if sorte == 'fracassou':
                vida -= ataque_zombi*2


    print(),print(),print()
