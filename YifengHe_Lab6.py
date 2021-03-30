# Yifeng He Lab 6
sourcefile_name = 'C:/Users/Yifeng He/Desktop/IO/Loans.csv'
destinationfile_name = 'C:/Users/Yifeng He/Desktop/IO/LoansWithFutureValue.csv'

def calculate_futurevalue(p, r, t, n = 365):
    p_float = float(p.replace('$', '').replace(',', ''))
    r_float = float(r.replace('%', ''))*.01
    t_float = float(t)
    a = p_float*(1 + r_float/n)**(n*t_float)
    return a
with open(sourcefile_name, 'r', encoding='utf-8') as sf, open(destinationfile_name, 'a', encoding='utf-8') as df:
    line = sf.readline()
    line = sf.readline()
    df.write('Loan ID, First Name, Last Name, Loan Principle, Annual Interest Rate,Term, Future Value\n')
    while line != '':
        line = line.replace('\n', '')
        line_list = line.split(',')
        loan_ID = line_list[0]
        first_name = line_list[1]
        last_name = line_list[2]
        loan_principle = line_list[3]
        interest = line_list[4]
        term = line_list[5]
        fV = calculate_futurevalue(loan_principle, interest, term)
        line = sf.readline()
        df.write(loan_ID+','+first_name+','+last_name+','+loan_principle+','+interest+','+term+','+str(fV)+'\n')
