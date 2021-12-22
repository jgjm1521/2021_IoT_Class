from flask import Flask, render_template

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

# 라우팅을 위한 뷰 함수
@app.route("/")

def hello_world():
    return render_template("hello.html", title="Hello")
    
@app.route("/first")
def first():
    return render_template("first.html", title = "First Page")
@app.route("/second")
def second():
    return render_template("second.html", title = "Second Page")

if __name__ == "__main__":
    app.run(host="0.0.0.0")