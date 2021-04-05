from datetime import datetime


def deletion_order(data_list, priority='frequency'):
    # convert str to datetime object for the ease of sorting
    for i in data_list:
        i['last_updated'] = datetime.strptime(i['last_updated'], '%d-%m-%Y')
    if priority == 'frequency':
        sorted_list = sorted(data_list, key=lambda i: (i['frequency'], i['last_updated']))
    elif priority == 'last_updated':
        sorted_list = sorted(data_list, key=lambda i: (i['last_updated'], i['frequency']))
    return sorted_list


if __name__ == '_main_':
    test_input = [
        {'id': 'data1', 'last_updated': '18-03-2021', 'frequency': 78},
        {'id': 'data10', 'last_updated': '18-03-2021', 'frequency': 96},
        {'id': 'data11', 'last_updated': '17-03-2021', 'frequency': 80},
        {'id': 'data2', 'last_updated': '24-03-2021', 'frequency': 63},
        {'id': 'data3', 'last_updated': '16-03-2021', 'frequency': 61},
        {'id': 'data4', 'last_updated': '22-03-2021', 'frequency': 59},
        {'id': 'data5', 'last_updated': '19-03-2021', 'frequency': 55},
        {'id': 'data5', 'last_updated': '20-03-2021', 'frequency': 78},
        {'id': 'data6', 'last_updated': '17-03-2021', 'frequency': 89},
        {'id': 'data6', 'last_updated': '22-03-2021', 'frequency': 62},
        {'id': 'data7', 'last_updated': '24-03-2021', 'frequency': 82},
        {'id': 'data8', 'last_updated': '21-03-2021', 'frequency': 69},
        {'id': 'data9', 'last_updated': '24-03-2021', 'frequency': 85}
    ]
    order = deletion_order(test_input,priority='frequency')
    print(order)