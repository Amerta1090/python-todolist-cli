from datetime import datetime, timedelta

class Task:
    def __init__(self, id, title, description, status="Belum Selesai", priority="Sedang", deadline=None, estimasi_waktu=30, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.deadline = deadline  # Format: YYYY-MM-DD
        self.estimasi_waktu = estimasi_waktu
        self.created_at = created_at or datetime.now().isoformat()

        self.update_priority()

    def update_priority(self):
        if self.status == "Selesai":
            return
        if self.deadline:
            try:
                deadline_dt = datetime.strptime(self.deadline, "%Y-%m-%d")
                if deadline_dt <= datetime.now() + timedelta(days=2):
                    self.priority = "Tinggi"
                    return
            except ValueError:
                pass
        if self.estimasi_waktu > 60:
            self.priority = "Sedang"
        else:
            self.priority = "Rendah"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "deadline": self.deadline,
            "estimasi_waktu": self.estimasi_waktu,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        if "estimasi_waktu_pengerjaan" in data:
            data["estimasi_waktu"] = data.pop("estimasi_waktu_pengerjaan")
        return Task(**data)
