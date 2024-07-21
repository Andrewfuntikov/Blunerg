from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.views.generic.base import View
from django.template.loader import render_to_string
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}
types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'books/index.html', context=context)


def get_info_about_sign_zodiac(requests, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac.title()
    }
    return render(requests, 'books/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound("НЕ правильный номер")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def index1(request):
    zodiac_style = list(types)
    """
    <ol>
        <li>Fire</li>
        <li>Earth</li>
        <li>Air</li>
        <li>Water</li>
    </ol>
    """
    li_elements = ""
    for sign in zodiac_style:
        redirect_path = reverse("type", args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_style(requests, und: str):
    description = types.get(und, None)
    if description:
        li_elements = ""
        for sign in description:
            redirect_path = reverse("horoscope-name", args=[sign])
            li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
        response = f"""
        <ul>
            {li_elements}
        </ul>
        """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound('Не найдено')


def get_info_by_date(request, month, day):
    month = int(month)
    day = int(day)
    zodiac = None

    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        zodiac = 'aries'
    elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
        zodiac = 'taurus'
    elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        zodiac = 'gemini'
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        zodiac = 'cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
        zodiac = 'leo'
    elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
        zodiac = 'virgo'
    elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        zodiac = 'libra'
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        zodiac = 'scorpio'
    elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
        zodiac = 'sagittarius'
    elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
        zodiac = 'capricorn'
    elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        zodiac = 'aquarius'
    elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
        zodiac = 'pisces'

    if zodiac:
        return HttpResponse(f"<h2>Месяц: {month}, День: {day}, Зодиак: {zodiac}</h2>")
    else:
        return HttpResponseNotFound("Неверные данные")
