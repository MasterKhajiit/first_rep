class BaseIncome:
    """
    Basic class include parameters for all groups of people

    people_count - (int), number of people of specific group
    average_income - (int), average income for 1 person of specific group in BYN
    tax_rate - (int), tax rate in percent for specific group. Default value for most of groups is "13"

    annual_income - (float) method returns annual value of taxes for one specific group
    """

    def __init__(self, people_count, average_income, tax_rate=13):
        self.people_count = people_count  # set average people base
        self.average_income = average_income  # set average income for 1 person
        self.tax_rate = tax_rate / 100  # set tax rate for specific business branch

    def annual_income(self):
        return self.people_count * (self.average_income * self.tax_rate)


class BaseExpenses:
    pass
