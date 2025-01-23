FROM python:3.11

ENV PYTHONBUFFERED=1

WORKDIR /api

COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000