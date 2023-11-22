FROM python:3.10.12

COPY requirements.txt /temp/requirements.txt
COPY v_cats /v_cats

WORKDIR /v_cats

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -r /temp/requirements.txt

CMD ["docker run -it --rm --name redis -p 6379:6379 redis"]
