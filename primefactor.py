from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def factorize():
    try:
        number = int(request.form['inputNumber'])
        # получение числа из формы
        if 2 <= number <= 1e21:
            n = number  # число, с которым будет работать алгоритм
        else:
            return render_template('index.html',
                                   resultNumber="INPUT OUT OF RANGE")
    except ValueError:
        return render_template('index.html', resultNumber="UNSUPPORTED INPUT")
    i = 2  # начальное значение делителя
    f = []  # список делителей
    while i * i <= n:
        if n % i:  # проверка условия кратности
            i += 1  # переход к следующему делителю
        else:
            n //= i  # деление числа на делитель
            f.append(i)  # запись делителя в список
    if n > 1:
        f.append(n)  # конец вычислений и запись последнего делителя
    result = '*'.join(map(str, f))  # перевод списка делителей в строку
    return render_template('index.html', resultNumber=result,
                           inputNumber=number)


if __name__ == '__main__':
    app.run()
