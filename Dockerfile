FROM ubuntu
WORKDIR /tg_bot

RUN apt update
RUN apt upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]

