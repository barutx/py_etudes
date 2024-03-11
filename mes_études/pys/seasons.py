import datetime
import sys
import inflect

p = inflect.engine()
def main():
    try: 
        birth = input("Enter your date of birth in the following format: {}-{}-{}: \n".format("YYYY","MM","DD"))
        y,m,d = map(int,birth.split("-"))
        birth_time = datetime.date(y,m,d)
        today = datetime.date.today()
        age = today - birth_time
        s = age.total_seconds()
        m = round(int(s) / 60)
        m_words = p.number_to_words(m)
        print(m_words.title())
    except Exception("Put sth correct!"):
        sys.exit()

main()