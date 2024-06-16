from flask import Flask

tpapp = Flask(__name__)
@tpapp.route("/")

def hello_wolrld():
  return "Hello World!"  

if __name__ == "__main__":
  tpapp.run(host='0.0.0.0', debug=True)








#  print("Hello World!")
