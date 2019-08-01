hotel_daily_rates = [
    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 80),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]
maximum_daily_rate = 300
aff_hotels = []
#find the suitable hotels
for i in hotel_daily_rates :
    if maximum_daily_rate >= i[1] :
        aff_hotels.append(i)
#sort them by the ascending
aff_hotels = sorted(aff_hotels, key=lambda i: i[1])
#remove the prices
aff_hotels_names = []
for i in aff_hotels :
    aff_hotels_names.append(i[0])
print(aff_hotels_names);
