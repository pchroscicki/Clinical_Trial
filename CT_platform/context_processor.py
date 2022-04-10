from datetime import date


def get_date(request):
    return {'actual_date': date.today()}