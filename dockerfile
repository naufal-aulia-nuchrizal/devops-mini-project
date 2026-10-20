#1 gunakan python:3.11.9
From python:3.11-slim

#2 tentukan folder kerja di dalam container
WORKDIR /app

#3 salin file requirements.txt
COPY requirements.txt .

#4 install depedensi
run pip install --no-cache-dir -r requirements.txt

#5 salin kode aplikasi app.py ke dalam container
COPY app.py .

#6 jalankan aplikasi
cmd ["python", "app.py"]