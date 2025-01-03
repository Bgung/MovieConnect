from datetime import datetime

from .Base import Base

class Post(Base):
    def __init__(self):
        super().__init__('MovieConnect', 'posts')

    def insert(self, data):
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        data['views'] = 0
        return super().insert(data)
