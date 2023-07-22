class Note:

    def __init__(self, note_id, note_title, note_body, time_of_change):
        self.id = note_id
        self.title = note_title
        self.body = note_body
        self.time = time_of_change

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"Title: {self.title}\n" \
               f"Body: {self.body}\n" \
               f"Time: {self.time}"

    def get_note(self):
        return {"Id": f"{self.id}", "Title": f"{self.title}", "Body": f"{self.body}", "Time": f"{self.time}"}
