import pandas as pd

master_df = pd.read_csv('MLB_Ind_Game_Data.csv', encoding='ISO-8859–1')


master_df = master_df.drop(['Code','R','RA','Inn','Rank','GB','Save','Time','Streak','Orig. Scheduled', 'Games Back','Date.1','Date','Day Code','Wins.1','Day_Date','Streak.1','Losses.1','D/N','Win','Loss'], axis=1)

teams = master_df['Team'].unique()
home_avg_attendance = []
avg_yearly_attendance = []
away_draw_difference = []


for team in teams:
    home_df = master_df[master_df['Home Team'] == team]
    total_attendance = home_df['Attendance'].sum()
    avg_attendance = home_df['Attendance'].mean()
    home_avg_attendance.append(avg_attendance)
    games = len(home_df['Attendance'])

for team in teams:
    opp_df = master_df[master_df['Away Team'] == team]
    avg_draw_diff = opp_df['Attendance vs Avg'].mean()
    away_draw_difference.append(avg_draw_diff)




home_teams_df = {'Team': teams,
                 'Avg. Home Attendance': home_avg_attendance,
                 'Away draw power': away_draw_difference}

home_teams_df = pd.DataFrame(home_teams_df)


for value in home_avg_attendance:
    avg_yearly_attendance.append(value*81)


home_teams_df['Fans/yr'] = avg_yearly_attendance
home_teams_df = home_teams_df.drop([30,31,32,33])

home_teams_df[['Avg. Home Attendance', 'Fans/yr', 'Away draw power']] = home_teams_df[['Avg. Home Attendance', 'Fans/yr', 'Away draw power']].astype(int)




print(home_teams_df)

