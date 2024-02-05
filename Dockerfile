FROM python:3.11-slim-buster AS build
WORKDIR /app
ENV TZ=UTC
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src

FROM build AS streamlit
ENV PORT 8501
CMD streamlit run src/Home.py --server.port=$PORT