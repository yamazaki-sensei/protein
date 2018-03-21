from bottle import run
from src.application import routes


def main():
    run(host='0.0.0.0', port='8081', debug=True)

if __name__ == '__main__':
    main()
