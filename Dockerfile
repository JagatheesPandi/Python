FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p logs reports
CMD ["python","-m", "Test.TypeSpeeder_Enterpises"]
