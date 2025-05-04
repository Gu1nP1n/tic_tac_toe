# gameparts/exceptions.py

class FieldIndexError(IndexError):
    """ Выбрасывается, если выбрано значение вне поля. """

    def __init__(
            self,
            message='Введено значение за границами игрового поля!'
            ):

        super().__init__(message)


# Вот оно - новое исключение, унаследованное от базового класса Exception.
class CellOccupiedError(Exception):
    def __init__(
            self,
            message='Попытка изменить занятую ячейку'
            ):

        super().__init__(message)
