# Programming services bot in Telegram

## Telegram bot for sell programming service

## How install this telegram bot
### firstly you should download needed package for telegram bot
```bash
git clone https://github.com/sardor86/programming_services_bot.git
```
```bash
cd programming_services_bot
```
```bash
pip install -r requirements.txt
```

### Next you need create user and database in Postgresql
```bash
CREATE USER [your_user_name] WITH PASSWORD [your_user_password];
```
```bash
CREATE DATABASE [your_basedata] OWNER [your_user_name];
```
### After you need create telegram bot in https://t.me/BotFather and you get your telegram bot token

### Next you need create operators group and programmer group and add your bot

### Then you need add https://t.me/myidbot to your groups, and you need write in your group /getgroupid and you got id your groups

### Next you need create .env file and write there
```
DB_HOST=[Your db host]
DB_USER=[Your db user]
DB_PASSWORD=[Your db password]
DB_DATA_BASE=[Your database]

BOT_TOKEN=[Your telegram token]

OPERATORS_GROUP_ID=[Your operator group id]
PROGRAMMER_GROUP_ID=[Your programmer group id]
```

### After you can start telegram bot when command
```bash
python bot.py
```