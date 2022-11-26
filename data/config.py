from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

#BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
#ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
ADMINS = ["5809435353:AAG1dQ4aYt1OBdubnCB4GxfNuALkbQmntEg"]
BOT_TOKEN="5809435353:AAG1dQ4aYt1OBdubnCB4GxfNuALkbQmntEg"


