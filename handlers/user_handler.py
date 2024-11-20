from handlers.book_handler import *
from messages.text import *

book = Book(filename='data.json')

class UserFunctional:


    def CheckReady(self) -> int:
        print("Желаете повторить? \n[0] - Да \n[1] - Нет")
        input_data = input()
        if input_data == 0:
            return 0
        else:
            return 1

    def UserUpdateStatus(self):
        res = -1
        while res != 1:
            try:
                id, status = str(input("Введите ID книги, статус которой нужно обновить: ")), str(input("Введите необходимый статус: "))
                print(book.UpdateBook(id, status))
                res = self.CheckReady()

            except:
                logging.error("Occurred with update status of book")

    def UserAddNewBook(self):
        res = -1
        while res != 1:
            try:
                title = str(input("Введите название книги или введите ОТМЕНА для отмены операции: "))
                if title == "ОТМЕНА":
                    break
                author, year = str(input("\nВведите имя автора: ")),str(input("\nВведите год издания книги: "))
                print(book.AddABook(title, author, year))
                res = self.CheckReady()

            except:
                logging.error("Occurred with adding new book")

    def UserGetAllData(self):
        try:
            book.AllData()
            input("Нажмите Enter для продолжения")

        except:
            logging.error("Trouble with out data")

    def UserDeleteABook(self):
        res = -1
        while res != 1:
            try:
                input_id = input("Введите ID книги, которую нужно удалить или напишите ОТМЕНА для отмены: ")
                if input_id.lower() == "ОТМЕНА":
                    break
                print(book.DeleteABook(input_id))
                res = self.CheckReady()

            except:
                logging.error("Error with deleting book in user interface; Wrong ID")


    def UserFindBook(self):
        res = -1
        while res != 1:
            try:
                print("Введите автора, год издания или автора книги ля поиска,введите ОТМЕНА для отмены операции: ")
                input_data = str(input())
                if input_data == "ОТМЕНА":
                    break
                print(book.FindABook(input_data))

            except Exception as err:
                logging.error(f"Book don`t found: {err}")
            res = self.CheckReady()



    def MainInterface(self):
        input_data = None
        while (input_data != 0):
            print(main_message)
            input_data = input()
            try:
                if int(input_data) == 1:
                    self.UserFindBook()
                elif int(input_data) == 2:
                    self.UserAddNewBook()
                elif int(input_data) == 3:
                    self.UserUpdateStatus()
                elif int(input_data) == 4:
                    self.UserGetAllData()
                elif int(input_data) == 5:
                    self.UserDeleteABook()
                elif int(input_data) == 0:
                    break
            except:
                print("Пожалуйста используйте 1,2,3,4,5 или 0 для навигации по меню")