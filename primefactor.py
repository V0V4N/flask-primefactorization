from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def prime_factor():
    n = int(request.form['inputNumber'])  # получение числа из формы
    i = 2  # минимально возможный простой делитель
    f = []  # пустой список для всех делителей
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            f.append(i)
    if n > 1:
        f.append(n)
    return json.dumps('*'.join(map(str, f)))  # передача данных JSON

if __name__ == '__main__':
    app.run()
