from bottle import route, run, template, request
from bot import output

f = open('sample.txt', 'r', encoding='shift_jis')
init_text = f.read()
f.close()

@route('/')
def view():
    return template('template_view', input_text=init_text, output_text=['','','','',''])

@route('/', method='POST')
def get_botwords():
    input_text = request.forms['input_text']
    output_text = output(input_text)
    return template('template_view', input_text=input_text, output_text=output_text)

run(host='localhost', port=8080, debug=True)
