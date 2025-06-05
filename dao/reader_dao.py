from database import db, Reader

class ReaderDAO:
    @staticmethod
    def get_all_readers():
        return Reader.query.all()

    @staticmethod
    def get_reader_by_id(reader_id):
        return Reader.query.get(reader_id)