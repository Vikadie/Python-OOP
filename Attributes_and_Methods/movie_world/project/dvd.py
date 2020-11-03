class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    def __init__(self, name: str, id: int, creation_year:int, creation_month: str, age_restriction: int):
        self.name: str = name
        self.id: int = id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented: bool = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) :
        month_dict = { '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
                       '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
        day, month_num, year_str = date.split('.')
        year = int(year_str)
        month = month_dict[month_num]
        return cls(name, id, year, month, age_restriction)
