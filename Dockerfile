FROM python:3.10.8
EXPOSE 5000
WORKDIR /app
RUN pip install-r requirements.txt
COPY . .
 CMD ["app.py"]

