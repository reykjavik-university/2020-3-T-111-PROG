import csv


def main():
    active_customers_by_month = read_active_customers_file()
    show_premium_customers(active_customers_by_month)
    show_new_customers(active_customers_by_month)
    show_dormant_customers(active_customers_by_month)


def read_active_customers_file() -> dict:
    with open("active_customers_by_month.csv") as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return group_customers_by_month(rows)


def group_customers_by_month(rows: list) -> dict:
    active_customers_by_month = {}
    for month, customer_name in rows:
        if month not in active_customers_by_month:
            active_customers_by_month[month] = set()
        active_customers_by_month[month].add(customer_name)
    return active_customers_by_month


def show_premium_customers(active_customers_by_month: dict):
    premium_customers = None
    for customers in active_customers_by_month.values():
        if premium_customers is None:
            premium_customers = customers
        else:
            premium_customers = premium_customers.intersection(customers)
    show_customer_set("Premium customers", premium_customers)


def show_new_customers(active_customers_by_month: dict):
    last_month = max(active_customers_by_month.keys())
    customers_last_month = active_customers_by_month[last_month]

    older_customers = set()
    for month, customers in active_customers_by_month.items():
        if month != last_month:
            older_customers.update(customers)

    new_customers = customers_last_month - older_customers
    show_customer_set("New customers", new_customers)


def show_dormant_customers(active_customers_by_month: dict):
    all_customers = get_all_customers(active_customers_by_month)
    customers_active_in_the_last_two_months = get_recently_active_customers(
        active_customers_by_month, number_of_months=2
    )
    dormant_customers = all_customers - customers_active_in_the_last_two_months
    show_customer_set("Dormant customers", dormant_customers)


def get_all_customers(active_customers_by_month: dict) -> set:
    all_customers = set()
    for customers in active_customers_by_month.values():
        all_customers.update(customers)
    return all_customers


def get_recently_active_customers(active_customers_by_month: dict, number_of_months: int) -> set:
    sorted_months = sorted(active_customers_by_month.keys())
    last_n_months = sorted_months[-number_of_months:]
    recently_active_customers = set()
    for month in last_n_months:
        recently_active_customers.update(active_customers_by_month[month])
    return recently_active_customers


def show_customer_set(heading: str, customers: set):
    print(heading)
    print("-" * 40)
    for customer in sorted(customers):
        print(customer)
    print()


main()
