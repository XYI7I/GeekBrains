#  Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.
SELECT 'Животное' as source_table, id, name, age, species FROM Животное
UNION
SELECT 'Домашние животные' as source_table, id, name, age, species FROM Домашние_животные
UNION
SELECT 'Вьючные животные' as source_table, id, name, age, species FROM Вьючные_животные
UNION
SELECT 'Собаки' as source_table, id, name, age, species FROM Собаки
UNION
SELECT 'Кошки' as source_table, id, name, age, species FROM Кошки
UNION
SELECT 'Хомяки' as source_table, id, name, age, species FROM Хомяки
UNION
SELECT 'Лошади' as source_table, id, name, age, species FROM Лошади
UNION
SELECT 'Ослы' as source_table, id, name, age, species FROM Ослы
UNION
SELECT 'Молодые животные' as source_table, id, name, age, species, age_months FROM Молодые_животные;
