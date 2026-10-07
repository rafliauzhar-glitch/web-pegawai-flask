from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

def get_koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="PASSWORD_ANDA",
        database="latihan"
    )

@app.route("/")
def tampilkan_pegawai():
    koneksi = get_koneksi()
    cursor = koneksi.cursor()
    cursor.execute("SELECT * FROM pegawai")
    hasil = cursor.fetchall()
    koneksi.close()

    html = """
    <html>
    <head>
        <title>Data Pegawai</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            table { border-collapse: collapse; width: 60%; margin-bottom: 30px; }
            th, td { border: 1px solid #999; padding: 8px 12px; text-align: left; }
            th { background-color: #2E74B5; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            input { padding: 6px; margin: 4px; }
            button { padding: 6px 16px; background-color: #2E74B5; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Daftar Pegawai</h1>
        <table>
            <tr><th>ID</th><th>Nama</th><th>Divisi</th><th>Gaji</th></tr>
    """
    for baris in hasil:
        html += f"<tr><td>{baris[0]}</td><td>{baris[1]}</td><td>{baris[2]}</td><td>Rp{baris[3]:,.0f}</td></tr>"

    html += """
        </table>

        <h2>Tambah Pegawai Baru</h2>
        <form action="/tambah" method="POST">
            Nama: <input type="text" name="nama"><br>
            Divisi: <input type="text" name="divisi"><br>
            Gaji: <input type="text" name="gaji"><br>
            <button type="submit">Simpan</button>
        </form>
    </body>
    </html>
    """
    return html

@app.route("/tambah", methods=["POST"])
def tambah_pegawai():
    nama = request.form["nama"]
    divisi = request.form["divisi"]
    gaji = request.form["gaji"]

    koneksi = get_koneksi()
    cursor = koneksi.cursor()
    cursor.execute(
        "INSERT INTO pegawai (nama, divisi, gaji) VALUES (%s, %s, %s)",
        (nama, divisi, gaji)
    )
    koneksi.commit()
    koneksi.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)