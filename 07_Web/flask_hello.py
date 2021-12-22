from flask import Flask

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

# 라우팅을 위한 뷰 함수
@app.route("/")

def hello_world():
    return '''
    <p>Hello, Flask!</p>
    <a href="/first">Go first</a>
    <a href="/second">Go second</a>
    '''
    
@app.route("/first")
def first():
    return '''
    <p>first</p>
    <a href="/">Go home</a>
    '''
@app.route("/second")
def second():
    return '''
    <p>second</p>
    <a href="/">Go home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")