# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Дождя не было, утка-маляр дошла до бара сухой. ')
    print('Утка уже забыла про зонт и не успела открыть его, '
          'когда на неё пролили стаканчик горячительного. ')


def step2_no_umbrella():
    print('Дождь был, утка-маляр промокла. ')
    print('Но утка не расстроилась, в баре всё равно было очень весело. ')


if __name__ == '__main__':
    step1()
