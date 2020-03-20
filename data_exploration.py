import pandas as pd


master_df = pd.read_csv('MLB_Ind_Game_Data.csv', encoding='ISO-8859–1')
master_df = master_df.drop(['Code', 'R', 'RA', 'Inn', 'Rank', 'GB', 'Save', 'Time', 'Streak', 'Orig. Scheduled',
                            'Games Back', 'Date.1', 'Date', 'Day Code', 'Wins.1', 'Day_Date', 'Streak.1', 'Losses.1',
                            'D/N', 'Win', 'Loss'], axis=1)
print(master_df['Wins'])

'''
dataframe column values
'''
teams = master_df['Team'].unique()
home_avg_attendance = []
fans_per_year = []
away_draw_power = []
wins = []



for team in teams:
    overall_df = master_df[master_df['Team'] == team]
    win_count = len(overall_df[overall_df['Wins'] == 1])
    game_count = len(overall_df)
    wins.append(round((win_count/game_count)*100, 2))

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
home_teams_df = {'Team': teams,
                 'Avg. Home Attendance': home_avg_attendance,
                 'Fans/yr': fans_per_year,
                 'Away draw power': away_draw_power,
                 'Win %': wins}

home_teams_df = pd.DataFrame(home_teams_df)

home_teams_df = home_teams_df.drop([30, 31, 32, 33])
home_teams_df[['Avg. Home Attendance',
               'Fans/yr', 'Away draw power']] = home_teams_df[['Avg. Home Attendance',
                                                               'Fans/yr', 'Away draw power']].astype(int)

home_teams_df = home_teams_df.set_index(['Team'])
home_teams_df = home_teams_df.sort_values(by=['Avg. Home Attendance'], ascending=False)


print(home_teams_df)