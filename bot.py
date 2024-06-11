from markov import calc_markov

def output(text):
    response = []
    try: 
        
        response = calc_markov(text)
        #print(response)

        if not response:
            response = ''
        return response

    except Exception as e:
        print('予期しないエラーが発生しています')
        print('* 種類:', type(e))
        print('* 内容:', e)
