FROM python:3.7.10-slim

WORKDIR /root/

ENV VIRTUAL_ENV=/root/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN python -m pip install --upgrade pip &&\
    pip install -r requirements.txt

EXPOSE 8080

CMD "bash"
