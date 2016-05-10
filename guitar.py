class Guitar:
    def __init__(self,name="",year=0,cost=0):
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):
        return"{} ({}): ${:,.2f} added".format(self.name,self.year,float(self.cost))

    def get_age(self):
        age=2016-int(self.year)
        self=age
        return self

    def is_vintage(self):
        if self.get_age()>50:
            return True
        else:
            return False