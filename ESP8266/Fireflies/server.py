import http


# a server that serves index.html
def index(req):
    with open("index.html", "r") as f:
        return f.read()


if __name__ == "__main__":
    http.start_server(index)
