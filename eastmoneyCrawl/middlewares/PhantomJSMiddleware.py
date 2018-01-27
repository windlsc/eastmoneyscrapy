
class PhantomJSMiddleware():
    @classmethod
    def process_request(cls, request, spider):

        if request.meta.has_key('fund_value'):
            driver = webdriver.PhantomJS() 
            driver.get(request.url)
            content = driver.page_source.encode('utf-8')
            driver.quit()  
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
