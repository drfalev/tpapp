from flask import Flask, render_template

app = Flask(__name__)

L = [
  {
    'a':'alma'
    , 'b':'banán'
    , 'c':'cseresznye'
  }
  , {
    'a':'répa'
    , 'b':'retek'
    , 'c':'mogyoró'
  }
]

@app.route("/")

def hello_wolrld():
  # return "Hello World now"  
  return render_template('home.html'
                        , list=L
                        )
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)








#  print("Hello World!")
