# Web Pegawai (Flask + MySQL)

Aplikasi web sederhana untuk menampilkan dan menambah data pegawai. Dibuat sebagai proyek belajar Python, Flask, dan MySQL.

## Fitur
- Menampilkan data pegawai dari database MySQL dalam bentuk tabel
- Menambah data pegawai baru melalui form
- Validasi input sebelum disimpan ke database

## Teknologi
Python, Flask, MySQL, HTML, CSS

## Cara Menjalankan
1. Install library: `pip install flask mysql-connector-python`
2. Import database: jalankan file `database_pegawai.sql` di MySQL Workbench
3. Buka file `web_pegawai.py`, lalu ganti `PASSWORD_ANDA` dengan password MySQL kamu
4. Jalankan: `python web_pegawai.py`
5. Buka `http://127.0.0.1:5000` di browser
