class BaseIncome:
    """
    Basic class include parameters of income for all groups of people

    people_count - (int), number of people of specific group
    average_income - (int), average income for 1 person of specific group in BYN
    personal_tax_rate - (int), personal tax rate in percent for specific group. Default value for most of groups is "13"
    organization_tax_rate - (int) organization tax rate in percent for specific group.Default value for most of groups
    is "34"

    annual_income - (float) method returns annual value of taxes for one specific group
    """

    def __init__(self, people_count, average_income, personal_tax_rate=13, organization_tax_rate=34):
        self.people_count = people_count  # set average people base
        self.average_income = average_income  # set average income for 1 person
        self.personal_tax_rate = personal_tax_rate / 100  # set personal tax rate for specific business branch
        self.organization_tax_rate = organization_tax_rate / 100  # set organization tax rate

    def annual_income(self):
        return self.people_count * (self.average_income * (self.personal_tax_rate + self.organization_tax_rate))


class BaseExpenses:
    """
    Basic class include parameters of expenses for all groups of people

    people_count - (int), number of people of specific group
    average_payment - (int), average expenses for 1 person of specific group in BYN
    """

    def __init__(self, people_count, average_payment):
        self.people_count = people_count  # set average people base
        self.average_payment = average_payment  # set average payment for 1 person

# test comment to check synch in two rep