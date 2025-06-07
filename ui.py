# ui.py

from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)  # Reset warna otomatis setiap print

def print_menu():
    print("\n=== Aplikasi To-Do List ===")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Edit Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Hapus Tugas")
    print("6. Filter Tugas")
    print("7. Search Tugas")
    print("8. Keluar\n")

def format_status(status):
    if status == "Selesai":
        return Fore.GREEN + status + Style.RESET_ALL
    else:
        return Fore.RED + status + Style.RESET_ALL

def display_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas untuk ditampilkan.")
        return

    table = []
    for t in tasks:
        table.append([
            t.id,
            t.title,
            t.description,
            format_status(t.status),
            t.priority,
            t.deadline,
            f"{t.estimasi_waktu} menit"
        ])

    headers = ["ID", "Judul","Deskripsi", "Status", "Prioritas", "Deadline", "Estimasi Waktu"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def prompt_task_details():
    title = input("Masukkan judul tugas: ").strip()
    description = input("Masukkan deskripsi tugas: ").strip()
    priority = input("Masukkan prioritas (Rendah/Sedang/Tinggi): ").capitalize().strip()
    deadline = input("Masukkan deadline (YYYY-MM-DD): ").strip()
    estimasi_waktu = input("Estimasi waktu pengerjaan (menit): ").strip()

    # Validasi sederhana
    if priority not in ["Rendah", "Sedang", "Tinggi"]:
        priority = "Sedang"
    try:
        estimasi_waktu = int(estimasi_waktu)
    except ValueError:
        estimasi_waktu = 30

    return title, description, priority, deadline, estimasi_waktu

def prompt_task_id():
    try:
        return int(input("Masukkan ID tugas: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

def confirm_action(message):
    choice = input(f"{message} (y/n): ").lower()
    return choice == 'y'
