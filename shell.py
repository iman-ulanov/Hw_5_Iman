from restaurant.models import *

user1 = Client(user=User.objects.create(email='nikname21@gmail.com', password='defender42'),
               name='Нурсултан Бердиев', card_number='4147 5657 9878 9009')
user1.save()

user2 = Worker(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'),
               name='Алтынай Алиева', position='Оператор кассы')
user2.save()

cheese = Ingredient.objects.create(name='Сыр', extra_price=80, calories=150)
chicken = Ingredient.objects.create(name='Курица', extra_price=100, calories=250)
beef = Ingredient.objects.create(name='Говядина', extra_price=120, calories=300)
salad = Ingredient.objects.create(name='Салат', extra_price=50, calories=50)
french_fries = Ingredient.objects.create(name='Фри', extra_price=50, calories=70)
fish = Ingredient.objects.create(name='Рыба', extra_price=120, calories=270)
rice = Ingredient.objects.create(name='Рис', extra_price=70, calories=100)
cottage = Ingredient.objects.create(name='Творог', extra_price=100, calories=170)
eggs = Ingredient.objects.create(name='Яйца', extra_price=50, calories=120)

food1 = Food.objects.create(name='Шаурма', start_price=200, calories=500, type_of_cuisine='Турецкая')
food2 = Food.objects.create(name='Гамбургер', start_price=180, calories=350, type_of_cuisine='Американская')
food3 = Food.objects.create(name='Паста', start_price=450, calories=400, type_of_cuisine='Итальянская')
food4 = Food.objects.create(name='Боул', start_price=600, calories=500, type_of_cuisine='Японская')
food5 = Food.objects.create(name='Суши', start_price=400, calories=450, type_of_cuisine='Японская')

order1 = Order.objects.create(food=food1, client=user1, worker=user2)
order1.ingredients.set([cheese, beef, salad, french_fries])

order2 = Order.objects.create(food = food2, client=user1, worker=user2)
order2.ingredients.set([chicken, salad])

order3 = Order.objects.create(food=food3, worker=user2, client=user1)
order3.ingredients.set([cheese, cottage, salad, eggs])

order4 = Order.objects.create(food=food5,client=user1, worker=user2)
order4.ingredients.set([rice, fish, eggs])

order5 = Order.objects.create(food=food4, client=user1, worker=user2)
order5.ingredients.set([rice, cheese, salad, french_fries, cottage])

order6 = Order.objects.create(food=food2, client=user1, worker=user2)
order6.ingredients.set([cheese, salad, beef])

order7 = Order.objects.create(food=food1, client=user1, worker=user2)
order7.ingredients.set([cheese, salad, beef, fish])

order8 = Order.objects.create(food=food3, client=user1, worker=user2)
order8.ingredients.set([cheese, salad, chicken])

print(order1.final_price)
