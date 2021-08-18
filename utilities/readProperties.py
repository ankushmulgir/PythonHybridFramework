import configparser

config=configparser.RawConfigParser()

path1 = r'C:\Users\amq5708\Desktop\Py\HybridFramework\Configurations\config.ini'
config.read(path1)
# config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getNaukriURL():
        return config.get('naukri','naukriURL')

    @staticmethod
    def getNaukriUserName():
        return config.get('naukri', 'user')

    @staticmethod
    def getNaukriPassword():
        return config.get('naukri', 'pwd')

