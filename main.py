from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        inp = request.form['inp']
        word = inp.split(' ')
        flag = ''
        for i in word:
            if(len(i)%2):
                flag+='<b>'+i[:len(i)//2+1]+'</b>'+i[len(i)//2+1:]+' '
            else:
                flag+='<b>'+i[:len(i)//2]+'</b>'+i[len(i)//2:]+' '
        return render_template('index.html', flag=flag)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# inp = input()
# word = inp.split(' ')
# for i in word:
#     if(len(i)%2):
#         print(i[:len(i)//2+1], i[len(i)//2+1:])
#     else:
#         print(i[:len(i)//2], i[len(i)//2:])

# print(word)