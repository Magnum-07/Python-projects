import pandas
data = pandas.read_csv('Squirrel_data.csv')
fur_color_data = data['Primary Fur Color']
fur_color_list = fur_color_data.to_list()

# Counting the number of each type of squirrel
Gray_count = fur_color_list.count("Gray")
Cinnamon_count = fur_color_list.count("Cinnamon")
Black_count = fur_color_list.count("Black")
data_dict = {
    'colors': ['Gray', "Cinnamon", "Black"],
    'count': [Gray_count, Cinnamon_count, Black_count]
}
new_df = pandas.DataFrame(data_dict)
new_df.to_csv('new_data.csv')
