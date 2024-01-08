inp = eval(input("Input Seconds: "))

sec = inp % (24 * 3600)
mins = sec // 60
sec %= 60

print(str(inp) + " seconds is: " + str(mins) + " minute(s) " + str(sec) + " second(s)")
