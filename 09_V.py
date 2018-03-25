# 09_V1
print('adjapegeeb'[int(input()) - 1])

# 09_V2
fac = '{}!'.format
oneterm = '{0}**{1}/{1}!'.format
def sin(x,n):
	out = str(x)
	sign = True
	for i in range(3, 2 * n, 2):
		out += ' {} {}'.format('+-'[sign], oneterm(x, i))
		sign ^= True
	return out		
exec(input().strip())

# 09_V3
def read_date():
    d, m, y = input().split()
    month = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    return (int(d), month.index(m) + 1, int(y))

def zodiac(d, m):
    return next(z for (d1, m1), (d2, m2), z in [
      [(22,3), (21,4), "Aries"      ],
      [(22,4), (21,5), "Taurus"     ],
      [(22,5), (21,6), "Gemini"     ],
      [(22,6), (21,7), "Cancer"     ],
      [(22,7), (21,8), "Leo"        ],
      [(22,8), (21,9), "Virgo"      ],
      [(22,9), (21,10),"Libra"      ],
      [(22,10),(21,11),"Scorpio"    ],
      [(22,11),(21,12),"Sagittarius"],
      [(22,12),(20,1), "Capricorn"  ],
      [(21,1), (20,2), "Aquarius"   ],
      [(21,2), (21,3), "Pisces"     ]
    ] if d >= d1 and m == m1 or d <= d2 and m == m2)

def days_in_feb(y):
    return 29 if y % 400 == 0 or y % 100 != 0 and y % 4 == 0 else 28

def days_in_month(m, y):
    return days_in_feb(y) if m is 2 else 30 if m in [4, 6, 9, 11] else 31

def days_in_between(d1 ,m1, y1, d2, m2, y2):
    dm1, dm2 = [[days_in_month(m, y) for m in range(1, 13)] for y in [y1, y2]]
    return (days_in_month(m1,y1) - d1 + 1) + sum(dm1[m1:]) + \
          int((y2 - y1 - 1)*365.25) + sum(dm2[:m2-1]) + (d2 - 1)
def main() :
    p1, p2 = read_date(), read_date()
    print(zodiac(*p1[:2]), zodiac(*p2[:2]))
    print(days_in_between(*p1, *p2))

exec(input().strip())

# 09_V4
def is_odd(x):        return bool(x & 1)
def odd_list(ls):     return list(filter(is_odd, ls))
def sum_square(ls):   return sum(i * i for i in ls)
def make_int_list(s): return list(map(int, s.split()))
exec(input().strip())
