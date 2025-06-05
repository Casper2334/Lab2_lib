from dao.reader_dao import ReaderDAO

class ReaderService:
    @staticmethod
    def get_all_readers():
        return ReaderDAO.get_all_readers()

    @staticmethod
    def get_reader_by_id(reader_id):
        return ReaderDAO.get_reader_by_id(reader_id)