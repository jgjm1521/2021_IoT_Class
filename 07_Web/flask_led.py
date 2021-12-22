from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

# 라우팅을 위한 뷰 함수
@app.route("/led")
def hello_world():
    return '''
    <p>Hello, Flask!</p>
    <a href="/led/on">LED ON</a>
    <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<cmd>")
def led_op(cmd):
    print(cmd)
    if cmd == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>LED ON</p>
            <a href="/led">Go Home</a>
        '''
    elif cmd == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>LED OFF</p>
            <a href="/led">Go Home</a>
        '''
if __name__ == "__main__":
    app.run(host="0.0.0.0")