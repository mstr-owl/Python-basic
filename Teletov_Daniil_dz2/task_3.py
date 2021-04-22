season_list=[('Winter',1,2,12),('Spring',3,4,5),('Summer',6,7,8),('Autumn',9,10,11)]
season_dict={'Winter':{1,2,12},'Spring':{3,4,5},'Summer':{6,7,8},'Autumn':{9,10,11}}
# number_month=int(input("Enter the month number:"))
number_month=7
for i in range(len(season_list)):
    if number_month in season_list[i]:
        print(season_list[i][0])

for season, month in season_dict.items():
    if number_month in month:
        print(season)
