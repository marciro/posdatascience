import redis
import random

def create_setnumber(r):
    for i in range(1,100):
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

    for i in range(1,51):
        print("Gerando o cartão: " +"card:"+str(i))
        card = r.srandmember("set:numbers", 15)
        print("Números escolhidos: "+str(card))
        for j in range (1,16):
            print("Adicionando "+str(card[j-1]))
            r.sadd("card:"+str(i),card[j-1])

        print(r.smembers("card:"+str(i)))
        r.sadd("available_cards",i)

def clearing(redis):
    redis.delete("set:numbers")
    for i in range(1,51):
        redis.delete("card:"+str(i))
        redis.delete("player:"+str(i)+":score")


def create_player(redis, i):
    redis.hset("player:"+str(i),"name","player"+str(i))
    draw_card = redis.spop("available_cards")
    redis.hset("player:"+str(i),"card","card:"+str(int(draw_card)))
    redis.hset("player:"+str(i),"score","score:"+str(0))
    print("Imprimindo os dados do jogador player:"+str(i))
    print(redis.hvals("player:"+str(i)))


def create_players(redis):
    for i in range(1,51):
        create_player(redis,i)


def theres_winner(redis):
    for i in range(1,51):
        player_score = redis.get("player:"+str(i)+":score")
        print("Verificando score do jogador player"+str(i)+": "+str(player_score))
        if player_score is not None and int(player_score) == 15:
            winners_name = redis.hget("player:"+str(i),"name")
            winners_card = redis.hget("player:"+str(i),"card")
            winners_numbers = redis.smembers(winners_card)
            print("Encontrado o vencedor:" + "player:" + str(i))

            print("Nome: "+str(winners_name))
            print("Cartão: " + str(winners_card))
            print("Números vencedores: " + str(winners_numbers))
            redis.set("winner", "player:"+str(i))
            return True
    return False


def check_score(redis,number_drawed):
    for i in range(1,51):
        card = redis.hget("player:"+str(i),"card")
        cardNumbers = redis.smembers(card)
        if number_drawed in cardNumbers:
            print("Número encontrado na cartela "+str(card)+": "+str(number_drawed))
            redis.incr("player:"+str(i)+":score",1)
            # Adicionar no score do jogador - Usar incr


def draw_number(redis):
    return redis.spop("set:numbers")


def start_game(redis):
    # Enquanto não houver vencendor, sortear um número
    # Percorrer todas as cartelas e adicionar no score de cada jogador caso tenha o número em sua cartela
    # O jogador que alcançar o score de 15 primeiro é o vencedor.


    while(not theres_winner(redis)):
        number_drawed = draw_number(redis)
        print("Número sorteado: "+str(number_drawed))
        check_score(redis,number_drawed)
        
        



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
    print(redis.get("winner"))


main()
