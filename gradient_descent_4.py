input = 2
weight = 0.5
goal_pred = 0.8
alpha = 0.01

for i in range(500):
	# предсказание
	pred = weight * input 
	# среднеквадратическая ошибка
	error = (pred - goal_pred) ** 2
	# чистая ошибка
	delta = pred - goal_pred
	# остановка - обращение знака - масштабирование
	weight -= alpha * (delta * input)

	print(f"Error: {error}\n Prediction: {pred}")