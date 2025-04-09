import pstats

def main():
    '''open a profile report and display the results'''
    p= pstats.Stats('my_profile/profile_output.py')
    p.print_stats()

if __name__ == '__main__':
    main()