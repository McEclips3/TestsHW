import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv


courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко",
     "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко",
     "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, name_folder):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": name_folder, "url": link_url}
        response = requests.put(link_url, headers=headers, params=params)
        return response.status_code


def unique_names(all_mentors):

    # добавьте в список всех преподавателей со всех курсов
    all_list = []
    for m in all_mentors:
        all_list.extend(m)
    # допишите сюда ваш код, который заполнит all_list. можете как складывать списки, так и использовать метод extend

    # сделайте список all_names_list, состоящий только из имен, и заполните его
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])

    # сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    unique_names2 = set(all_names_list)

    # теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
    # допишите код ниже
    all_names_sorted = sorted(unique_names2)
    # допишите конструкцию вывода результата. можете использовать string.join()
    # результат будет в all_names_sorted
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def unique3(all_mentors):
    all_list = []
    for m in all_mentors:
        all_list.extend(m)
    # допишите сюда ваш код, который заполнит all_list. можете как складывать списки, так и использовать метод extend
    # сделайте список all_names_list, состоящий только из имен, и заполните его
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])

    # сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    unique_names3 = set(all_names_list)
    # подсчитайте встречаемость каждого имени через list.count()
    popular = []
    for name in all_names_list:
        popular.append((name, all_names_list.count(name)))
    # добавьте подсчет имен
    popular = list(set(popular))
    # добавьте  подсчет имен
    # это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
    # используйте его как есть (или при желании можете написать собственный :))
    popular.sort(key=lambda x: x[1], reverse=True)

    # получите топ-три самых часто встречающихся имен из списка popular
    # подсказка: возьмите срез списка
    top_3 = popular[0:3]
    top_str = []
    for name, count in top_3:
        top_str.append(name + ': ' + str(count))
    return f'{" раз(а), ".join(top_str)} раз(а)'


def super_puper(all_mentors):
    mentors_names = []
    for m in all_mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    # храните здесь пары курсов, на есть совпавшие имена
    pairs = []
    # # попарное сравнение "наборов" преподавателей на курсах. каждую новую пару запоминаем для исключения повторов.
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            # проверьте, что вы не сравниваете список сам с собой:
            if id1 == id2:
                continue
            # допишите ниже код для сравнения двух "наборов" преподавателей. подсказка: используйте множества
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:  # допишите проверку, что результат не пустой, имена есть
                # допишите ниже код, который проверяет, что эта пара еще не встречалась
                pair = {courses[id1], courses[id2]}
                # и если pair еще не встречалась, то выведите на экран два курса и список преподавателей,
                # которые есть на обоих курсах
                if pair not in pairs:
                    pairs.append(pair)
                    # отсортируйте имена по алфавиту. подсказка: используйте sorted() для списка
                    all_names_sorted = sorted(intersection_set)
                    # допишите конструкцию вывода результата. можете использовать string.join()
                    return f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}"


# if __name__ == '__main__':
dotenv_path = join(dirname(__file__), 'tokens.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("TOKEN")
ya = YandexDisk(token=TOKEN)
print(super_puper(mentors))
print(unique_names(mentors))
print(unique3(mentors))
ya.create_folder('щук')


