import csv

total = dict()
loc_max = None
loc_min = None

def check_num(value:str) -> int:
    if value == '-':
        return 0
    else:
        try:
            return int(value)
        except:
            return 0

def f1(x):
    return total[x]

def main():
    with open('covid19.csv', 'r', encoding='utf-8') as covid19:
        csv_reader = csv.reader(covid19)
        next(csv_reader)
        
        print("%s %9s %9s %9s %9s" % ('시도', '계', '10월', '11월', '12월'))
        for row in csv_reader:
            oct = check_num(row[2])
            nov = check_num(row[3])
            dec = check_num(row[4])
            sum = oct + nov + dec

            total[row[1]] = sum
            print("%s %10s %10s %10s %10s" % (row[1], format(sum, ','), format(oct, ','), format(nov, ','), format(dec, ',')))

    loc_max = max(total.keys(), key=f1)
    loc_min = min(total.keys(), key=(lambda k: total[k]))

    print("{0}에서 {1}명으로 확진자가 가장 많이 발생했으며,".format(loc_max, format(total[loc_max], ',')))
    print("{0}에서 {1}명으로 확진자가 가장 적게 발생했습니다.".format(loc_min, format(total[loc_min], ',')))

main()

