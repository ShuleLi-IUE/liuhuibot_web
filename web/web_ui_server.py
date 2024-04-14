from http.server import SimpleHTTPRequestHandler, HTTPServer

# 定义一个自定义的请求处理类，用于返回指定的 HTML 页面
class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # 设置超时时间（单位：秒）
        timeout_seconds = 30
        self.request.settimeout(timeout_seconds)

        # html_content = None
        if self.path == '/' or self.path == '/index' or self.path == '/amrpolicy':
            # 读取 HTML 页面内容
            with open('index.html', 'rb') as file:
                html_content = file.read()
        elif self.path == '/reference':
            with open('reference.html', 'rb') as file:
                html_content = file.read()
        elif self.path == '/contact':
            with open('contact.html', 'rb') as file:
                html_content = file.read()
        else:
            # 如果没有匹配到任何路径，则返回一个默认的页面
            html_content = b"<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>"


        # 发送 HTML 页面内容作为响应
        self.wfile.write(html_content)

# 指定服务器地址和端口
server_address = ('', 80)

# 创建 HTTP 服务器，并指定自定义的请求处理类
httpd = HTTPServer(server_address, MyRequestHandler)

# 启动 HTTP 服务器
print('Starting server...')
httpd.serve_forever()
