from whoosh.query import DateRange
from dateutil.parser import parse as parse_date


def search_in_date(before_date, after_date):
    '''
    Function for creating a query and descriptive text for searching articles by date.

    The function receives strings in the format 'yyyy-mm-dd' for the date before and after.

    It then converts these strings to datetime objects (or None values)
    and uses them to create a query for searching in the schema index,
    and then creates descriptive text according to the search parameters.

    The function returns the created query and descriptive text.
    '''

    # Conversion of provided values to datetime objects or None
    parse_before = parse_date(before_date) if before_date else None
    parse_after = parse_date(after_date) if after_date else None

    # Creating the query
    date_query = DateRange("published",
                           parse_after, parse_before,
                           startexcl=False, endexcl=False)

    # Creating descriptive text for the search result
    display_text = ""
    if before_date:
        display_text += f"published before {parse_before.strftime('%d. %m. %Y')}"
        if after_date:
            display_text += f" and after {parse_after.strftime('%d. %m. %Y')}"
    elif after_date:
        display_text += f"published after {parse_after.strftime('%d. %m. %Y')}"
    display_text += "<br>"

    return date_query, display_text
