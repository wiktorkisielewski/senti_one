FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
COPY nginx.conf /etc/nginx/nginx.conf