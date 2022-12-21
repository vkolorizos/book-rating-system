FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app
