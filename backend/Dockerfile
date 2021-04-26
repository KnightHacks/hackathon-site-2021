FROM python:3.9.0-slim

ENV TZ America/New_York

WORKDIR /home/backend/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "gunicorn" ]
CMD [ "-b 0.0.0.0:5000", "src.__main__:main()" ]
