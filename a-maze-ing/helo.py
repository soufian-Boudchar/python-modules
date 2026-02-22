import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"[+] Server listening on port {PORT}")

while True:
    client, addr = server.accept()
    print("[+] Connection from", addr)

    try:
        request = client.recv(4096).decode()
    except UnicodeDecodeError:
        print("[!] Cannot decode request, closing connection.")
        client.close()
        continue

    print("-----REQUEST------")
    print(request)
    print("------------------")

    lines = request.splitlines()
    if not lines:
        print("Empty request, closing connection.")
        client.close()
        continue

    request_line = lines[0]

    # Split the request line into method, path, and version
    method, path, version = request_line.split()

    print("METHOD:", method)
    print("PATH:", path)
    print("VERSION:", version)

    if path == "/":
        filename = "index.html"
    else:
        filename = path.lstrip("/")

    try:
        with open(filename, "r") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK"
    except FileNotFoundError:
        body = "<h1>404 Not Found</h1>"
        status_line = "HTTP/1.1 404 Not Found"

    http_response = (
        status_line + "\r\n" +
        "Content-Type: text/html\r\n" +
        "Content-Length: " + str(len(body.encode())) + "\r\n" +
        "Connection: close\r\n" +
        "\r\n" +
        body
    )

    client.sendall(http_response.encode())
    client.close()