import redis
import random

def create_setnumber(r):
    for i in range(1,99):
        r.sadd('set_number',i)

# Conectar no Redis
def connect_redis(p_host, p_port, p_password):
    r = redis.Redis(
        host=p_host,
        port=p_port,
        password=p_password)

    return r


# Criar database do bingo
def create_repo(r):
    #r.set('foo','bar')
    #print(r.get('foo'))

    for user in range(1,50):
        create_card(user,r)



    #r.set('cartela_'+str(i), bingo_numbers)

def create_card(u,r):
    create_setnumber(r)
    #srandmember retorna uma lista de string
    srandmember = r.srandmember('set_number', 15)
    for i in range(1,15):
        rand_num = srandmember[i]
        #Enquanto o número já existir no conjunto, sorteia o próximo, senão prossegue
        #if(rand_num  )
        #Adiciona ao card que está sendo construido.
        r.sadd('card_'+str(u),srandmember[i])


def main():
    redis = connect_redis('localhost', 6379, '')
    create_repo(redis)

main()
