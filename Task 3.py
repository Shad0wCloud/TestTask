import mysql.connector
from mysql.connector import Error



def CreateConnection(host_name, user_name, user_password): #подключение к бд
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
    except Error as e:
        print(e)
    return connection
	
def ExecuteQuery(connection, query): #выполнение запроса
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)	


'''
Под понятием "Злостный читатель" я подразумеваю студента(читателя), который взял 2 и более копии одинаковой книги
Алгоритм основан на БД из первого задания

Сам алгоритм:

Мы пробегаемся по каждой записи в нашем массиве запроса, в начале каждой итерацию достаем айди книги и айди студента,
после чего ищем в оставшемся массиве запроса строчки, где айди студента и айди книги совпадают.
Если такая строка найдена, то count++
После прохождения вложенного цикла for, мы проверяем переменную count, и если она больше 1, то записываем студента в список злостных читателей

Я предусмотрел то, что мой алгоритм может записать два раза одинаковый айди, и с помощью set избавляюсь от одинаковых записей
'''
def GetBadReaders(students):  # метод по поиску злостных читателей
    badReaders = []  # создаем массив для злостных читателей
    for i in range(0, len(students)):  # в данном цикле мы ищем читателей, у которых больше одной одинаковой копии книги
        count = 1  # сколько одинаковых копий у студента
        StudentId = students[i][0] #достаем айди студента
        bookId = students[i][1] #достаем айди книги
        for j in range(i + 1, len(students)): #проверяем, сколько у студента одинаковых копий книг
            if (students[j][1] == bookId and students[j][0] == StudentId):
                count = count + 1
        if (count > 1): # если у студента больше 1 копии, то мы записываем его в злостных читателей
            badReaders.append(StudentId)
    if(badReaders == []):
        return "No bad readers"
    return (set(badReaders))
	
	
connection = CreateConnection("localhost", "root", "root123")
query = "SELECT StudentId, BookId FROM Students"
students = ExecuteQuery(connection, query)
badReaders = GetBadReaders(students)
print(badReaders)

