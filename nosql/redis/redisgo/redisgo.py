import redis
import random

def create_setnumber(r):
    for i in range(1,99):
        r.sadd("set:numbers",int(i))


# Conectar no Redis
def connect_redis(p_host, p_port, p_password):
    r = redis.Redis(
        host=p_host,
        port=p_port,
        password=p_password)

    return r


def create_cards(r):
    create_setnumber(r)
    #srandmember retorna uma lista de string

    for i in range(1,50):
        print("Gerando o cartão: " +"card:"+str(i))
        card = r.srandmember("set:numbers", 15)
        print("Números escolhidos: "+str(card))

        for j in range (0,14):
            print("Adicionando "+str(card[j]))
            r.sadd("card:"+str(i),card[j])

        print(r.smembers("card:"+str(i)))
        r.sadd("available_cards",i)

def clearing(redis):
    redis.delete("set:numbers")
    for i in range(1,50):
        redis.delete("card:"+str(i))


def create_player(redis, i):
    redis.hset("player:"+str(i),"name","player"+str(i))
    draw_card = redis.spop("available_cards")
    redis.hset("player:"+str(i),"card","card:"+str(int(draw_card)))
    redis.hset("player:"+str(i),"score","score:"+str(0))
    print("Imprimindo os dados do jogador player:"+str(i))
    print(redis.hvals("player:"+str(i)))


def create_players(redis):
    for i in range(1,50):
        create_player(redis,i)


def theres_winner(redis):




    pass


def start_game(redis):
    # Enquanto não houver vencendor, sortear um número
    # Percorrer todas as cartelas e adicionar no score de cada jogador caso tenha o número em sua cartela
    # O jogador que alcançar o score de 15 primeiro é o vencedor.
    while(theres_winner(redis)):



def main():
    redis = connect_redis("localhost", 6379, "")
    #Limpar estruturas persistidas
    clearing(redis)
    # Gerar os cartões (50 cartões)
    create_cards(redis)
    # Criar 50 jogadores
    create_players(redis)
    # Iniciar o jogo
    start_game(redis)

    # Associar a cada jogador uma cartela e criar uma estrutura de jogo contendo o nome do jogador, sua cartela e o score
    # Iniciar o jogo gerando o conjunto de números sorteados e percorrendo cada cartela de cada jogador e pontuando no score
    # cada acerto. Quem acertar os 15 números é o vencendor.


    #card_37 = redis.smembers("card:37")
    #print(card_37)
    #print(card_37)



main()
