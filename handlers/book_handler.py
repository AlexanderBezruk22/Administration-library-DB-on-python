import json
import logging


class Book:
    def __init__(self, filename: str):
        self.filename = filename

    def BookTemplate(self, title: str, author: str, year: int) -> dict:

        template = {
            "Title": f"{title}",
            "Author": f"{author}",
            "Year": f"{year}",
            "Status": "В наличии"
        }

        return template

    def AllData(self):
        try:
            file = open(self.filename, mode="r", encoding="utf-8")
            print(file.read().strip())
        except:
            logging.error("File is empty")

    def ReadJson(self) -> dict:

        file = open(self.filename, mode="r", encoding="utf-8")
        result = json.load(file)
        file.close()
        return result

    def AddToJson(self, data: dict):

        try:
            file = open(self.filename, mode="w", encoding="utf-8")
            json.dump(data, file, indent=5, ensure_ascii=False)
            file.close()

        except Exception as err:
            logging.error(f"ERROR 1002: {err}")

    def UpdateBook(self, id: str, status: str) -> dict:
        id = str(id)
        data = self.ReadJson()
        try:
            temp = data[id]
            temp["status"] = status
            data[id] = temp
            self.AddToJson(data)
            return {"Success": 200}
        except Exception as err:
            logging.error(f"Book with that Id doesn`t exist: {err}")
    def UniqueId(self) -> str:

        try:
            readFile = open(self.filename)
            output_list = []
            data = json.load(readFile)

            for key, value in data.items():
                output_list.append(int(key))

            max_id = max(output_list) + 1
            return str(max_id)
        except:
            return "1"



    def AddABook(self, title: str, author: str, year: str) -> dict:

        try:
            final_data = self.ReadJson()
            data = self.BookTemplate(title, author, year)
            id = self.UniqueId()
            final_data[id] = data
            self.AddToJson(final_data)
            return {"Success": 200}

        except:
            try:
                data = self.BookTemplate(title, author, year)
                id = self.UniqueId()
                final_data = {}
                final_data[id] = data
                self.AddToJson(final_data)
                return {"Success": 200}
            except:
                logging.error("Occurred with adding a book")


    def DeleteABook(self, id: str) -> dict:
        data = self.ReadJson()
        try:
            data.pop(str(id))
            self.AddToJson(data)
            return {"Success": 200}
        except Exception as err:
            logging.error(f"Trouble with deleting book, book with that id doesn`t exist: {err}")

    def FindABook(self, query):
        query = str(query)
        data = self.ReadJson()
        output_data = {}
        try:
            for key, value in data.items():
                if (value['Title'] == query or value['Author'] == query or value['Year'] == query):
                     output_data[f"id: {key}"] = data[key]

            return output_data
        except Exception as err:
            logging.error(f"Occurred with finding a book; \nBook dont find; {err}")