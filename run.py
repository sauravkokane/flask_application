if __name__ == "__main__":
    from application import app

    app.config['DEBUG'] = False
    app.config['FLASK_ENV'] = 'production'
    app.run()
