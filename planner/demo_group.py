from tspu_api import get_groups, build_faculty_tree

groups = get_groups()
tree = build_faculty_tree(groups)

print("Всего групп:", len(groups))
print("Факультеты:", ", ".join(sorted(tree.keys())))

# пример: вывести группы ФМФ 3 курса
print("\nФМФ, 3 курс:")
for g in tree.get("ФМФ", {}).get("3", []):
    print("-", g)
