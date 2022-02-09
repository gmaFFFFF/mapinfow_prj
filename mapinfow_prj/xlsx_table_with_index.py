from __future__ import annotations

from typing import Union, Optional


class ТаблицаСИндексом:
    """
    Таблица в файле xlsx, имеющая индексный столбец (ключ)
    """

    class СтрокаТаблицы:
        """
        Строка в ТаблицаСИндексом
        """

        _таблица: ТаблицаСИндексом
        _данные: list

        def __init__(self, данные: list, таблица: ТаблицаСИндексом) -> None:
            super().__init__()
            self._таблица = таблица
            self._данные = данные

        def __getitem__(self, стлб: Union[str, int, slice]):
            if isinstance(стлб, str):
                return self._данные[self._таблица.заголовки.index(стлб)]
            elif isinstance(стлб, slice) or isinstance(стлб, int):
                return self._данные[стлб]
            else:
                raise TypeError(f'{стлб=} может быть str, int, slice, но не {type(стлб).__name__}')

        def __iter__(self):
            return self._данные.__iter__()

    заголовки: list[str]
    _строки: list[СтрокаТаблицы]
    _индекс_стлб: int

    def __init__(self, заголовки: list[str], данные: list[list], ключ_стлб: Optional[str]) -> None:
        super().__init__()
        self.заголовки = заголовки
        self._строки = [ТаблицаСИндексом.СтрокаТаблицы(стр, self) for стр in данные]
        self._индекс_стлб = заголовки.index(ключ_стлб) if ключ_стлб is not None else 1

    def __getitem__(self, ключ: Union[str, int, slice]) -> Union[list[СтрокаТаблицы], СтрокаТаблицы]:
        if isinstance(ключ, slice):
            return self._строки[ключ]
        elif isinstance(ключ, type(self._строки[0][self._индекс_стлб])):
            стр = [стр
                   for стр in self._строки
                   if стр[self._индекс_стлб] == ключ]
            return стр[0] if len(стр) == 1 else стр

        else:
            raise TypeError(f'Несовместимый формат {ключ=}')

    def __iter__(self):
        return self._строки.__iter__()
