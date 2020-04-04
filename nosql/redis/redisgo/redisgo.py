import redis


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



def main():
    redis = connect_redis("localhost", 6379, "")
    create_repo(redis)



main()
