
from web import Create_app

app = Create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
#     app.run(debug=True)
