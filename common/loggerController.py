import logging
import colorlog


class Logger:
    def __init__(self,name="Login_log",log_file="../log/test.log",level=logging.DEBUG):
        # 1.实例化日志对象，同时设置级别
        # 创建日志记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 创建控制台处理器，并设置颜色格式化
        console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.DEBUG)
        console_formatter = colorlog.ColoredFormatter(
            '%(asctime)s - %(log_color)s%(levelname)s%(reset)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red'
            }
        )
        console_handler.setFormatter(console_formatter)

        # 创建文件处理器，并设置级别及格式化
        file_handler = logging.FileHandler(log_file)
        #file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s %(filename)s (%(lineno)d): %(message)s')
        file_handler.setFormatter(file_formatter)

        # 将处理器添加到日志记录器中
        # self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    # @classmethod
    # def info(cls, param):
    #     pass


if __name__ == '__main__':
    logs=Logger()
    logs.logger.debug("this is a debug message")
    logs.logger.info("this is a info message")
    logs.logger.warning("this is a warning message")
    logs.logger.error("this is a error message")
    logs.logger.critical("this is a critical message")



