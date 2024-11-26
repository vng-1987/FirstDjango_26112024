from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	text = """
		<h1>"Изучаем django"</h1>
		<strong>Автор</strong>: <i>Иванов И.П.</i>
	"""
	return HttpResponse(text)

def about(request):
	FirstName = "Иван"
	LastName = "Иванов"
	MiddleName = "Петрович"
	Telefon = "8-923-600-01-02"
	Email = "vasya@mail.ru"
	text = f"""
		Имя: <strong>{FirstName}</strong><br>
		Отчество: <strong>{MiddleName}</strong><br>
		Фамилия: <strong>{LastName}</strong><br>
		телефон: <strong>{Telefon}</strong><br>
		email: <strong>{Email}</strong><br>
	"""
	return HttpResponse(text)

def items(request, id=0):
	items = [
		{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
		{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
		{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
		{"id": 7, "name": "Картофель фри" ,"quantity":0},
		{"id": 8, "name": "Кепка" ,"quantity":124},
		]
	text = f"""{items[0]}"""

	print(f"Количество элементов списка items:\n\t{len(items)}")
	print(f"id страницы = {id}")

	if id == 0:
		text = f"""
			<h2>Список товаров</h2><hr>
			<ul>
				<li><a href="http://127.0.0.1:8000/items/1"><strong>{items[0]['name']}</strong> в количестве: <strong>{items[0]['quantity']}</strong> шт</a></li>
				<li><a href="http://127.0.0.1:8000/items/2"><strong>{items[1]['name']}</strong> в количестве: <strong>{items[1]['quantity']}</strong> шт</a></li>
				<li><a href="http://127.0.0.1:8000/items/5"><strong>{items[2]['name']}</strong> в количестве: <strong>{items[2]['quantity']}</strong> шт</a></li>
				<li><a href="http://127.0.0.1:8000/items/7"><strong>{items[3]['name']}</strong> в количестве: <strong>{items[3]['quantity']}</strong> шт</a></li>
				<li><a href="http://127.0.0.1:8000/items/8"><strong>{items[4]['name']}</strong> в количестве: <strong>{items[4]['quantity']}</strong> шт</a></li>
			<ul>
		"""
			
	else: 
		for x in range(len(items)):
			if items[x]['id'] == id:
				print(f"1_{items[x]['id']}")
				text = f"""
					<h2>Товар</h2><hr> <strong>{items[x]['name']}</strong> в количестве: <strong>{items[x]['quantity']}</strong> шт<br><hr>
					<a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>
				"""
				break
			else:
				print(f"2_{items[x]['id']}")
				text = f"""
					Товар с <strong>id={id}</strong> не найден<br><hr>
					<a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>
				"""
	return HttpResponse(text)