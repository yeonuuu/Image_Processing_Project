FROM python:3.10.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "src/test_image.py", "img_path"]