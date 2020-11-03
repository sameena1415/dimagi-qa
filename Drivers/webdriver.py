from selenium import webdriver


class Driver:

    def __init__(self):

        self.instance = webdriver.Chrome()
        self.instance.maximize_window()

    def currwinhand(self):
        self.instance.current_window_handle()

    def winhandle(self):
        self.instance.window_handles

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")
