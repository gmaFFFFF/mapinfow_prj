from dataclasses import dataclass
from numbers import Number
from typing import Optional


@dataclass(frozen=True)
class Эллипсоид:
    proj_стр: str


@dataclass(frozen=True)
class Датум:
    proj_стр: str


@dataclass(frozen=True)
class Проекция:
    proj_стр: str


@dataclass(frozen=True)
class АффинноеПреобразование:
    s11: Number
    s12: Number
    xoff: Number
    s21: Number
    s22: Number
    yoff: Number


@dataclass(frozen=True)
class ГраницыСистемыКоординат:
    x_min: Number
    y_min: Number
    x_max: Number
    y_max: Number


@dataclass(frozen=True)
class СистемаКоординат:
    группа_ск: Optional[str]
    название_ск: Optional[str]
    код: Optional[int]
    датум: Датум
    проекция: Проекция
    афин: Optional[АффинноеПреобразование] = None
    границы: Optional[ГраницыСистемыКоординат] = None
