from db import db

class ItemTags(db.model):
    __tablename__ = "item_tags"

id = db.Column(db.Integer, primary_key=True)
item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))