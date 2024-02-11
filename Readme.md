# Programming services bot in Telegram

## Telegram bot for sell programming service

## How install this telegram bot
```
### Firstly you should to create telegram bot in https://t.me/BotFather and get your telegram bot token

### Next step you should create operators group and programmers group after add your bot

### Then you should add https://t.me/myidbot to your groups, and you need write in your group /getgroupid and you got id your groups

### Next you need create .env file and in write here
```
DB_HOST=[Your db host]
DB_USER=[Your db user]
DB_PASSWORD=[Your db password]
DB_DATA_BASE=[Your database]

BOT_TOKEN=[Your telegram token]

OPERATORS_GROUP_ID=[Your operator group id]
PROGRAMMER_GROUP_ID=[Your programmer group id]
```

### After you can start telegram bot whith command
```bash
docker-compose build .
docker-compose up
```
