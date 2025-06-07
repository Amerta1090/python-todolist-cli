# main.py

from task import Task
from task_manager import TaskManager
import storage
import ui

DATA_FILE = "todolist.json"

def main():
    task_manager = TaskManager()
    
    # Load data dari file JSON
    saved_tasks = storage.load_data(DATA_FILE)
    task_manager.load_tasks(saved_tasks)

    while True:
        ui.print_menu()
        choice = input("Masukkan pilihan Anda: ").strip()

        if choice == '1':  # Lihat Semua Tugas
            tasks = task_manager.list_tasks()
            ui.display_tasks(tasks)

        elif choice == '2':  # Tambah Tugas
            title, description, priority, deadline, estimasi = ui.prompt_task_details()
            new_id = task_manager.generate_new_id()
            new_task = Task(new_id, title, description, status="Belum Selesai",
                            priority=priority, deadline=deadline, estimasi_waktu=estimasi)
            task_manager.add_task(new_task)
            storage.save_data(DATA_FILE, task_manager.to_dict_list())
            print("Tugas berhasil ditambahkan.")

        elif choice == '3':  # Edit Tugas
            task_id = ui.prompt_task_id()
            if task_id is None:
                continue
            task = task_manager.get_task(task_id)
            if not task:
                print("Tugas tidak ditemukan.")
                continue
            
            print("Masukkan data baru (kosongkan jika tidak ingin diubah):")
            title = input(f"Judul ({task.title}): ").strip() or task.title
            description = input(f"Deskripsi ({task.description}): ").strip() or task.description
            priority = input(f"Prioritas ({task.priority}): ").capitalize().strip() or task.priority
            deadline = input(f"Deadline ({task.deadline}): ").strip() or task.deadline
            estimasi_input = input(f"Estimasi waktu ({task.estimasi_waktu} menit): ").strip()
            try:
                estimasi_waktu = int(estimasi_input) if estimasi_input else task.estimasi_waktu
            except ValueError:
                estimasi_waktu = task.estimasi_waktu

            task_manager.edit_task(task_id, title=title, description=description,
                                   priority=priority, deadline=deadline, estimasi_waktu=estimasi_waktu)
            storage.save_data(DATA_FILE, task_manager.to_dict_list())
            print("Tugas berhasil diperbarui.")

        elif choice == '4':  # Tandai Tugas Selesai
            task_id = ui.prompt_task_id()
            if task_id is None:
                continue
            if task_manager.mark_done(task_id):
                storage.save_data(DATA_FILE, task_manager.to_dict_list())
                print("Tugas telah ditandai selesai.")
            else:
                print("Tugas tidak ditemukan.")

        elif choice == '5':  # Hapus Tugas
            task_id = ui.prompt_task_id()
            if task_id is None:
                continue
            task = task_manager.get_task(task_id)
            if not task:
                print("Tugas tidak ditemukan.")
                continue
            if ui.confirm_action(f"Yakin ingin menghapus tugas '{task.title}'?"):
                task_manager.delete_task(task_id)
                storage.save_data(DATA_FILE, task_manager.to_dict_list())
                print("Tugas berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
                
        elif choice == "6": #Filter Tugas
            kunci = input("Filter berdasarkan (status/priority): ").strip().lower()
            nilai = input(f"Masukkan nilai {kunci}: ")
            hasil = task_manager.filter_tasks(kunci, nilai)
            ui.display_tasks(hasil)

        elif choice == "7": #Search Tugas
            keyword = input("Masukkan kata kunci: ")
            hasil = task_manager.search_tasks(keyword)
            ui.display_tasks(hasil)

        elif choice == '8':  # Keluar
            print("Terima kasih telah menggunakan aplikasi To-Do List!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
