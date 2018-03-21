from bottle import run, default_app
from src.application import routes


def main():
    run(host='0.0.0.0', port='8081', debug=True)

if __name__ == '__main__':
    main()
else:
   application = default_app()
