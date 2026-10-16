# devsecops-p5-NIM

## 1. Nama Aplikasi & Fungsinya
**Secure Task Manager** adalah aplikasi CLI untuk mengelola daftar tugas
(tambah, lihat, selesaikan, hapus) dengan validasi input dan penyimpanan JSON.

## 2. Bahasa / Framework
- Python 3.11 (standard library saja)
- Unit test: `unittest`
- SAST: Bandit

## 3. Cara Menjalankan
```bash
pip install -r requirements.txt
python -m src.main add "Belajar DevSecOps" -p high -d 2026-12-31
python -m src.main list
python -m src.main done 1
python -m src.main delete 1
python -m unittest discover -s tests -v
```

## 4. Overview Pipeline CI/CD
Workflow: `.github/workflows/devsecops.yml`
- **Trigger:** push dan pull_request ke branch `main`.
- **Job `build`:** checkout, setup Python, install dependencies, compile check, unit test.
- **Job `sast-scan`** (`needs: build`): menjalankan Bandit, mengunggah laporan JSON
  sebagai artifact, lalu **Quality Gate**: pipeline gagal jika ada temuan
  severity MEDIUM atau lebih tinggi.
