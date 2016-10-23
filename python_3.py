hr = float(raw_input('Enter hours: '))
rt = float(raw_input('Enter rate: '))
if hr > 40:
    ab40 = hr - 40
    pay = 40 * rt + ab40 * (rt * 1.5)
else:
    pay = hr * rt
print 'Pay:', pay