class Stack:

    def __init__(self):
        self.items = [] #Задаем Стак на основании списка

    def isEmpty(self): #Проверка пустой Stack
        return self.items == []

    def push(self, item): #Добавляет элемент в стак
        self.items.insert(0,item)

    def pop(self): #Удаляет элемент в стак
        return self.items.pop(0)

    def peek(self): #Возвращает верхний элемент в стак
        return self.items[0]

    def size(self): #Возвращает кол-во элементов в стаке
        return len(self.items)

def balance(text: str) -> str:
    text_stack = Stack()
    open_dict = {'(': ')', '[': ']', '{': '}'}
    close_dict = {')': '(', ']': '[', '}': '{'}
    for x in text:
        if x in open_dict: text_stack.push(x)
        elif text_stack.size() != 0:
            if text_stack.peek() == close_dict[x]: text_stack.pop()
            else: return 'Несбалансированно'
        else: return 'Несбалансированно'
    if text_stack.isEmpty(): return 'Сбалансированно'
    else: return 'Несбалансированно'



if __name__ == '__main__':
    var1 = '(((([{}]))))'
    var2 = '[([])((([[[]]])))]{()}'
    var3 = '{{[()]}}'
    var4 = '}{}'
    var5 = '{{[(])]}}'
    var6 = '[[{())}]'

    print(balance(var1))
    print(balance(var2))
    print(balance(var3))
    print(balance(var4))
    print(balance(var5))
    print(balance(var6))


