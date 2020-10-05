# This program is based on programming project 1 in Chapter 8 in the textbook

COLUMN_DATE = 0
COLUMN_PRICE = 5
COLUMN_VOLUME = 6

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def get_data_list(file_stream):
    ''' Returns a list of data from the given file_stream, excluding the header row '''
    data_list = []
    header = True
    for line_str in file_stream:
        if header:          # strip the header row from the data
            header = False
            continue
        else:
            data_list.append(line_str.strip().split(','))
    return data_list

def add_monthly_averages(monthly_averages_list, last_year_month, weighted_sum, total_volume):
    average = weighted_sum / total_volume
    monthly_averages_list.append((last_year_month, average))

def accumulate(stock_data, weighted_sum, total_volume):
    ''' Accumulate the weighted sum and total volume from the stock data '''
    volume = int(stock_data[COLUMN_VOLUME])
    price = float(stock_data[COLUMN_PRICE])
    weighted_sum += price * volume
    total_volume += volume
    return weighted_sum, total_volume

def get_monthly_averages(data_list):
    ''' The parameter data_list is a list of lists.  Each inner list contains:
        Data, Open, High, Low, Close, Adj Close, Volume.
        Returns the weighed average adjusted closing price for each month '''
    last_year_month = ''
    weighted_sum, total_volume = 0.0, 0
    monthly_averages_list = []

    for data in data_list:
        date = data[COLUMN_DATE]
        year_month = date[:7]   # First six characters denote the year and month
        if year_month != last_year_month and last_year_month != '':
            add_monthly_averages(monthly_averages_list, last_year_month, weighted_sum, total_volume)
            weighted_sum, total_volume = 0.0, 0
        
        weighted_sum, total_volume = accumulate(data, weighted_sum, total_volume)
        last_year_month = year_month
    else:   # process the last month found
        add_monthly_averages(monthly_averages_list, last_year_month, weighted_sum, total_volume)
    return monthly_averages_list

def get_highest(data_list):
    ''' Returns the highest price in the list and the date it occurred on '''
    highest_price = 0
    highest_date = ''

    for data in data_list:
        price = float(data[COLUMN_PRICE])
        if  price > highest_price:
            highest_price = price
            highest_date = data[COLUMN_DATE]
    return (highest_date, highest_price)
    
def print_averages(monthly_averages_list):
    print('{:10}{:>7}'.format("Month", "Price"))
    for data_tuple in monthly_averages_list:
        print('{:10}{:>7.2f}'.format(data_tuple[0], data_tuple[1]))

def print_highest(highest_date, highest_price):
    print('Highest price {:.2f} on day {}'.format(highest_price, highest_date))
    
# Main program starts here
filename = input("Enter filename: ")
file_stream = open_file(filename)
if file_stream:
    data_list = get_data_list(file_stream)
    monthly_averages_list = get_monthly_averages(data_list)
    print_averages(monthly_averages_list)
    highest_date, highest_price = get_highest(data_list)
    print_highest(highest_date, highest_price)
    file_stream.close()
else:
    print("Filename {} not found!".format(filename))