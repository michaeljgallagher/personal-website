from app import app, db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    desc_short = db.Column(db.Text)
    desc_long = db.Column(db.Text)
    tech = db.Column(db.String(128))
    image = db.Column(db.String(128))
    github = db.Column(db.String(128))
    live = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f"<{self.id} {self.name}>"
