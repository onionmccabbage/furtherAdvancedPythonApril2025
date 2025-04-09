import pstats

def main():
    '''open a profile report and display the results'''
    p= pstats.Stats('my_profiling/profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()