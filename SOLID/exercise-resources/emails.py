# You are provided with code containing class IEmail and class Email. The code does not follow the principle of
# single responsibility (the Email class has 2 responsibilities). Create a new class IContent and a class that
# inherits it called MyContent to split the responsibilities.
from abc import ABCMeta, ABC, abstractmethod


class IContent(ABC):
    @abstractmethod
    def __init__(self, content):
        pass


class MyContent(IContent):

    def __init__(self, content):
        self.__content = ''.join(['<myML>', content, '</myML>'])

    def __repr__(self):
        return f"{self.__content}"


class IEmail:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)