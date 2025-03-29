FROM python:3.11
WORKDIR /app
COPY ./app /app/app
COPY ./main.py /app/main.py
RUN pip install --no-cache-dir fastapi uvicorn sqlmodel psycopg2-binary python-jose passlib[bcrypt]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]