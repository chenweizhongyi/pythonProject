FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . /app

EXPOSE 5000

CMD ["uvicorn", "auth.server:app", "--host", "0.0.0.0"]