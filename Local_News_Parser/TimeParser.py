'''
Class consisting of static functions to manipulate time-related item strings
into numbers/standardized strings.

@author diproray
'''
class TimeParser:

    #TODO: try replacing this function with Python's date-time library.
    @staticmethod
    def get_month_from_text(month_string):

        month_to_mm = {
            "January":"01",
            "February":"02",
            "March":"03",
            "April":"04",
            "May":"05",
            "June":"06",
            "July":"07",
            "August":"08",
            "September":"09",
            "October":"10",
            "November":"11",
            "December":"12"
        }

        for month, month_num in month_to_mm.items():
            if (month_string.lower() == month.lower()):
                return month_num
                
        return None
