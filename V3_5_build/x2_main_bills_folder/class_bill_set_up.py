class CreateNewBill:

    def __init__(self, bill_id, bill_name, bill_cost, bill_due_date, bill_tags, is_active, bill_year):
        self.bill_id   = bill_id
        self.bill_name = bill_name
        self.bill_cost = bill_cost
        self.bill_due_date = bill_due_date
        self.bill_tags = bill_tags
        self.is_active = is_active
        self.bill_year = bill_year

    def __repr__(self):
        return ("{'id': %d, 'name': '%s', 'cost': %.2f, 'due': %d, 'tags': '%s', 'is_active': %s, 'year': %d}" %
                (int(self.bill_id), self.bill_name, float(self.bill_cost), int(self.bill_due_date),
                 list(self.bill_tags), 'Active' if self.is_active else 'Inactive', int(self.bill_year)))





