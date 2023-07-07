FROM python:3.9.17 as builder

WORKDIR /home/data

COPY . .
RUN pip install -r requirements.txt
RUN python create_embedding.py

FROM python:3.9.17

WORKDIR /home/data
COPY --from=builder /home/data/embeddings.pkl /home/data/embeddings.pkl
