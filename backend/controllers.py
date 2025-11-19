from backend.database import get_connection
from backend.models import Task
from datetime import datetime
def add_task(title: str, description: str) -> Task:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)",
            (title, description)
        )
        task_id = cursor.lastrowid
        conn.commit()
        return Task(id=task_id, title=title, description=description)
def get_tasks() -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, completed, created_at FROM todos")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(
                id=row[0],
                title=row[1],
                description=row[2],
                completed=bool(row[3]),
                created_at=datetime.fromisoformat(row[4])
            ))
        return tasks
def delete_task(task_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
        conn.commit()
def tooggle_task_completion(task_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT completed FROM todos WHERE id = ?", (task_id,)
            current_status = cursor.fetchone()
            if current_status:
                new_status = 0 if current_status[0] else 1
                cursor.execute(
                    "UPDATE todos SET completed = ? WHERE id = ?",
                    (new_status, task_id))
                conn.commit()
        )