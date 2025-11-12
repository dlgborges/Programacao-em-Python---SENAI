import statistics as st

comp1 = [1000,6000,1200,8000,1400]

comp2 = [5000,4000,3000,2000,7000]

comp3 = [1200,1300,8000,3000,15000]

comp4 = [1400,1750,2000,4500,5900]

comps = [comp1, comp2, comp3, comp4]
comps_names = ['Companhia nro 1', 'Companhia nro 2', 'Companhia nro 3', 'Companhia nro 4']

def mean(list):
    print('We are calculating the mean of the input data....', 'The mean of the input data is: ', st.mean(list))

def mode(list):
    print('We are calculating the mode of the input data....', 'The mode of the input data is: ', st.mode(list))

def median(list):
    print('We are calculating the median of the input data....', 'The median of the input data is: ', st.median(list))

def std_dev(list):
    print('We are calculating the standard deviation of the input data....', 'The standard deviation of the input data is: ', round(st.stdev(list),2))

def all_metrics(list):
    mean(list)
    mode(list)
    median(list)
    std_dev(list)

def main():
    for index, comp in enumerate(comps):
        print(f'Let\'s analyze salary data for: {comps_names[index]}.')
        all_metrics(comp)
        input('Continue? (Press ENTER to continue)')
    print('All salary data has been analyzed. Bye!')

main()