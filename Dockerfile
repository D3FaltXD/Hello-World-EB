FROM python:latest
WORKDIR /app
COPY . .
EXPOSE 3000
RUN pip install -r requirements.txt
CMD python3 -u web.py  # Shell form