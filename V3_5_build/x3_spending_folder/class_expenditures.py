class CreateNewExpenditure:

    def __init__(self, user_id, exp_name, exp_cost, exp_tags, exp_month, exp_year):
        self.user_id   = user_id
        self.exp_name  = exp_name
        self.exp_cost  = exp_cost
        self.exp_tags  = exp_tags
        self.exp_month = exp_month
        self.exp_year  = exp_year

    def __repr__(self):
        return ("{'id': %d, 'name': '%s', 'cost': %.2f, 'tags': '%s', 'month': %d, 'year': %d}" %
                (int(self.user_id), self.exp_name, float(self.exp_cost), list(self.exp_tags), int(self.exp_month), int(self.exp_year)))





