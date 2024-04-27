'''
Q6.Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points)
'''
g_pl=int(input("Enter Number of games played:"))
g_w=int(input("Enter Number of games Won:"))
g_l=int(input("Enter Number of games lost:"))

g_tie=g_pl-(g_w + g_l)
t_points = (g_w * 4) + (g_tie * 2)

print(f"Number of tie games:{g_tie}" )
print(f"Total points: {t_points}")