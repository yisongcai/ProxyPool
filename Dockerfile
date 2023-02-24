FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt
ENV APP_ENV=prod
ENV PROXYPOOL_REDIS_CONNECTION_STRING=redis://:redisQwer2wsx@192.168.137.216:6379/0
EXPOSE 5555
copy . .
VOLUME ["/app/proxypool/crawlers/private"]
CMD ['python', 'run.py']
