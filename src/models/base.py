from pydantic import BaseModel

from database import db


class LibraryBaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def serialize(self) -> dict:
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    @classmethod
    def create(cls, data: BaseModel):
        new_item = cls(**data.model_dump())
        db.session.add(new_item)
        db.session.commit()
        return new_item.serialize()

    @classmethod
    def get(cls, item_id):
        return cls.query.get(item_id)

    @classmethod
    def update(cls, data: BaseModel, id: int):
        item = cls.query.get(id)
        if not item:
            raise ValueError("Object not found")
        for field, value in data.model_dump().items():
            setattr(item, field, value)
        db.session.commit()
        return item.serialize()

    @classmethod
    def delete(cls, id):
        item = cls.query.get(id)
        if not item:
            raise ValueError("Object not found")

        db.session.delete(item)
        db.session.commit()

    @classmethod
    def list(cls) -> list:
        return [item.serialize() for item in cls.query.all()]
