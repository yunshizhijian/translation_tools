from tornado import web,ioloop,httpserver

#逻辑处理模块
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
       self.render('index.html')
#设置
settings = {
    'template_path':'template',
    'static_path':'static',
}
#处理前端传入的Word(跟页面对应)
class SearchWordHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        #获取前端的参数
        word = self.get_argument('word')
        print(word)

#路由,分发请求
application = web.Application([
            (r"/", MainPageHandler),
            (r"/search", SearchWordHandler),
        ],**settings)

#socket服务
if __name__ == '__main__':

        http_server = httpserver.HTTPServer(application)
        http_server.listen(8081)
        ioloop.IOLoop.current().start()