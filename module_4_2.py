def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

#------------ Вызов функций ------------

test_function() # Работает всё отлично

inner_function() # Мы получим ошибку, потому что inner_function() существует только в локальном пространстве функции test_function()