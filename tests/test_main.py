import unittest
from unittest import TestCase
import pytest

from main import *


@pytest.mark.parametrize(
    "names, expected", [[mentors, 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, '
                                   'Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, '
                                   'Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, '
                                   'Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий']]
)
def test_unique(names, expected):
    assert unique_names(names) == expected


@pytest.mark.parametrize(
    "names, expected", [[mentors, "На курсах \'Python-разработчик с нуля\' и "
                                  "\'Java-разработчик с нуля\' преподают: Антон, Евгений, Максим"]]
)
def test_super(names, expected):
    assert super_puper(names) == expected


@pytest.mark.parametrize(
    "names, expected", [[mentors, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']]
)
def test_unique3(names, expected):
    assert unique3(names) == expected


class TestYa(TestCase):
    @unittest.skipIf(ya.create_folder('Щуки') == 409, 'Папка уже создана')
    def test_folder(self):
        self.assertEqual(ya.create_folder('Щуки'), 201, 'Папка не создана')
