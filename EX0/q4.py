current_population = int('312_033_422')
seconds_per_year = 365 * 24 * 60 * 60

births = seconds_per_year // 7
deaths = seconds_per_year // 13
immigrants = seconds_per_year // 45

increase_per_year = births - deaths + immigrants

for year in range(1,6):
    current_population = current_population + increase_per_year
    print("第", year, "年的人口數為：", current_population)
