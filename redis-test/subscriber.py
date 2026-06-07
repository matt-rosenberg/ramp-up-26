import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

sub = r.pubsub()
sub.subscribe("MyChannel")

print("Waiting for messages: ")

for message in sub.listen():
    if message["type"] == "message":
        print("Received message: ", message["data"])