FROM mysterysd/wzmlx:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Install Node.js 24.x
RUN curl -fsSL https://deb.nodesource.com/setup_24.x | bash - \
    && apt-get install -y nodejs \
    && node -v && npm -v

# Copy project files and install Python deps
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
