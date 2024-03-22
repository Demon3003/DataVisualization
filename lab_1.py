
import matplotlib.pyplot as plt
import numpy as np

# 12 Позиційне порівняння (тип) У серпні два студенти обігнали за успішністю шість інших студентів.

# Успішність двох студентів
students = ['Студент 1', 'Студент 2']
grades = [85, 82]

# Успішність шести інших студентів
other_students = ['Студент 3', 'Студент 4', 'Студент 5', 'Студент 6', 'Студент 7', 'Студент 8']
other_grades = [75, 78, 70, 80, 72, 76]

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.bar(students, grades, color='blue', label='Два студенти')
plt.bar(other_students, other_grades, color='orange', label='Інші студенти')
plt.xlabel('Студенти')
plt.ylabel('Бали')
plt.title('Порівняння успішності студентів у серпні')
plt.legend()
plt.show()

# 11 Кореляційне порівняння (тип) Спостерігається зв'язок між доходами і зарплатою

# Згенеруємо дані для доходів та зарплати
np.random.seed(0)
income = np.random.normal(50000, 15000, 100)  # середнє значення 50000, стандартне відхилення 15000
salary = income + np.random.normal(0, 10000, 100)  # зарплата залежить від доходів з додаванням шуму

x1 = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000])
y1 = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000])

# Побудова графіка розсіювання
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, c = 'red')
plt.scatter(income, salary, color='blue')
plt.title('Зв\'язок між доходами та зарплатою')
plt.xlabel('Доходи')
plt.ylabel('Зарплата')
plt.grid(True)
plt.show()

# 10 Покомпонентне порівняння Найбільша частка фондів задіяна у виробництві.

# Згенеруємо дані для часток фондів
sectors = ['Виробництво', 'Торгівля', 'Послуги', 'Транспорт', 'Сільське господарство']
funds_share = np.random.rand(len(sectors)) * 100
funds_share[0] = np.max(funds_share) + 100  # Задамо найбільшу частку фондів для виробництва

# Побудова графіку
plt.figure(figsize=(9, 10))
plt.pie(funds_share, labels=sectors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Рівні вісі
plt.title('Частка фондів у різних секторах економіки', loc= 'left')
plt.show()

# 9 Часове порівняння Прибутковість акцій у компанії скорочується.

# # Згенеруємо дані для прибутковості акцій протягом року (у місячних інтервалах)
months = np.arange(1, 13)
profitability = [15, 16, 17, 19, 20, 17, 16, 14, 13, 12, 11, 10]  # середня прибутковість 10%, стандартне відхилення 3%

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(months, profitability, marker='o', color='blue', linestyle='-')
plt.title('Прибутковість акцій протягом року')
plt.xlabel('Місяці')
plt.ylabel('Прибутковість (тис. $)')
plt.xticks(months)
plt.grid(True)
plt.show()

# 8 Позиційне порівняння Центральний регіон займає останнє місце з народжуваності.

# # Згенеруємо дані для народжуваності в різних регіонах
regions = ['Північний', 'Східний', 'Західний', 'Південний', 'Центральний']
birth_rates = [50, 40, 39, 39, 12]  # народжуваність на 10000 осіб
lowest_birth_rate_region = 'Центральний'

# # Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(regions, birth_rates, color='blue')
plt.xlabel('Регіони')
plt.ylabel('Народжуваність (на 10000 осіб)')
plt.title('Порівняння народжуваності за регіонами')
plt.text(4, birth_rates[4], f'Найнижча\n({lowest_birth_rate_region})',
         ha='center', va='bottom', color='red')
plt.grid(axis='y')
plt.show()

# 7 Позиційне порівняння. Торік найбільша плинність кадрів спостерігалась у віковій групі від 30 до 35 років.

# # # Вікові групи
age_groups = ['18-25', '26-29', '30-35', '36-40', '41-45']

turnover_rates = [4, 3, 15, 7, 2]

# # Знаходимо вікову групу з найбільшою плинністю кадрів
max_turnover_age_group = '30-35'

# # Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(age_groups, turnover_rates, color='blue')
plt.xlabel('Вікові групи')
plt.ylabel('Коефіцієнт плинності кадрів (%) за минулий рік')
plt.title('Порівняння плинності кадрів за віковими групами')
plt.text(2, turnover_rates[2], f'Найбільша\n({max_turnover_age_group})',
         ha='center', va='bottom', color='red')
plt.grid(axis='y')
plt.show()


# 6 Кореляційне порівняння. Розмір надбавки до зарплати не залежить від трудового стажу.

# Згенеруємо випадкові дані для трудового стажу та розміру надбавки до зарплати
n = 100
years_of_experience = np.random.randint(0, 30, n)  # Трудовий стаж у роках
bonus_amount = np.random.uniform(0, 1000, n)  # Розмір надбавки до зарплати

# # Побудова графіка розсіювання
plt.figure(figsize=(8, 6))
plt.scatter(years_of_experience, bonus_amount, color='blue')
plt.title('Залежність розміру надбавки до зарплати від трудового стажу')
plt.xlabel('Трудовий стаж (роки)')
plt.ylabel('Розмір надбавки до зарплати')
plt.grid(True)
plt.show()


# 5 Покомпонентне порівняння. Продавець магазину проводить з клієнтами лише 15% свого робочого часу.

# # Дані про частку часу, який проводить продавець з клієнтами та іншими справами
time_with_clients = 15
time_with_other_activities = 100 - time_with_clients

# # Назви сегментів для кругової діаграми
labels = ['Час з клієнтами', 'Інші справи']

# # Дані для кругової діаграми
sizes = [time_with_clients, time_with_other_activities]

# # Побудова кругової діаграми
plt.figure(figsize=(9, 9))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Рівні вісі
plt.title('Використання часу продавця')
plt.show()

# 4 Позиційне порівняння. У вересні рівень плинності кадрів у шести підрозділах був приблизно однаковий. 

# # Назви підрозділів
departments = ['Підрозділ 1', 'Підрозділ 2', 'Підрозділ 3', 'Підрозділ 4', 'Підрозділ 5', 'Підрозділ 6']

# # Рівень плинності кадрів у вересні у шести підрозділах
turnover_rates = [10, 9, 10, 9, 10, 10]

# # Побудова графіка
plt.figure(figsize=(10, 8))
plt.bar(departments, turnover_rates, color='skyblue')
plt.title('Рівень плинності кадрів у вересні за підрозділами')
plt.xlabel('Підрозділи')
plt.ylabel('Коефіцієнт плинності кадрів %')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# 3 Кореляційне порівняння. Підвищення ціни на окремі сорти бензину не означає підвищення їх якості.

# # Згенеруємо випадкові дані для ціни та якості бензину
n = 15
price = np.random.uniform(1, 2, n)  # Випадкові ціни бензину
quality = np.random.uniform(1, 10, n)  # Випадкові оцінки якості бензину

# # Побудова графіка
plt.figure(figsize=(8, 6))
plt.scatter(price, quality, color='blue')
for i in range(len(price)):
    plt.text(price[i]+.03, quality[i]+.03, f'Марка: {i+1}', fontsize=9)
plt.title('Залежність ціни бензину від його якості')
plt.xlabel('Ціна')
plt.ylabel('Якість')
plt.grid(True)
plt.show()



# 2 Позиційне порівняння. Більшість співробітників отримує зарплату від 10 до 15 тис. гривень


people = [20, 50, 12, 10]

# # Визначимо проміжки зарплат
salary_bins = ['5000-9000', '10000-15000', '160000-30000', '31000-50000']


# # Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(salary_bins, people, color='blue')
plt.xlabel('Зарплата, грн.')
plt.ylabel('Кількість співробітників')
plt.title('Гістограма зарплат співробітників')
plt.show()



# 1 Часове порівняння. Протягом наступних десяти років прогнозується зменшення кількості навчальних закладів

# # Роки
years = np.arange(2024, 2034)

# # Прогноз кількості навчальних закладів
schools_forecast = np.array([500, 480, 460, 440, 420, 400, 380, 360, 340, 320])

# # Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(years, schools_forecast, marker='o', color='blue', linestyle='-')
plt.title('Прогноз зменшення кількості навчальних закладів')
plt.xlabel('Рік')
plt.ylabel('Кількість навчальних закладів')
plt.grid(True)
plt.show()
