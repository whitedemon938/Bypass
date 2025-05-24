FROM mysterysd/wzmlx:latest

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
