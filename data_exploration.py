import pandas as pd
import matplotlib.pyplot as plt


master_df = pd.read_csv('MLB_Ind_Game_Data.csv', encoding='ISO-8859–1')
master_df = master_df.drop(['Code', 'R', 'RA', 'Inn', 'Rank', 'GB', 'Save', 'Time', 'Streak', 'Orig. Scheduled',
                            'Games Back', 'Date.1', 'Date', 'Day Code', 'Wins.1', 'Day_Date', 'Streak.1', 'Losses.1',
                            'D/N', 'Win', 'Loss'], axis=1)


'''
dataframe column values
'''
teams = master_df['Team'].unique()
home_avg_attendance = []
fans_per_year = []
away_draw_power = []
win_pct = []
wins = []
fans_per_win = []
wins_per_season = []



for team in teams:
    overall_df = master_df[master_df['Team'] == team]
    win_count = len(overall_df[overall_df['Wins'] == 1])
    game_count = len(overall_df)
    wins.append(win_count)
    win_pct.append(round((win_count/game_count)*100, 2))

'''
loop calculating total home attendance and average home attendance/game for each team
'''
for team in teams:
    home_df = master_df[master_df['Home Team'] == team]
    total_attendance = home_df['Attendance'].sum()
    avg_attendance = home_df['Attendance'].mean()
    home_avg_attendance.append(avg_attendance)


'''
loop calculating average difference in attendance vs. the norm for each team when they play away
'''
for team in teams:
    opp_df = master_df[master_df['Away Team'] == team]
    avg_draw_diff = opp_df['Attendance vs Avg'].mean()
    away_draw_power.append(avg_draw_diff)



'''
loop calculating average yearly attendance (81 home games in an MLB season)
'''
for value in home_avg_attendance:
    fans_per_year.append(value*81)


'''
creating final dataframe
'''
final_df = {'Team': teams,
            'Avg. Home Attendance': home_avg_attendance,
            'Fans/yr': fans_per_year,
            'Away draw power': away_draw_power,
            'Win %': win_pct,
            'Total Wins': wins}

for i in range(0,len(final_df['Team'])):
    fans_per_win.append(final_df['Fans/yr'][i]/final_df['Total Wins'][i])

for i in range(0,len(final_df['Team'])):
    wins_per_season.append(round(final_df['Total Wins'][i]/7, 2))

final_df['Avg. Wins/Season'] = wins_per_season
final_df['Fans/win'] = fans_per_win

final_df = pd.DataFrame(final_df)
final_df = final_df.drop([30, 31, 32, 33])
final_df[['Avg. Home Attendance',
          'Fans/yr', 'Away draw power']] = final_df[['Avg. Home Attendance',
                                                     'Fans/yr', 'Away draw power']].astype(int)

final_df = final_df.sort_values(by=['Avg. Home Attendance'], ascending=False)


final_df = final_df.reset_index()


plt.bar(final_df['Team'],final_df['Avg. Home Attendance'])
plt.xlabel('Team')
plt.ylabel('Avg. Home Attendance')
plt.show()

plt.scatter(final_df['Avg. Wins/Season'],final_df['Fans/yr'])
plt.show()

plt.bar(final_df['Team'], final_df['Away draw power'])
plt.show()

print(final_df)