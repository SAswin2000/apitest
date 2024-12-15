FROM python:3.8-slim

WORKDIR /BakerHughes

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9130

CMD [ "python", "./app/main.py"]
