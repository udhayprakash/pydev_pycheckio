#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/create-intervals/solve/
"""
from pprint import pprint


class Text:
    def __init__(self):
        self.data = ''
        self.font_name = ''
        self.__version_num = -1
        self.__version_data = {}

    def write(self, data):
        self.__version_num += 1
        self.data += data
        self.__version_data[self.__version_num] = self.data

    def set_font(self, font_name):
        self.font_name = font_name

    def show(self):
        if self.font_name:
            return f'[{self.font_name}]{self.data}[{self.font_name}]'
        else:
            return self.data

    def restore(self, saved_object):
        self.data = saved_object.data
        self.font_name = saved_object.font_name


class SavedText:
    def __init__(self):
        self.verion_no = -1
        self.version_data = {}

    def save_text(self, text_object):
        self.verion_no += 1
        self.version_data[self.verion_no] = text_object
        if len(self.version_data) > 1:
            pprint(self.version_data)
            print(f'self.version_data[0].data:{self.version_data[0].data}')
            print(f'self.version_data[1].data:{self.version_data[1].data}')

    def get_version(self, version_no):
        return version_no
        # return self.version_data[version_no]


if __name__ == '__main__':
    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    # print("Coding complete? Let's try tests!")
