FROM python:3.12.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 3000

CMD ["reflex", "run", "--backend-host", "0.0.0.0", "--backend-port", "3000"] 