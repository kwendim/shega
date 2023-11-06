FROM python:3.9.7-slim
RUN apt update
RUN apt install -y gcc
ENV PYTHONUNBUFFERED=1
# RUN pip install pipenv
RUN useradd -ms /bin/bash django
WORKDIR /shegagiveaway
COPY requirements.txt /shegagiveaway/
RUN pip install -r requirements.txt
COPY / /shegagiveaway/
# RUN chown -R django:django /fairway
# USER django