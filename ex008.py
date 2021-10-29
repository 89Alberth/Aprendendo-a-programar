mt = float(input('Quantos metros tem: '))
dec = mt * 10
cm = mt * 10 * 10
mm = mt * 10 * 10 * 10
deca = mt / 10
hm = mt / 10 / 10
km = mt / 10 / 10 / 10

print('Metros: {}\nDecímetro: {}\nCentímetro: {}\nMilímetro: {}\nDecâmetro: {}\nHectômetro: {}\nQuilômetro: {}'
      .format(mt, dec, cm, mm, deca, hm, km))
